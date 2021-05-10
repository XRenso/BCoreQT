# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainAcXNse.ui'
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
        MainWindow.resize(1047, 573)
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
        self.frame_menu.setMinimumSize(QSize(40, 70))
        self.frame_menu.setMaximumSize(QSize(40, 70))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame_menu.setFont(font)
        self.frame_menu.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame_menu)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.menuButton)


        self.verticalLayout.addWidget(self.frame_menu, 0, Qt.AlignTop)

        self.frame = QFrame(self.Left_Bar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(40, 440))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.frame_left = QFrame(self.Left_Bar)
        self.frame_left.setObjectName(u"frame_left")
        self.frame_left.setMinimumSize(QSize(40, 50))
        self.frame_left.setMaximumSize(QSize(40, 50))
        self.frame_left.setFrameShape(QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QFrame.Raised)
        self.btn_info = QPushButton(self.frame_left)
        self.btn_info.setObjectName(u"btn_info")
        self.btn_info.setGeometry(QRect(0, 0, 40, 50))
        self.btn_info.setMinimumSize(QSize(40, 50))
        self.btn_info.setMaximumSize(QSize(40, 60))
        self.btn_info.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(85, 0, 255);\n"
"}")

        self.verticalLayout.addWidget(self.frame_left, 0, Qt.AlignBottom)


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
        self.frame_top_menu.setMinimumSize(QSize(0, 100))
        self.frame_top_menu.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_top_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top_menu)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Apps = QFrame(self.frame_top_menu)
        self.Apps.setObjectName(u"Apps")
        self.Apps.setFrameShape(QFrame.StyledPanel)
        self.Apps.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Apps)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.MainMenu_btn = QPushButton(self.Apps)
        self.MainMenu_btn.setObjectName(u"MainMenu_btn")
        self.MainMenu_btn.setMinimumSize(QSize(80, 80))
        self.MainMenu_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(185, 32, 185);\n"
"}")

        self.horizontalLayout_4.addWidget(self.MainMenu_btn)

        self.BCalc_btn = QPushButton(self.Apps)
        self.BCalc_btn.setObjectName(u"BCalc_btn")
        self.BCalc_btn.setMinimumSize(QSize(80, 80))
        self.BCalc_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(185, 32, 185);\n"
"}")

        self.horizontalLayout_4.addWidget(self.BCalc_btn)

        self.BMedia_btn = QPushButton(self.Apps)
        self.BMedia_btn.setObjectName(u"BMedia_btn")
        self.BMedia_btn.setMinimumSize(QSize(80, 80))
        self.BMedia_btn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(27, 27, 27);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color:rgb(185, 32, 185);\n"
"}")

        self.horizontalLayout_4.addWidget(self.BMedia_btn)


        self.horizontalLayout_3.addWidget(self.Apps, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_top_menu)

        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.Pages_Widget = QStackedWidget(self.frame_pages)
        self.Pages_Widget.setObjectName(u"Pages_Widget")
        self.page_Main = QWidget()
        self.page_Main.setObjectName(u"page_Main")
        self.gridLayout = QGridLayout(self.page_Main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logo = QLabel(self.page_Main)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 0))
        self.logo.setMaximumSize(QSize(550, 500))
        self.logo.setPixmap(QPixmap(u"gray_logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)

        self.Pages_Widget.addWidget(self.page_Main)
        self.page_BCalc = QWidget()
        self.page_BCalc.setObjectName(u"page_BCalc")
        self.Pages_Widget.addWidget(self.page_BCalc)
        self.page_BMedia = QWidget()
        self.page_BMedia.setObjectName(u"page_BMedia")
        self.label_2 = QLabel(self.page_BMedia)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 210, 291, 151))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.Pages_Widget.addWidget(self.page_BMedia)

        self.verticalLayout_4.addWidget(self.Pages_Widget)


        self.verticalLayout_2.addWidget(self.frame_pages)


        self.horizontalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_Widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BCore", None))
        self.menuButton.setText("")
        self.btn_info.setText("")
        self.MainMenu_btn.setText("")
        self.BCalc_btn.setText("")
        self.BMedia_btn.setText("")
        self.logo.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BMEDIA", None))
    # retranslateUi

