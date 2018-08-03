# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tech_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

import vkapi
import utils
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(341, 171)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Техническая информация"))
        # self.label.setOpenExternalLinks(True)
        self.label.setText(_translate("Form", "Внутренний IP: " + str(utils.internal_ip())))
        self.label_2.setText(_translate("Form", "Внешний IP: " + str(utils.external_ip())))
        
        if utils.check_connection(vkapi.HOST_API):
            self.label_3.setText(_translate("Form",
             "Хост: [" + vkapi.HOST_API + "] - Доступен"))
        else:
            self.label_3.setText(_translate("Form",
             "Хост: [" + vkapi.HOST_API + "] - Недоступен"))

        if utils.check_connection(vkapi.OAUTH):
            self.label_4.setText(_translate("Form",
             "Хост: [" + vkapi.OAUTH + "] - Доступен"))
        else:
            self.label_4.setText(_translate("Form",
             "Хост: [" + vkapi.OAUTH + "] - Недоступен"))
            
        self.pushButton_3.setText(_translate("Form", "OK"))

