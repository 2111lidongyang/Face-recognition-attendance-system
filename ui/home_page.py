# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(908, 591)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet(".QFrame#frame{border-image: url(:/img/home.png);}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 70, 480, 480))
        self.label.setStyleSheet(".QLabel{\n"
"border: 2px solid #4973f6;\n"
"border-radius:10px;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.cardBtn = QtWidgets.QPushButton(self.frame)
        self.cardBtn.setGeometry(QtCore.QRect(522, 327, 151, 51))
        self.cardBtn.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.cardBtn.setText("")
        self.cardBtn.setObjectName("cardBtn")
        self.enrollBtn = QtWidgets.QPushButton(self.frame)
        self.enrollBtn.setGeometry(QtCore.QRect(710, 330, 151, 51))
        self.enrollBtn.setStyleSheet("font: 20 10pt \"阿里妈妈方圆体 VF Light\";\n"
"color:#000000;\n"
"border:none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.enrollBtn.setText("")
        self.enrollBtn.setObjectName("enrollBtn")
        self.userManagerBtn = QtWidgets.QPushButton(self.frame)
        self.userManagerBtn.setGeometry(QtCore.QRect(790, 10, 111, 51))
        self.userManagerBtn.setStyleSheet("font: 63 12pt \"阿里妈妈方圆体 VF SemiBold\";")
        self.userManagerBtn.setObjectName("userManagerBtn")
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userManagerBtn.setText(_translate("Form", "用户管理"))
import ui.image