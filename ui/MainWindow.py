# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\peng\Desktop\chia-tools\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 633)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tabFolders = QtWidgets.QWidget()
        self.tabFolders.setObjectName("tabFolders")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabFolders)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabFoldersWidget = FoldersWidget(self.tabFolders)
        self.tabFoldersWidget.setObjectName("tabFoldersWidget")
        self.verticalLayout_2.addWidget(self.tabFoldersWidget)
        self.tabWidget.addTab(self.tabFolders, "")
        self.tabPlot = QtWidgets.QWidget()
        self.tabPlot.setObjectName("tabPlot")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabPlot)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabPlotWidget = PlotWidget(self.tabPlot)
        self.tabPlotWidget.setObjectName("tabPlotWidget")
        self.verticalLayout_5.addWidget(self.tabPlotWidget)
        self.tabWidget.addTab(self.tabPlot, "")
        self.tabHPoolOGMine = QtWidgets.QWidget()
        self.tabHPoolOGMine.setObjectName("tabHPoolOGMine")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabHPoolOGMine)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabHPoolOGMineWidget = HPoolOGMineWidget(self.tabHPoolOGMine)
        self.tabHPoolOGMineWidget.setObjectName("tabHPoolOGMineWidget")
        self.verticalLayout_6.addWidget(self.tabHPoolOGMineWidget)
        self.tabWidget.addTab(self.tabHPoolOGMine, "")
        self.tabHPoolPPMine = QtWidgets.QWidget()
        self.tabHPoolPPMine.setObjectName("tabHPoolPPMine")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabHPoolPPMine)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tabHPoolPPMineWidget = HPoolPPMineWidget(self.tabHPoolPPMine)
        self.tabHPoolPPMineWidget.setObjectName("tabHPoolPPMineWidget")
        self.verticalLayout_7.addWidget(self.tabHPoolPPMineWidget)
        self.tabWidget.addTab(self.tabHPoolPPMine, "")
        self.tabHuobiPoolMine = QtWidgets.QWidget()
        self.tabHuobiPoolMine.setObjectName("tabHuobiPoolMine")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabHuobiPoolMine)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabHuobiPoolMineWidget = HuobiPoolMineWidget(self.tabHuobiPoolMine)
        self.tabHuobiPoolMineWidget.setObjectName("tabHuobiPoolMineWidget")
        self.verticalLayout_3.addWidget(self.tabHuobiPoolMineWidget)
        self.tabWidget.addTab(self.tabHuobiPoolMine, "")
        self.tabPlotCheck = QtWidgets.QWidget()
        self.tabPlotCheck.setObjectName("tabPlotCheck")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabPlotCheck)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabPlotCheckWidget = PlotCheckWidget(self.tabPlotCheck)
        self.tabPlotCheckWidget.setObjectName("tabPlotCheckWidget")
        self.verticalLayout_8.addWidget(self.tabPlotCheckWidget)
        self.tabWidget.addTab(self.tabPlotCheck, "")
        self.tabAbout = QtWidgets.QWidget()
        self.tabAbout.setObjectName("tabAbout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabAbout)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabAboutWidget = AboutWidget(self.tabAbout)
        self.tabAboutWidget.setObjectName("tabAboutWidget")
        self.verticalLayout_4.addWidget(self.tabAboutWidget)
        self.tabWidget.addTab(self.tabAbout, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ChiaTools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFolders), _translate("MainWindow", "硬盘"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlot), _translate("MainWindow", "P图任务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHPoolOGMine), _translate("MainWindow", "HPoolOG老矿池挖矿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHPoolPPMine), _translate("MainWindow", "HPoolPP新矿池挖矿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabHuobiPoolMine), _translate("MainWindow", "火币矿池挖矿"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPlotCheck), _translate("MainWindow", "Plot检查"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAbout), _translate("MainWindow", "关于"))
from widgets.AboutWidget import AboutWidget
from widgets.FoldersWidget import FoldersWidget
from widgets.HPoolOGMineWidget import HPoolOGMineWidget
from widgets.HPoolPPMineWidget import HPoolPPMineWidget
from widgets.HuobiPoolMineWidget import HuobiPoolMineWidget
from widgets.PlotCheckWidget import PlotCheckWidget
from widgets.PlotWidget import PlotWidget
