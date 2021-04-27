# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BCorebgWlJb.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 80, 661, 71))
        font = QFont()
        font.setFamily(u"Noto Sans Sinhala UI")
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(254, 121, 199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 140, 651, 31))
        font1 = QFont()
        font1.setFamily(u"Noto Sans Sinhala UI")
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(84, 89, 114);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 240, 651, 41))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background-color: rgb(98, 114, 164);\n"
"	color:rgb(200, 200, 200);\n"
"	border-style : none;\n"
"	border-radius: 20px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 20px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.568, x2:1, y2:0.586, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(255, 70, 70, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 300, 651, 31))
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"color: rgb(84, 89, 114);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_creator = QLabel(self.dropShadowFrame)
        self.label_creator.setObjectName(u"label_creator")
        self.label_creator.setGeometry(QRect(330, 350, 311, 21))
        font2 = QFont()
        font2.setFamily(u"Noto Sans Sinhala UI")
        font2.setPointSize(12)
        self.label_creator.setFont(font2)
        self.label_creator.setStyleSheet(u"color: rgb(84, 89, 114);")
        self.label_creator.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<STRONG>Borch</STRONG>CORE", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<STRONG>CORE OF</STRONG> YOUR <strong>LIFE </strong>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.label_creator.setText(QCoreApplication.translate("SplashScreen", u"Created: <strong>Borch Entr. Oderiy Yaroslav</strong>", None))
    # retranslateUi

