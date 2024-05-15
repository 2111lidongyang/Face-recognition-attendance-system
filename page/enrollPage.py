from datetime import datetime
import os
import cv2
import face_recognition
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from pypinyin import lazy_pinyin

from sql.tools import create_db
from ui.enroll_page import Ui_Form

"""
该页面用于录入员工信息，包括姓名、性别、年龄、手机号、部门、工号、照片等信息。
"""


class EnrollPage(QWidget, Ui_Form):
    def __init__(self, mainpage):
        super(EnrollPage, self).__init__()
        self.setupUi(self)
        self.mainpage = mainpage  # 传入主页面对象
        self.cap = cv2.VideoCapture(0)  # 打开摄像头
        self.cap_flag = 0  # 定义一个标志位
        self.timer = QTimer(self)
        self.flag = False
        self.frame = None  # 定义一个变量，用于存放摄像头画面
        # 定义一个定时器，每隔30毫秒更新一次label中的画面
        self.init_slot()  # 初始化槽函数

    def init_slot(self):
        self.capBtn.clicked.connect(self.capture_face)  # 连接槽函数
        self.timer.timeout.connect(self.update_label)  # 连接槽函数
        self.backBtn.clicked.connect(self.backclose)  # 连接槽函数
        self.enrollBtn.clicked.connect(self.enroll_face)  # 连接槽函数
        self.fileBtn.clicked.connect(self.open_file)  # 连接打开本地文件夹槽函数

    def open_file(self):
        """
        选择上传本地人脸图片进行注册
        :return:
        """
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "选择图片", "",
                                                  "Images (*.png *.xpm *.jpg)", options=options)
        if fileName:
            img = cv2.imread(fileName)
            cv2.imwrite("temp.png", img)  #
            self.flag = True
            # 将图片显示到label_7中
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            qImg = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.label_7.setPixmap(QPixmap.fromImage(qImg))

    def enroll_face(self):
        """
        用户注册
        :return:
        """
        if self.flag:
            work_id = self.work_id_lineEdit.text()
            name = self.name_lineEdit.text()
            gender = self.gender_lineEdit.text()
            work_age = self.work_age_lineEdit.text()
            phone = self.phone_lineEdit.text()
            department = self.department_lineEdit.text()
            user_pwd = self.pwd_lineEdit.text()  # 获取用户输入的密码

            # 检查字段是否为空
            if not all([work_id, name, gender, work_age, phone, department, user_pwd]):
                QMessageBox.warning(self, "警告", "请填写完整信息！")
                return

                # 转换为拼音
            name_pinyin = "".join(lazy_pinyin(name))
            print('name:', name_pinyin)  # 这里打印的是拼音，如果后续还要用原名，则不需要转换

            # 判断该name或work_id是否已经存在
            db, cursor = create_db()  # 假设create_db函数返回数据库连接和游标
            cursor.execute(
                "SELECT * FROM workers WHERE name='{}' OR work_id={} LIMIT 1".format(name_pinyin, int(work_id)))
            result = cursor.fetchone()
            print('result:', result)
            if result:
                QMessageBox.warning(self, "警告", "该员工已存在！")
                cursor.close()
                db.close()
                return

                # 保存图片，注意这里"temp.png"需要是有效的图片路径
            # 如果"temp.png"不是当前工作目录下的图片，则需要提供正确的路径
            path = "face_image"  # 模型数据图片目录
            if not os.path.exists(path):
                os.makedirs(path)  # 如果目录不存在则创建
            img_path = os.path.join(path, name_pinyin + ".png")  # 直接使用原名，而不是拼音
            cv2.imwrite(img_path, cv2.imread("temp.png"))  # 假设"temp.png"是当前有效的图片
            print(img_path)

            # 插入数据到数据库
            try:
                cursor.execute("INSERT INTO workers (work_id, name, gender, work_age, phone, department, image_url) "
                               "VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format
                               (int(work_id), name_pinyin, gender, int(work_age), phone, department, img_path))
                db.commit()

                # 清除输入框
                self.name_lineEdit.clear()
                self.gender_lineEdit.clear()
                self.work_age_lineEdit.clear()
                self.phone_lineEdit.clear()
                self.department_lineEdit.clear()
                self.pwd_lineEdit.clear()
                self.work_id_lineEdit.clear()
                now = datetime.now()
                # 格式化为指定的字符串格式
                today = now.strftime("%Y-%m-%d")
                sql2 = "INSERT INTO attendance (work_id, time,state) VALUES ('{}', '{}', 0)".format(int(work_id), today)
                cursor.execute(sql2)
                sql_enroll = "INSERT INTO manager (user_id, user_pwd) VALUES ('{}', '{}')".format(str(work_id), str(user_pwd))   # 员工注册
                cursor.execute(sql_enroll)
                db.commit()
                # 关闭数据库连接
                cursor.close()
                db.close()
                QMessageBox.information(self, "提示", "录入成功！")
            except Exception as e:
                print(e)
                QMessageBox.warning(self, "警告", "录入失败！")
                cursor.close()
                db.close()
                return

            # 关闭数据库连接
            # except Exception as e:
            #     print(e)
            #     QMessageBox.warning(self, "警告", "录入失败！")



        else:
            QMessageBox.warning(self, "警告", "请先拍照！")
            return

    def backclose(self):
        """
        返回主界面
        :return:
        """
        if self.cap_flag == 1:
            self.timer.stop()  # 关闭定时器
            self.cap.release()  # 释放摄像头
        self.close()
        self.mainpage.cap = cv2.VideoCapture(0)
        self.mainpage.init_face()  # 重新初始化人脸识别
        self.mainpage.timer.start(30)
        self.mainpage.show()

    def capture_face(self):
        """
        打开摄像头并捕捉人脸
        :return:
        """
        if self.cap_flag == 0:
            self.cap_flag = 1
            self.timer.start(30)
            self.capBtn.setText("拍取人脸照片")
        elif self.cap_flag == 1:
            self.cap_flag = 2
            image = self.frame
            cv2.imwrite("temp.png", image)  # 保存图片到本地
            QMessageBox.information(self, "提示", "拍照成功")
            self.flag = True
            self.capBtn.setText("关闭摄像头")
        elif self.cap_flag == 2:
            self.cap_flag = 0
            self.timer.stop()
            self.flag = False
            self.capBtn.setText("开启摄像头")

    def update_label(self):
        """
        更新label中的画面
        :return:
        """
        ret, self.frame = self.cap.read()  # 读取摄像头画面
        if ret:
            # 将图片显示到label中
            img = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            qImg = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.label_7.setPixmap(QPixmap.fromImage(qImg))   # 显示图片到label中
