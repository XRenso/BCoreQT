# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainLiagRB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1015, 600)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_Bar = QFrame(self.centralwidget)
        self.Left_Bar.setObjectName(u"Left_Bar")
        self.Left_Bar.setMinimumSize(QSize(0, 0))
        self.Left_Bar.setMaximumSize(QSize(40, 16777215))
        self.Left_Bar.setFrameShape(QFrame.NoFrame)
        self.Left_Bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Left_Bar)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.Left_Bar)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMaximumSize(QSize(40, 70))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame_menu.setFont(font)
        self.frame_menu.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_menu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 3, 41, 61))

        self.verticalLayout.addWidget(self.frame_menu)

        self.frame_left = QFrame(self.Left_Bar)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setMaximumSize(QSize(40, 500))
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_left)


        self.horizontalLayout.addWidget(self.Left_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.Content.setFrameShape(QFrame.StyledPanel)
        self.Content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.Content)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        self.frame_top_menu.setMaximumSize(QSize(16777215, 70))
        self.frame_top_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_top_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_top_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_pages)


        self.horizontalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
    # retranslateUi

