# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\peng\Desktop\chia-tools\ui\CreatePlotDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreatePlotDialog(object):
    def setupUi(self, CreatePlotDialog):
        CreatePlotDialog.setObjectName("CreatePlotDialog")
        CreatePlotDialog.resize(513, 458)
        self.verticalLayout = QtWidgets.QVBoxLayout(CreatePlotDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(CreatePlotDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.comboSSD = QtWidgets.QComboBox(CreatePlotDialog)
        self.comboSSD.setObjectName("comboSSD")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboSSD)
        self.label_5 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboHDD = QtWidgets.QComboBox(CreatePlotDialog)
        self.comboHDD.setObjectName("comboHDD")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboHDD)
        self.label_2 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.editFpk = QtWidgets.QTextEdit(CreatePlotDialog)
        self.editFpk.setObjectName("editFpk")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editFpk)
        self.label_3 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.editPpk = QtWidgets.QTextEdit(CreatePlotDialog)
        self.editPpk.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.editPpk.setObjectName("editPpk")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.editPpk)
        self.spinNumber = QtWidgets.QSpinBox(CreatePlotDialog)
        self.spinNumber.setEnabled(False)
        self.spinNumber.setMinimum(1)
        self.spinNumber.setMaximum(10000)
        self.spinNumber.setObjectName("spinNumber")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.spinNumber)
        self.label_7 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.timeEditDelay = QtWidgets.QTimeEdit(CreatePlotDialog)
        self.timeEditDelay.setObjectName("timeEditDelay")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.timeEditDelay)
        self.label_6 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.spinThreadNum = QtWidgets.QSpinBox(CreatePlotDialog)
        self.spinThreadNum.setMinimum(1)
        self.spinThreadNum.setProperty("value", 2)
        self.spinThreadNum.setObjectName("spinThreadNum")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.spinThreadNum)
        self.label_71 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_71.setObjectName("label_71")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_71)
        self.spinMemory = QtWidgets.QSpinBox(CreatePlotDialog)
        self.spinMemory.setMaximum(10000)
        self.spinMemory.setSingleStep(100)
        self.spinMemory.setProperty("value", 4608)
        self.spinMemory.setObjectName("spinMemory")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spinMemory)
        self.checkBoxSpecifyCount = QtWidgets.QCheckBox(CreatePlotDialog)
        self.checkBoxSpecifyCount.setObjectName("checkBoxSpecifyCount")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.checkBoxSpecifyCount)
        self.label_4 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.spinBucketNum = QtWidgets.QSpinBox(CreatePlotDialog)
        self.spinBucketNum.setMinimum(1)
        self.spinBucketNum.setMaximum(9999)
        self.spinBucketNum.setProperty("value", 128)
        self.spinBucketNum.setObjectName("spinBucketNum")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.spinBucketNum)
        self.label_8 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboK = QtWidgets.QComboBox(CreatePlotDialog)
        self.comboK.setObjectName("comboK")
        self.comboK.addItem("")
        self.comboK.addItem("")
        self.comboK.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboK)
        self.label_9 = QtWidgets.QLabel(CreatePlotDialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.checkBoxBitfield = QtWidgets.QCheckBox(CreatePlotDialog)
        self.checkBoxBitfield.setObjectName("checkBoxBitfield")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.checkBoxBitfield)
        self.verticalLayout.addLayout(self.formLayout)
        self.commandLinkButton = QtWidgets.QCommandLinkButton(CreatePlotDialog)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.verticalLayout.addWidget(self.commandLinkButton)
        self.buttonBox = QtWidgets.QDialogButtonBox(CreatePlotDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(CreatePlotDialog)
        self.buttonBox.accepted.connect(CreatePlotDialog.accept)
        self.buttonBox.rejected.connect(CreatePlotDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CreatePlotDialog)

    def retranslateUi(self, CreatePlotDialog):
        _translate = QtCore.QCoreApplication.translate
        CreatePlotDialog.setWindowTitle(_translate("CreatePlotDialog", "创建P图任务"))
        self.label.setText(_translate("CreatePlotDialog", "临时目录（固态硬盘）"))
        self.label_5.setText(_translate("CreatePlotDialog", "最终目录（机械硬盘）"))
        self.label_2.setText(_translate("CreatePlotDialog", "Farmer Public Key(fpk)"))
        self.label_3.setText(_translate("CreatePlotDialog", "Pool Public Key(ppk)"))
        self.label_7.setText(_translate("CreatePlotDialog", "延迟时间"))
        self.timeEditDelay.setDisplayFormat(_translate("CreatePlotDialog", "HH:mm:ss"))
        self.label_6.setText(_translate("CreatePlotDialog", "线程数"))
        self.label_71.setText(_translate("CreatePlotDialog", "最大内存"))
        self.spinMemory.setSuffix(_translate("CreatePlotDialog", "MiB"))
        self.checkBoxSpecifyCount.setText(_translate("CreatePlotDialog", "指定数量"))
        self.label_4.setText(_translate("CreatePlotDialog", "桶数(Buckets)"))
        self.label_8.setText(_translate("CreatePlotDialog", "Plot大小(K)"))
        self.comboK.setItemText(0, _translate("CreatePlotDialog", "32"))
        self.comboK.setItemText(1, _translate("CreatePlotDialog", "33"))
        self.comboK.setItemText(2, _translate("CreatePlotDialog", "34"))
        self.label_9.setText(_translate("CreatePlotDialog", "开启位域(bitfield)"))
        self.checkBoxBitfield.setText(_translate("CreatePlotDialog", "开启"))
        self.commandLinkButton.setText(_translate("CreatePlotDialog", "关于fpk和ppk"))
