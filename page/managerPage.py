from datetime import datetime, timedelta
from PyQt5.QtGui import QPixmap, QImage, QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QMessageBox, QHeaderView, QAbstractItemView

from sql.tools import create_db
from ui.manager_page import Ui_Form

"""
    管理员页面, 负责员工管理, 请假管理, 考勤管理等功能
"""


class ManagerPage(QWidget, Ui_Form):
    def __init__(self):
        super(ManagerPage, self).__init__()
        self.setupUi(self)
        self.init_slot()
        self.account = None  # 登录账号
        self.login_flag = False  # 登录标志

    def init_slot(self):
        self.tabWidget.currentChanged.connect(self.on_tab_changed)
        self.enrollBtn.clicked.connect(self.enroll_clicked)  # 连接管理员注册按钮槽函数
        self.loginBtn.clicked.connect(self.login_clicked)  # 连接管理员登录槽函数
        # self.init_userdata()  # 初始化用户数据
        self.delBtn.clicked.connect(self.del_clicked)
        self.findBtn.clicked.connect(self.find_clicked)  # 考勤统计槽函数
        self.leaveBtn.clicked.connect(self.leave_clicked)  # 请假管理槽函数

    def leave_clicked(self):
        """
        请假管理槽函数
        :return:
        """
        work_id = self.work_id__leave_lineEdit.text()  # 获取员工工号
        # 获取combox选择的状态
        state = self.comboBox.currentIndex()  # 0: 事假 1: 病假 2: 调休
        leave_con = None
        if state == 0:
            leave_con = 1
        elif state == 1:
            leave_con = 0
        else:
            QMessageBox.warning(self, '警告', '请选择请假类型！')
            return
        start_time = self.start_lineEdit.text()
        end_time = self.stop_lineEdit.text()
        opion = self.opinion_textEdit.toPlainText()
        if not start_time or not end_time or not work_id or not opion:
            QMessageBox.warning(self, '警告', '请填写完整信息！')
            return
        db, cursor = create_db()
        # 判断该员工是否存在
        sql = "SELECT * FROM workers WHERE work_id = '{}' LIMIT 1".format(int(work_id))
        cursor.execute(sql)
        result = cursor.fetchone()
        if not result:
            QMessageBox.warning(self, '警告', '该员工不存在！')
            return
        # 判断输入的请假日期区间是否有效
        start_time = datetime.strptime(start_time, '%Y-%m-%d')
        end_time = datetime.strptime(end_time, '%Y-%m-%d')

        if start_time > end_time:
            QMessageBox.warning(self, '警告', '结束日期不能早于开始日期！')
            return
        now_time = datetime.now()
        if start_time < now_time:
            QMessageBox.warning(self, '警告', '请假开始日期不能早于当前日期！')
            return
        # 判断该员工是否已经请假
        sql = "SELECT * FROM attendance WHERE work_id = '{}' AND state = 2 AND state = 3 AND time >= '{}' AND time <= " \
              "'{}'".format(int(work_id), start_time, end_time)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result:
            QMessageBox.warning(self, '警告', '该员工在该时间段已经请假！')
            return
        # 写入数据库
        sql2 = "INSERT INTO `leave` (work_id, types_of_leaves, leave_explanation, start_time, stop_time) VALUES ('{}', " \
               "'{}', '{}', '{}', '{}')".format(int(work_id), int(leave_con), opion, start_time, end_time)
        try:
            cursor.execute(sql2)

            # 计算日期差
            print('end_time', end_time)
            print('start_time', start_time)
            date_diff = end_time - start_time
            # 循环遍历日期范围
            for i in range(date_diff.days + 1):
                current_date = start_time + timedelta(days=i)
                time_day = current_date.strftime('%Y-%m-%d')
                print('time_day', time_day)
                if state == 0:
                    s = 3
                elif state == 1:
                    s = 2
                else:
                    QMessageBox.warning(self, '警告', '请选择请假类型！')
                    return
                sql_insert = "INSERT INTO `attendance` (work_id, state, time) VALUES ('{}', '{}', '{}')".format(
                    int(work_id), s, time_day)
                cursor.execute(sql_insert)
            db.commit()
            QMessageBox.information(self, '成功', '请假成功！')
        except BaseException as e:
            print('error', str(e))
            db.rollback()
        finally:
            cursor.close()
            db.close()

    def find_clicked(self):
        """
        考勤统计槽函数
        :return:
        """
        tiem = self.findlineEdit.text()  # 获取用户要查询的员工工号
        month_mapping = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12}
        mouth = month_mapping.get(self.comboBox_2.currentIndex(), None)
        if mouth is None:
            QMessageBox.warning(self, '警告', '请选择月份！')
            return
        print('查询员工号：', tiem)
        if not tiem:
            QMessageBox.warning(self, '警告', '请输入查询条件')
            return
        else:
            db, cursor = create_db()
            # sql_find = "SELECT * FROM check_in WHERE time = '{}'".format(tiem)
            sql_find = "SELECT w.name, w.department, a.state, a.card_time, a.time, l.leave_explanation FROM workers as w " \
                       "JOIN attendance as a ON w.work_id = a.work_id " \
                       "LEFT JOIN `leave` as l ON w.work_id = l.work_id WHERE w.work_id = '{}' AND MONTH(a.time) = '{}'".format(
                int(tiem), mouth)
            try:
                cursor.execute(sql_find)
                result = cursor.fetchall()
                print(result)
                if result:
                    # 创建模型
                    self.model_2 = QStandardItemModel(len(result), 6)  # 几行几列数据
                    self.model_2.setHorizontalHeaderLabels(['姓名', '部门', '状态', '出勤时间', '日期', '请假原因'])
                    # 填充数据
                    nomal_num = 0  # 正常出勤次数
                    leave_num = 0  # 请假次数
                    late_num = 0  # 迟到次数
                    for i in range(len(result)):
                        item1 = QStandardItem(str(result[i][0]))
                        item2 = QStandardItem(str(result[i][1]))
                        if result[i][2] == 0:
                            item3 = QStandardItem('缺勤')
                        elif result[i][2] == 1:
                            item3 = QStandardItem('正常出勤')
                            nomal_num += 1
                        elif result[i][2] == 2:
                            item3 = QStandardItem('病假')
                            leave_num += 1
                        elif result[i][2] == 3:
                            item3 = QStandardItem('事假')
                            leave_num += 1
                        elif result[i][2] == 4:
                            item3 = QStandardItem('迟到')
                            late_num += 1
                        if result[i][3] is None:
                            item4 = QStandardItem('无')
                        else:
                            item4 = QStandardItem(str(result[i][3]))
                        item5 = QStandardItem(str(result[i][4]))
                        item6 = QStandardItem(str(result[i][5]))
                        self.model_2.setItem(i, 0, item1)
                        self.model_2.setItem(i, 1, item2)
                        self.model_2.setItem(i, 2, item3)
                        self.model_2.setItem(i, 3, item4)
                        self.model_2.setItem(i, 4, item5)
                        if result[i][2] == 2 or result[i][2] == 3:
                            self.model_2.setItem(i, 5, item6)
                        else:
                            self.model_2.setItem(i, 5, QStandardItem('无'))
                    # 将模型应用到表格视图中
                    self.tableView_2.setModel(self.model_2)
                    # self.tableView_2设置为只读模式
                    self.tableView_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
                    # 调整列宽以适应内容
                    # 内容全部显示
                    self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                    # 内容自适应
                    self.tableView_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.onelineEdit_2.setText(str(nomal_num))
                    self.twoonelineEdit_3.setText(str(leave_num))
                    self.twoonelineEdit_4.setText(str(late_num))

                else:
                    QMessageBox.warning(self, '警告', '无数据')
            except Exception as e:
                print(e)
                QMessageBox.warning(self, '警告', '查询失败')
            finally:
                cursor.close()
                db.close()
                return

    def del_clicked(self):
        """
        员工考勤查询
        :return:
        """
        # 获取选中的行索引
        tiem = self.account  # 获取用户要查询的员工工号
        print('查询员工号：', tiem)
        if tiem is None:
            QMessageBox.warning(self, '警告', '请输入查询条件')
            return
        else:
            db, cursor = create_db()
            sql_find = "SELECT w.name, w.department, a.state, a.card_time, a.time, l.leave_explanation FROM workers as w " \
                       "JOIN attendance as a ON w.work_id = a.work_id " \
                       "LEFT JOIN `leave` as l ON w.work_id = l.work_id WHERE w.work_id = '{}'".format(int(tiem))
            try:
                cursor.execute(sql_find)
                result = cursor.fetchall()
                print(result)
                if result:
                    # 创建模型
                    self.model = QStandardItemModel(len(result), 6)  # 几行几列数据
                    self.model.setHorizontalHeaderLabels(['姓名', '部门', '状态', '出勤时间', '日期', '请假原因'])
                    # 填充数据
                    nomal_num = 0  # 正常出勤次数
                    leave_num = 0  # 请假次数
                    late_num = 0  # 迟到次数
                    for i in range(len(result)):
                        item1 = QStandardItem(str(result[i][0]))
                        item2 = QStandardItem(str(result[i][1]))
                        if result[i][2] == 0:
                            item3 = QStandardItem('缺勤')
                        elif result[i][2] == 1:
                            item3 = QStandardItem('正常出勤')
                            nomal_num += 1
                        elif result[i][2] == 2:
                            item3 = QStandardItem('病假')
                            leave_num += 1
                        elif result[i][2] == 3:
                            item3 = QStandardItem('事假')
                            leave_num += 1
                        elif result[i][2] == 4:
                            item3 = QStandardItem('迟到')
                            late_num += 1
                        if result[i][3] is None:
                            item4 = QStandardItem('无')
                        else:
                            item4 = QStandardItem(str(result[i][3]))
                        item5 = QStandardItem(str(result[i][4]))
                        item6 = QStandardItem(str(result[i][5]))
                        self.model.setItem(i, 0, item1)
                        self.model.setItem(i, 1, item2)
                        self.model.setItem(i, 2, item3)
                        self.model.setItem(i, 3, item4)
                        self.model.setItem(i, 4, item5)
                        if result[i][2] == 2 or result[i][2] == 3:
                            self.model.setItem(i, 5, item6)
                        else:
                            self.model.setItem(i, 5, QStandardItem('无'))
                    # 将模型应用到表格视图中
                    self.tableView.setModel(self.model)
                    # 调整列宽以适应内容
                    self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                    self.onelineEdit.setText(str(nomal_num))
                    self.twoonelineEdit.setText(str(leave_num))
                    self.twoonelineEdit_2.setText(str(late_num))
                else:
                    QMessageBox.warning(self, '警告', '无数据')
            except Exception as e:
                print(e)
                QMessageBox.warning(self, '警告', '查询失败')
            finally:
                cursor.close()
                db.close()
                return

    # def init_userdata(self):
    #     db, cursor = create_db()
    #     sql = "SELECT * FROM users"
    #     cursor.execute(sql)
    #     row = cursor.fetchall()
    #
    #     if row:
    #         print(row)
    #         # 创建模型
    #         self.model = QStandardItemModel(len(row), 2)  # 几行几列数据
    #         self.model.setHorizontalHeaderLabels(['用户姓名', '用户编号'])
    #         # 填充数据
    #         for i in range(len(row)):
    #             item1 = QStandardItem(row[i][0])
    #             item2 = QStandardItem(str(row[i][1]))
    #             self.model.setItem(i, 0, item1)
    #             self.model.setItem(i, 1, item2)
    #
    #         # 将模型应用到表格视图中
    #         self.tableView.setModel(self.model)
    #         # 调整列宽以适应内容
    #         self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    #     else:
    #         print('无该用户信息')
    #         QMessageBox.warning(self, '登录失败', '无该用户信息！')

    def on_tab_changed(self, index):
        current_tab = self.tabWidget.widget(index)
        self.tabWidget.currentChanged.disconnect(self.on_tab_changed)
        print("Current Index:", index)

        if current_tab == self.tab:
            print("Switched to Tab 1")
            self.tabWidget.currentChanged.connect(self.on_tab_changed)
            return
        elif current_tab == self.tab_2:
            print("Switched to Tab 1")
            self.tabWidget.setCurrentIndex(1)
            self.tabWidget.currentChanged.connect(self.on_tab_changed)
            return
        elif current_tab == self.tab_3:
            # if not self.login_flag:
            #     QMessageBox.warning(self, '权限警告', '您没有登录')
            #     print("Setting Index to 0")
            #     self.tabWidget.setCurrentIndex(0)
            #     self.tabWidget.currentChanged.connect(self.on_tab_changed)
            #     return
            # else:
            print("Setting Index to 2")
            self.tabWidget.setCurrentIndex(2)
            self.tabWidget.currentChanged.connect(self.on_tab_changed)
            return
        elif current_tab == self.tab_4:
            if not self.login_flag:
                QMessageBox.warning(self, '权限警告', '您没有登录或者没有权限')
                print("Setting Index to 0")
                self.tabWidget.setCurrentIndex(0)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return
            else:
                print("Setting Index to 2")
                self.tabWidget.setCurrentIndex(3)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return
        elif current_tab == self.tab_5:
            if not self.login_flag:
                QMessageBox.warning(self, '权限警告', '您没有登录或者没有权限')
                print("Setting Index to 0")
                self.tabWidget.setCurrentIndex(0)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return
            else:
                print("Setting Index to 2")
                self.tabWidget.setCurrentIndex(4)
                self.tabWidget.currentChanged.connect(self.on_tab_changed)
                return

    def enroll_clicked(self):
        """
        管理员注册槽函数
        :return:
        """
        user_id = self.newidlineEdit.text()
        user_pwd = self.newidlineEdit.text()
        yzm = self.yzmlineEdit.text()
        print(yzm)
        if not user_id or not user_pwd or not yzm:
            QMessageBox.warning(self, '警告', '请填写完整信息')
            return
        else:
            if yzm != '211166':
                QMessageBox.warning(self, '警告', '验证码错误')
                return
            db, cour = create_db()
            sql_find = "SELECT * FROM manager WHERE user_id = '%s' LIMIT 1" % user_id
            try:
                cour.execute(sql_find)
                result = cour.fetchone()
                if result:
                    QMessageBox.warning(self, '警告', '该用户已存在')
                    return
                else:
                    sql_insert = "INSERT INTO manager (user_id, user_pwd) VALUES ('%s', '%s')" % (user_id, user_pwd)
                    cour.execute(sql_insert)
                    db.commit()
                    QMessageBox.information(self, '提示', '注册成功')
                    self.newidlineEdit.clear()
                    self.yzmlineEdit.clear()
                    self.newpwdlineEdit.clear()
            except Exception as e:
                print(e)
                db.rollback()
                QMessageBox.warning(self, '警告', '注册失败')
            finally:
                cour.close()
                db.close()

    def login_clicked(self):
        """
        管理员或职工登录槽函数
        :return:
        """
        user_id = self.idlineEdit.text()
        user_pwd = self.pwdlineEdit.text()
        # 获取用户选择的登录身份radioButton
        if self.radioButton.isChecked():
            user_type = '员工'    # 员工
            self.account = user_id  # 保存登录账号
        elif self.radioButton_2.isChecked():
            user_type = '管理员'    # 管理员
        else:
            QMessageBox.warning(self, '警告', '请选择登录身份！')
            return
        if not user_id or not user_pwd:
            QMessageBox.warning(self, '警告', '请填写完整信息')
            return
        else:
            db, cour = create_db()
            sql_find = "SELECT * FROM manager WHERE user_id = '%s' AND user_pwd = '%s' LIMIT 1" % (user_id, user_pwd)
            try:
                cour.execute(sql_find)

                result = cour.fetchone()
                if result:
                    if user_type == '管理员':
                        self.login_flag = True
                    QMessageBox.information(self, '提示', '登录成功')
                    self.tabWidget.setCurrentIndex(2)
                    self.tabWidget.currentChanged.connect(self.on_tab_changed)
                    self.idlineEdit.clear()
                    self.pwdlineEdit.clear()
                else:
                    QMessageBox.warning(self, '警告', '用户名或密码错误')
            except Exception as e:
                print(e)
                QMessageBox.warning(self, '警告', '登录失败')
            finally:
                db.close()
                return
