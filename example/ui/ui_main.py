# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1086, 331)
        self.verticalLayout = QtWidgets.QVBoxLayout(Main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.methodComboBox = QtWidgets.QComboBox(Main)
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.horizontalLayout.addWidget(self.methodComboBox)
        self.urlEdit = QtWidgets.QLineEdit(Main)
        self.urlEdit.setObjectName("urlEdit")
        self.horizontalLayout.addWidget(self.urlEdit)
        self.sendBtn = QtWidgets.QPushButton(Main)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout.addWidget(self.sendBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(Main)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startBtn = QtWidgets.QPushButton(Main)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout_2.addWidget(self.startBtn)
        self.restartBtn = QtWidgets.QPushButton(Main)
        self.restartBtn.setObjectName("restartBtn")
        self.horizontalLayout_2.addWidget(self.restartBtn)
        self.pausedBtn = QtWidgets.QPushButton(Main)
        self.pausedBtn.setObjectName("pausedBtn")
        self.horizontalLayout_2.addWidget(self.pausedBtn)
        self.prevBtn = QtWidgets.QPushButton(Main)
        self.prevBtn.setObjectName("prevBtn")
        self.horizontalLayout_2.addWidget(self.prevBtn)
        self.nextBtn = QtWidgets.QPushButton(Main)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_2.addWidget(self.nextBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Form"))
        self.methodComboBox.setItemText(0, _translate("Main", "GET"))
        self.methodComboBox.setItemText(1, _translate("Main", "PUT"))
        self.methodComboBox.setItemText(2, _translate("Main", "POST"))
        self.methodComboBox.setItemText(3, _translate("Main", "DELETE"))
        self.sendBtn.setText(_translate("Main", "发送"))
        self.startBtn.setText(_translate("Main", "开始"))
        self.restartBtn.setText(_translate("Main", "重置"))
        self.pausedBtn.setText(_translate("Main", "暂停"))
        self.prevBtn.setText(_translate("Main", "上一页"))
        self.nextBtn.setText(_translate("Main", "下一页"))
