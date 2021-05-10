# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infoskUHLs.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Info(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.StyledPanel)
        self.menu.setFrameShadow(QFrame.Raised)
        self.menu.setLineWidth(1)
        self.verticalLayout_4 = QVBoxLayout(self.menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.studioNameFrame = QFrame(self.menu)
        self.studioNameFrame.setObjectName(u"studioNameFrame")
        self.studioNameFrame.setMinimumSize(QSize(0, 70))
        self.studioNameFrame.setMaximumSize(QSize(16777215, 70))
        self.studioNameFrame.setFrameShape(QFrame.StyledPanel)
        self.studioNameFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.studioNameFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.StudioName = QLabel(self.studioNameFrame)
        self.StudioName.setObjectName(u"StudioName")
        self.StudioName.setMinimumSize(QSize(0, 70))
        self.StudioName.setMaximumSize(QSize(16777215, 70))
        self.StudioName.setTextFormat(Qt.AutoText)
        self.StudioName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.StudioName)


        self.verticalLayout_4.addWidget(self.studioNameFrame)

        self.MAINTEXT = QFrame(self.menu)
        self.MAINTEXT.setObjectName(u"MAINTEXT")
        self.MAINTEXT.setMinimumSize(QSize(0, 500))
        self.MAINTEXT.setMaximumSize(QSize(16777215, 16777215))
        self.MAINTEXT.setFrameShape(QFrame.StyledPanel)
        self.MAINTEXT.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.MAINTEXT)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.INFO = QLabel(self.MAINTEXT)
        self.INFO.setObjectName(u"INFO")
        self.INFO.setMinimumSize(QSize(0, 600))
        self.INFO.setMaximumSize(QSize(16777215, 900))
        self.INFO.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.INFO)

        self.creators = QLabel(self.MAINTEXT)
        self.creators.setObjectName(u"creators")
        self.creators.setMinimumSize(QSize(0, 50))
        self.creators.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_3.addWidget(self.creators)


        self.verticalLayout_4.addWidget(self.MAINTEXT)


        self.verticalLayout.addWidget(self.menu)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Info", None))
        self.StudioName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#0000ff;\">BORCH ENTERTAINMENT</span></p></body></html>", None))
        self.INFO.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">\u041f\u0420\u041e\u0414\u0423\u041a\u0422 \u042f\u0412\u041b\u042f\u0415\u0422\u0421\u042f \u0421\u041e\u0411\u0421\u0422\u0412\u0415\u041d\u041e\u0421\u0422\u042c\u042e BORCH</span></p><p align=\"center\"><br/>\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043d\u0435 \u044f\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u0432\u0440\u0435\u0434\u043e\u043d\u043e\u0441\u043d\u044b\u043c \u041f\u041e \u0438 \u043d\u0435 \u0441\u043e\u0431\u0438\u0440\u0430\u0435\u0442 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e \u043e \u0432\u0430\u0441 \u0438 \u0441 \u0432\u0430\u0448\u0435\u0433\u043e \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430.</p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">\u0421\u041f\u0418\u0421\u041e\u041a \u0417\u0410 \u0427\u0422\u041e \u041c\u042b \u041d\u0415 \u041d\u0415"
                        "\u0421\u0401\u041c \u041e\u0422\u0412\u0415\u0422\u0421\u0412\u0415\u041d\u041d\u041e\u0421\u0422\u042c:</span></p><p align=\"center\">1)\u0417\u0430 \u0432\u0430\u0448\u0435 \u0437\u043b\u043e\u0434\u0435\u044f\u043d\u0438\u044f \u0441\u0434\u0435\u043b\u0430\u043d\u043d\u044b\u0435 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u044d\u0442\u043e\u0433\u043e \u041f\u041e </p><p align=\"center\">2)\u0417\u0430 \u0432\u0440\u0435\u0434 \u0432\u0430\u0448\u0435\u043c\u0443 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u043c\u0443 \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0443 \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u044d\u0442\u043e\u0433\u043e \u041f\u041e</p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.creators.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442 - \u041e\u0434\u0435\u0440\u0438\u0439 \u042f\u0440\u043e\u0441\u043b\u0430\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447</p><p align=\"right\">\u0410\u0432\u0442\u043e\u0440 \u0438\u0434\u0435\u0439 - \u0411\u0430\u0439\u0434\u0430\u043b\u0430 \u041d\u0438\u043a\u0438\u0442\u0430 \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447</p><p align=\"right\"><br/></p></body></html>", None))
    # retranslateUi
