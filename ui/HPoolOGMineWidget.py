# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\peng\Desktop\chia-tools\ui\HPoolOGMineWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HPoolOGMineWidget(object):
    def setupUi(self, HPoolOGMineWidget):
        HPoolOGMineWidget.setObjectName("HPoolOGMineWidget")
        HPoolOGMineWidget.resize(989, 522)
        self.verticalLayout = QtWidgets.QVBoxLayout(HPoolOGMineWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(HPoolOGMineWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.editMinerName = QtWidgets.QLineEdit(HPoolOGMineWidget)
        self.editMinerName.setObjectName("editMinerName")
        self.horizontalLayout_3.addWidget(self.editMinerName)
        self.label = QtWidgets.QLabel(HPoolOGMineWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.editApiKey = QtWidgets.QLineEdit(HPoolOGMineWidget)
        self.editApiKey.setObjectName("editApiKey")
        self.horizontalLayout_3.addWidget(self.editApiKey)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.labelStatus = QtWidgets.QLabel(HPoolOGMineWidget)
        self.labelStatus.setText("")
        self.labelStatus.setObjectName("labelStatus")
        self.horizontalLayout_3.addWidget(self.labelStatus)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.buttonStart = QtWidgets.QPushButton(HPoolOGMineWidget)
        self.buttonStart.setObjectName("buttonStart")
        self.horizontalLayout_3.addWidget(self.buttonStart)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.textEditLog = QtWidgets.QTextEdit(HPoolOGMineWidget)
        self.textEditLog.setObjectName("textEditLog")
        self.verticalLayout.addWidget(self.textEditLog)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxAutoStart = QtWidgets.QCheckBox(HPoolOGMineWidget)
        self.checkBoxAutoStart.setObjectName("checkBoxAutoStart")
        self.horizontalLayout.addWidget(self.checkBoxAutoStart)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(HPoolOGMineWidget)
        QtCore.QMetaObject.connectSlotsByName(HPoolOGMineWidget)

    def retranslateUi(self, HPoolOGMineWidget):
        _translate = QtCore.QCoreApplication.translate
        HPoolOGMineWidget.setWindowTitle(_translate("HPoolOGMineWidget", "Form"))
        self.label_2.setText(_translate("HPoolOGMineWidget", "矿机名称"))
        self.label.setText(_translate("HPoolOGMineWidget", "API Key"))
        self.buttonStart.setText(_translate("HPoolOGMineWidget", "开始挖矿"))
        self.checkBoxAutoStart.setText(_translate("HPoolOGMineWidget", "开机自动启动并开始HPoolOG挖矿"))
