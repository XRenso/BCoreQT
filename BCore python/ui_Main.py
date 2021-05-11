# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainmdySKZ.ui'
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
        self.btn_info.setMaximumSize(QSize(40, 16777215))
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
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        self.gridLayout_2 = QGridLayout(self.page_BCalc)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.symbols = QPlainTextEdit(self.page_BCalc)
        self.symbols.setObjectName(u"symbols")
        self.symbols.setMinimumSize(QSize(0, 110))
        font1 = QFont()
        font1.setPointSize(17)
        self.symbols.setFont(font1)

        self.gridLayout_2.addWidget(self.symbols, 1, 0, 1, 1)

        self.Calc = QFrame(self.page_BCalc)
        self.Calc.setObjectName(u"Calc")
        self.Calc.setMinimumSize(QSize(0, 300))
        self.Calc.setMaximumSize(QSize(16777215, 16777215))
        self.Calc.setFrameShape(QFrame.StyledPanel)
        self.Calc.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Calc)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Buttons_lol = QGridLayout()
        self.Buttons_lol.setSpacing(0)
        self.Buttons_lol.setObjectName(u"Buttons_lol")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.plusOrMinus = QPushButton(self.Calc)
        self.plusOrMinus.setObjectName(u"plusOrMinus")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plusOrMinus.sizePolicy().hasHeightForWidth())
        self.plusOrMinus.setSizePolicy(sizePolicy1)
        self.plusOrMinus.setMinimumSize(QSize(0, 40))
        self.plusOrMinus.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.plusOrMinus)

        self.zero = QPushButton(self.Calc)
        self.zero.setObjectName(u"zero")
        sizePolicy1.setHeightForWidth(self.zero.sizePolicy().hasHeightForWidth())
        self.zero.setSizePolicy(sizePolicy1)
        self.zero.setMinimumSize(QSize(0, 40))
        self.zero.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.zero)

        self.dot = QPushButton(self.Calc)
        self.dot.setObjectName(u"dot")
        sizePolicy1.setHeightForWidth(self.dot.sizePolicy().hasHeightForWidth())
        self.dot.setSizePolicy(sizePolicy1)
        self.dot.setMinimumSize(QSize(0, 40))
        self.dot.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.dot)

        self.equal = QPushButton(self.Calc)
        self.equal.setObjectName(u"equal")
        sizePolicy1.setHeightForWidth(self.equal.sizePolicy().hasHeightForWidth())
        self.equal.setSizePolicy(sizePolicy1)
        self.equal.setMinimumSize(QSize(0, 40))
        self.equal.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_9.addWidget(self.equal)


        self.Buttons_lol.addLayout(self.horizontalLayout_9, 5, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.oneFromX = QPushButton(self.Calc)
        self.oneFromX.setObjectName(u"oneFromX")
        sizePolicy1.setHeightForWidth(self.oneFromX.sizePolicy().hasHeightForWidth())
        self.oneFromX.setSizePolicy(sizePolicy1)
        self.oneFromX.setMinimumSize(QSize(0, 40))
        self.oneFromX.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.oneFromX)

        self.inSecondStepen = QPushButton(self.Calc)
        self.inSecondStepen.setObjectName(u"inSecondStepen")
        sizePolicy1.setHeightForWidth(self.inSecondStepen.sizePolicy().hasHeightForWidth())
        self.inSecondStepen.setSizePolicy(sizePolicy1)
        self.inSecondStepen.setMinimumSize(QSize(0, 40))
        self.inSecondStepen.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.inSecondStepen)

        self.radikal = QPushButton(self.Calc)
        self.radikal.setObjectName(u"radikal")
        sizePolicy1.setHeightForWidth(self.radikal.sizePolicy().hasHeightForWidth())
        self.radikal.setSizePolicy(sizePolicy1)
        self.radikal.setMinimumSize(QSize(0, 40))
        self.radikal.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.radikal)

        self.delenie = QPushButton(self.Calc)
        self.delenie.setObjectName(u"delenie")
        sizePolicy1.setHeightForWidth(self.delenie.sizePolicy().hasHeightForWidth())
        self.delenie.setSizePolicy(sizePolicy1)
        self.delenie.setMinimumSize(QSize(0, 40))
        self.delenie.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.delenie)


        self.Buttons_lol.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self._2 = QHBoxLayout()
        self._2.setSpacing(2)
        self._2.setObjectName(u"_2")
        self.one = QPushButton(self.Calc)
        self.one.setObjectName(u"one")
        sizePolicy1.setHeightForWidth(self.one.sizePolicy().hasHeightForWidth())
        self.one.setSizePolicy(sizePolicy1)
        self.one.setMinimumSize(QSize(0, 40))
        self.one.setMaximumSize(QSize(16777215, 16777215))

        self._2.addWidget(self.one)

        self.two = QPushButton(self.Calc)
        self.two.setObjectName(u"two")
        sizePolicy1.setHeightForWidth(self.two.sizePolicy().hasHeightForWidth())
        self.two.setSizePolicy(sizePolicy1)
        self.two.setMinimumSize(QSize(0, 40))
        self.two.setMaximumSize(QSize(16777215, 16777215))

        self._2.addWidget(self.two)

        self.three = QPushButton(self.Calc)
        self.three.setObjectName(u"three")
        sizePolicy1.setHeightForWidth(self.three.sizePolicy().hasHeightForWidth())
        self.three.setSizePolicy(sizePolicy1)
        self.three.setMinimumSize(QSize(0, 40))
        self.three.setMaximumSize(QSize(16777215, 16777215))

        self._2.addWidget(self.three)

        self.plus = QPushButton(self.Calc)
        self.plus.setObjectName(u"plus")
        sizePolicy1.setHeightForWidth(self.plus.sizePolicy().hasHeightForWidth())
        self.plus.setSizePolicy(sizePolicy1)
        self.plus.setMinimumSize(QSize(0, 40))
        self.plus.setMaximumSize(QSize(16777215, 16777215))

        self._2.addWidget(self.plus)


        self.Buttons_lol.addLayout(self._2, 4, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.seven = QPushButton(self.Calc)
        self.seven.setObjectName(u"seven")
        sizePolicy1.setHeightForWidth(self.seven.sizePolicy().hasHeightForWidth())
        self.seven.setSizePolicy(sizePolicy1)
        self.seven.setMinimumSize(QSize(0, 40))
        self.seven.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.seven)

        self.eight = QPushButton(self.Calc)
        self.eight.setObjectName(u"eight")
        sizePolicy1.setHeightForWidth(self.eight.sizePolicy().hasHeightForWidth())
        self.eight.setSizePolicy(sizePolicy1)
        self.eight.setMinimumSize(QSize(0, 40))
        self.eight.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.eight)

        self.nine = QPushButton(self.Calc)
        self.nine.setObjectName(u"nine")
        sizePolicy1.setHeightForWidth(self.nine.sizePolicy().hasHeightForWidth())
        self.nine.setSizePolicy(sizePolicy1)
        self.nine.setMinimumSize(QSize(0, 40))
        self.nine.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.nine)

        self.umnozhenie = QPushButton(self.Calc)
        self.umnozhenie.setObjectName(u"umnozhenie")
        sizePolicy1.setHeightForWidth(self.umnozhenie.sizePolicy().hasHeightForWidth())
        self.umnozhenie.setSizePolicy(sizePolicy1)
        self.umnozhenie.setMinimumSize(QSize(0, 40))
        self.umnozhenie.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.umnozhenie)


        self.Buttons_lol.addLayout(self.horizontalLayout_8, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.four = QPushButton(self.Calc)
        self.four.setObjectName(u"four")
        sizePolicy1.setHeightForWidth(self.four.sizePolicy().hasHeightForWidth())
        self.four.setSizePolicy(sizePolicy1)
        self.four.setMinimumSize(QSize(0, 40))
        self.four.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.four)

        self.five = QPushButton(self.Calc)
        self.five.setObjectName(u"five")
        sizePolicy1.setHeightForWidth(self.five.sizePolicy().hasHeightForWidth())
        self.five.setSizePolicy(sizePolicy1)
        self.five.setMinimumSize(QSize(0, 40))
        self.five.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.five)

        self.six = QPushButton(self.Calc)
        self.six.setObjectName(u"six")
        sizePolicy1.setHeightForWidth(self.six.sizePolicy().hasHeightForWidth())
        self.six.setSizePolicy(sizePolicy1)
        self.six.setMinimumSize(QSize(0, 40))
        self.six.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.six)

        self.minus = QPushButton(self.Calc)
        self.minus.setObjectName(u"minus")
        sizePolicy1.setHeightForWidth(self.minus.sizePolicy().hasHeightForWidth())
        self.minus.setSizePolicy(sizePolicy1)
        self.minus.setMinimumSize(QSize(0, 40))
        self.minus.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_10.addWidget(self.minus)


        self.Buttons_lol.addLayout(self.horizontalLayout_10, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.percent = QPushButton(self.Calc)
        self.percent.setObjectName(u"percent")
        sizePolicy1.setHeightForWidth(self.percent.sizePolicy().hasHeightForWidth())
        self.percent.setSizePolicy(sizePolicy1)
        self.percent.setMinimumSize(QSize(0, 40))
        self.percent.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.percent)

        self.inThirdStepen = QPushButton(self.Calc)
        self.inThirdStepen.setObjectName(u"inThirdStepen")
        sizePolicy1.setHeightForWidth(self.inThirdStepen.sizePolicy().hasHeightForWidth())
        self.inThirdStepen.setSizePolicy(sizePolicy1)
        self.inThirdStepen.setMinimumSize(QSize(0, 40))
        self.inThirdStepen.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.inThirdStepen)

        self.AC = QPushButton(self.Calc)
        self.AC.setObjectName(u"AC")
        sizePolicy1.setHeightForWidth(self.AC.sizePolicy().hasHeightForWidth())
        self.AC.setSizePolicy(sizePolicy1)
        self.AC.setMinimumSize(QSize(0, 40))
        self.AC.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.AC)

        self.Backspace = QPushButton(self.Calc)
        self.Backspace.setObjectName(u"Backspace")
        sizePolicy1.setHeightForWidth(self.Backspace.sizePolicy().hasHeightForWidth())
        self.Backspace.setSizePolicy(sizePolicy1)
        self.Backspace.setMinimumSize(QSize(0, 40))
        self.Backspace.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.Backspace)


        self.Buttons_lol.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.Buttons_lol)


        self.gridLayout_2.addWidget(self.Calc, 0, 0, 1, 1)

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

        self.Pages_Widget.setCurrentIndex(1)


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
        self.plusOrMinus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.dot.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.oneFromX.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.inSecondStepen.setText(QCoreApplication.translate("MainWindow", u"x^2", None))
        self.radikal.setText(QCoreApplication.translate("MainWindow", u"\u221a(\u043a\u043e\u0440\u0435\u043d\u044c)", None))
        self.delenie.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.umnozhenie.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.percent.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.inThirdStepen.setText(QCoreApplication.translate("MainWindow", u"x^3", None))
        self.AC.setText(QCoreApplication.translate("MainWindow", u"AC", None))
        self.Backspace.setText(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"BMEDIA", None))
    # retranslateUi

