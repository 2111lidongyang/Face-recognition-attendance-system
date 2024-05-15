import os
from datetime import datetime
from threading import Thread
import cv2
import face_recognition
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QMessageBox
from page.enrollPage import EnrollPage
from page.managerPage import ManagerPage
from sql.tools import create_db
from ui.home_page import Ui_Form

"""
主页逻辑代码
"""


class HomePage(QWidget, Ui_Form):
    def __init__(self):
        super(HomePage, self).__init__()
        self.setupUi(self)
        self.init_slot()  # 初始化槽函数
        # 定义一个定时器，每隔30毫秒更新一次label中的画面
        self.name = "Unknown"  # 定义一个变量，用于保存当前检测到的人脸的名字
        # 格式化为指定的字符串格式
        from datetime import time

        # 创建一个time对象，表示上午9:00
        self.time_flag = time(9, 0)
        self.time_flag_str = self.time_flag.strftime("%H:%M:%S")
        self.frames = None
        self.cap = cv2.VideoCapture(0)  # 打开摄像头
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)  # 连接槽函数，每隔30毫秒调用一次槽函数，更新label中的画面
        self.timer.start(30)  # 启动定时器，每隔30毫秒调用一次槽函数

    def init_slot(self):
        """
        初始化槽函数
        :return:
        """
        Thread(target=self.init_time).start()  # 启动线程，初始化签到记录
        self.init_face()  # 初始化人脸识别模型
        self.cardBtn.clicked.connect(self.card_slot)  # 连接签到按钮槽函数
        self.enrollBtn.clicked.connect(self.enroll_slot)  # 连接用户注册按钮槽函数
        self.userManagerBtn.clicked.connect(self.user_manager_slot)  # 打开用户管理界面槽函数

    def user_manager_slot(self):
        self.user_manager = ManagerPage()   # 实例化用户管理界面
        self.user_manager.show()  # 显示用户管理界面
        self.user_manager.tabWidget.setCurrentIndex(0)  # 默认设置为普通用户的界面
        self.timer.stop()  # 停止定时器
        self.cap.release()  # 释放摄像头
        self.close()  # 关闭主界面

    def init_time(self):
        """
        每日更新一下签到记录
        :return: 无
        """
        db, cour = create_db()  # 连接数据库
        now = datetime.now()  # 获取当前时间
        today = now.strftime("%Y-%m-%d")
        sql = "SELECT work_id FROM workers"
        try:
            cour.execute(sql)
            results = cour.fetchall()
            if results is not None:
                for row in results:
                    user_id = row[0]
                    try:
                        #  查询这个人今天有没有数据初始化
                        sql_find = "SELECT * FROM attendance WHERE work_id = '{}' AND time = '{}' LIMIT 1".format(
                            user_id,
                            today)
                        cour.execute(sql_find)
                        res = cour.fetchone()
                        print('res', res)
                        if res is None:  # 如果这个人今天还没有数据
                            sql2 = "INSERT INTO attendance (work_id, time, state) VALUES ('{}', '{}', '{}')".format(
                                user_id, today, 0)
                            cour.execute(sql2)
                            db.commit()
                        else:
                            print('数据初始化过了')
                            continue
                    except Exception as e:
                        print(e)

                        continue
                print('数据初始化完成！')
            else:
                return
        except Exception as e:
            print(e)
            return

    def init_face(self):
        """
        初始化人脸识别模型
        :return:
        """
        path = "face_image"  # 模型数据图片目录
        self.total_image_name = []
        self.total_face_encoding = []

        for fn in os.listdir(path):  # fn 表示的是文件名q
            print(path + "/" + fn)
            try:
                self.total_face_encoding.append(
                    face_recognition.face_encodings(
                        face_recognition.load_image_file(path + "/" + fn))[0])
                fn = fn[:(len(fn) - 4)]  # 截取图片名（这里应该把images文件中的图片名命名为为人物名）
                self.total_image_name.append(fn)  # 图片名字列表
            except Exception as e:
                continue

    def update_label(self):
        """
        更新label中的画面
        :return:
        """
        ret, frame = self.cap.read()
        # 复制frame到self.frames中，用于显示当前帧
        self.frames = frame.copy()  # 保存当前帧
        if not ret:  # 如果读取失败，则退出循环
            return
        # 发现在视频帧所有的脸和face_enqcodings
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        # 在这个视频帧中循环遍历每个人脸
        for (top, right, bottom, left), face_encoding in zip(
                face_locations, face_encodings):
            # 看看面部是否与已知人脸相匹配。
            for i, v in enumerate(self.total_face_encoding):
                match = face_recognition.compare_faces(
                    [v], face_encoding, tolerance=0.5)
                self.name = "Unknown"
                if match[0]:
                    self.name = self.total_image_name[i]
                    break
            # 画出一个框，框住脸
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            # 画出一个带名字的标签，放在框下
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255),
                          cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, self.name, (left + 6, bottom - 6), font, 1.0,
                        (255, 255, 255), 1)
            # 将frame显示在label中
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width
            qImg = QImage(frame.data, width, height, bytesPerLine, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(qImg))

    def card_slot(self):
        """
        签到槽函数,员工人脸签到
        :return:
        """
        # 开始读取图片
        db, cour = create_db()
        if self.name == "Unknown":
            QMessageBox.warning(self, "Warning", "Unknown face, please try again.")
            return
        sql = "SELECT * FROM workers WHERE name = '%s' LIMIT 1" % str(self.name)
        try:
            cour.execute(sql)
            result = cour.fetchone()
            if result is None:
                QMessageBox.warning(self, "Warning", "该用户不存在，请先注册！")
                return
            else:
                # 开始打卡记录插入数据库
                # 获取今天的日期和时间
                now = datetime.now()
                # 格式化为指定的字符串格式
                today = now.strftime("%Y-%m-%d")
                # 获取用户id
                work_id = result[0]  # 用户工号
                print('work_id:', work_id)
                # 看看今天这个人有没有打卡
                sql_find = "SELECT * FROM attendance WHERE work_id = '{}' AND time = '{}' AND state = 0 LIMIT 1".format(
                    work_id, today)
                cour.execute(sql_find)
                result = cour.fetchone()
                print('result:', result)
                if result:  # 如果用户今天还没有打卡记录
                    # 开始打卡记录插入数据库
                    # 判断打卡的状态
                    state = 0  # 默认为未签到
                    if now.time() < self.time_flag:  # 如果现在时间小于签到时间
                        # 正常签到
                        state = 1
                        QMessageBox.information(self, "Information", "{}，打卡成功！".format(self.name))
                    else:  # 如果现在时间大于签到时间
                        # 迟到
                        state = 4
                        QMessageBox.warning(self, "Warning", "您已迟到，请早点打卡！")
                    sql2 = "UPDATE attendance SET state = '{}', card_time = NOW() WHERE work_id = '{}' AND time = '{}'".format(
                        int(state), work_id, today)
                    cour.execute(sql2)
                    db.commit()
                    cour.close()
                    db.close()
                    return
                else:  # 如果用户今天已经打过卡了
                    QMessageBox.warning(self, "Warning", "你今天已经打过卡了，或者你今天已经请假了")
                    return

        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Warning", "No card found, please register.")
            return

    def enroll_slot(self):
        """
        # 用户注册槽函数
        :return:
        """
        self.timer.stop()  # 停止定时器
        self.label.clear()  # 清空label
        self.cap.release()
        self.enroll_page = EnrollPage(self)
        self.enroll_page.show()
        self.hide()

        # if self.namelineEdit.text() == "":
        #     QMessageBox.warning(self, "Warning", "Please input your name.")
        #     return
        # name = self.namelineEdit.text()
        # # 将用户输入的中文名字转换为拼音
        # from pypinyin import lazy_pinyin
        # name = "".join(lazy_pinyin(name))
        # print('name:', name)
        # # 去数据库中查询该用户是否存在
        # db, cour = create_db()
        # sql = "SELECT * FROM users WHERE user_name = '%s' LIMIT 1" % str(name)
        # try:
        #     cour.execute(sql)
        #     result = cour.fetchone()
        #     if result:
        #         QMessageBox.warning(self, "Warning", "User already exists, please try again.")
        #         return
        #     else:
        #         # 开始用户注册
        #         # 保存人脸数据
        #         if self.name == "Unknown":
        #             # 开始人脸录入
        #             path = "face_image"  # 模型数据图片目录
        #             # 保存图片
        #             cv2.imwrite(path + "/" + name + ".png", self.frames)
        #
        #             # 用户数据保存到数据库
        #             # 随机生成一个用户id
        #             import random
        #             user_id = random.randint(1, 999999)
        #             sql1 = "INSERT INTO users (user_name, user_id) VALUES ('%s', '%s')" % (name, user_id)
        #             cour.execute(sql1)
        #             now = datetime.now()
        #             # 格式化为指定的字符串格式
        #             today = now.strftime("%Y-%m-%d")
        #             sql2 = "INSERT INTO check_in (user_id, time, is_card) VALUES ('{}', '{}', '{}')".format(user_id,
        #                                                                                                     today, 0)
        #             cour.execute(sql2)
        #             db.commit()
        #             cour.close()
        #             db.close()
        #             QMessageBox.information(self, "Information", "{}，注册成功！".format(name))
        #             # 开始人脸编码
        #             image = path + "/" + name + ".png"
        #             print(image)
        #             face_encoding = face_recognition.face_encodings(
        #                 face_recognition.load_image_file(image))[0]
        #             # 保存人脸编码
        #             self.total_face_encoding.append(face_encoding)
        #             self.total_image_name.append(name)
        #             return
        #         else:
        #             QMessageBox.warning(self, "Warning", "你已经注册过了，请不要重复注册！")
        #             return
        # except Exception as e:
        #     print(e)
        #     QMessageBox.warning(self, "Warning", "您已经注册过了，请不要重复注册！")
        #     return
