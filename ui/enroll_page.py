# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\enroll.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1011, 627)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backBtn = QtWidgets.QPushButton(self.frame_2)
        self.backBtn.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_2.addWidget(self.backBtn)
        spacerItem = QtWidgets.QSpacerItem(887, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_2.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_11 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.verticalLayout_3.addWidget(self.frame_11)
        self.frame_12 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.capBtn = QtWidgets.QPushButton(self.frame_12)
        self.capBtn.setObjectName("capBtn")
        self.horizontalLayout_12.addWidget(self.capBtn)
        self.fileBtn = QtWidgets.QPushButton(self.frame_12)
        self.fileBtn.setObjectName("fileBtn")
        self.horizontalLayout_12.addWidget(self.fileBtn)
        self.verticalLayout_3.addWidget(self.frame_12)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setStyleSheet("font: 63 10pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.work_id_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.work_id_lineEdit.setObjectName("work_id_lineEdit")
        self.horizontalLayout_4.addWidget(self.work_id_lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_13 = QtWidgets.QFrame(self.groupBox)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.frame_13)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.pwd_lineEdit = QtWidgets.QLineEdit(self.frame_13)
        self.pwd_lineEdit.setObjectName("pwd_lineEdit")
        self.horizontalLayout_13.addWidget(self.pwd_lineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout_2.addWidget(self.frame_13)
        self.frame_5 = QtWidgets.QFrame(self.groupBox)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.name_lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.horizontalLayout_5.addWidget(self.name_lineEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.label_3 = QtWidgets.QLabel(self.frame_6)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.gender_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.gender_lineEdit.setObjectName("gender_lineEdit")
        self.horizontalLayout_6.addWidget(self.gender_lineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.groupBox)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.work_age_lineEdit = QtWidgets.QLineEdit(self.frame_7)
        self.work_age_lineEdit.setObjectName("work_age_lineEdit")
        self.horizontalLayout_7.addWidget(self.work_age_lineEdit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.groupBox)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.phone_lineEdit = QtWidgets.QLineEdit(self.frame_8)
        self.phone_lineEdit.setObjectName("phone_lineEdit")
        self.horizontalLayout_8.addWidget(self.phone_lineEdit)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.groupBox)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem13)
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.department_lineEdit = QtWidgets.QLineEdit(self.frame_9)
        self.department_lineEdit.setObjectName("department_lineEdit")
        self.horizontalLayout_9.addWidget(self.department_lineEdit)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        self.verticalLayout_2.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.groupBox)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem15)
        self.enrollBtn = QtWidgets.QPushButton(self.frame_10)
        self.enrollBtn.setObjectName("enrollBtn")
        self.horizontalLayout_10.addWidget(self.enrollBtn)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem16)
        self.verticalLayout_2.addWidget(self.frame_10)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 9)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.backBtn.setText(_translate("Form", "返回首页"))
        self.groupBox_2.setTitle(_translate("Form", "人脸录入"))
        self.capBtn.setText(_translate("Form", "开启摄像头"))
        self.fileBtn.setText(_translate("Form", "选择本地图片"))
        self.groupBox.setTitle(_translate("Form", "请输入用户信息"))
        self.label.setText(_translate("Form", "工号："))
        self.label_8.setText(_translate("Form", "密码："))
        self.label_2.setText(_translate("Form", "姓名："))
        self.label_3.setText(_translate("Form", "性别："))
        self.label_4.setText(_translate("Form", "工龄："))
        self.label_5.setText(_translate("Form", "电话："))
        self.label_6.setText(_translate("Form", "部门："))
        self.enrollBtn.setText(_translate("Form", "注册"))