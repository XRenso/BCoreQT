################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
from ui_functions import *
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtGui as qtGUI
from PyQt5 import QtCore as qtCORE
from PyQt5 import QtWidgets as qtWIDGETS
from PyQt5.QtCore import QRect
import re
## ==> SPLASH SCREEN
from ui_BCore import Ui_SplashScreen

## ==> MAIN WINDOW
from ui_Main import Ui_MainWindow
from ui_info import Ui_Info
## ==> GLOBALS
counter = 0

# YOUR APPLICATION
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



#SetIconOnButtons
        self.ui.menuButton.setIcon(QtGui.QIcon("21.png"))#Menu_btn

        self.ui.BCalc_btn.setIcon(QtGui.QIcon("BCalc.png"))#BCalc_btn
        self.ui.BCalc_btn.setIconSize(QtCore.QSize(80,80))#change size of BCalc icon

        self.ui.MainMenu_btn.setIcon(QtGui.QIcon("Home.png"))#Main Menu
        self.ui.MainMenu_btn.setIconSize(QtCore.QSize(80,80))#change size of main menu icon

        self.ui.btn_info.setIcon(QtGui.QIcon("info.png"))#Info
        self.ui.btn_info.setIconSize(QtCore.QSize(40,60))

#TOGGLE MENU

        self.ui.menuButton.clicked.connect(lambda: UIFuncrions.toggleMenu(self, 200 , True))#Button
        #ShortCUt
        self.shortcut = QShortcut(QKeySequence('Tab'), self)
        self.shortcut.activated.connect(lambda:UIFuncrions.toggleMenu(self,200,True))

#PAGES

        #MAIN MENU PAGE
        self.ui.MainMenu_btn.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_Main))

        #BCalc PAGE
        self.ui.BCalc_btn.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_BCalc))

        #BMedia PAGE
        self.ui.BMedia_btn.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_BMedia))
#################################3
#Show info
        #Button
        self.ui.btn_info.clicked.connect(lambda:self.openInfoWindow())
        #Shortcut
        self.shortcut = QShortcut(QKeySequence('Ctrl+B'), self)
        self.shortcut.activated.connect(lambda:self.openInfoWindow())
##########################

#BCalc


        self.ui.retranslateUi(self)
        self.ui.zero.clicked.connect(lambda:self.ui.show) #0
        self.ui.one.clicked.connect(lambda:self.ui.show) #1
        self.ui.two.clicked.connect(lambda:self.ui.show)#2
        self.ui.three.clicked.connect(lambda:self.ui.show)#3
        self.ui.four.clicked.connect(lambda:self.ui.show)#4
        self.ui.five.clicked.connect(lambda:self.ui.show)#5
        self.ui.six.clicked.connect(lambda:self.ui.show)#6
        self.ui.seven.clicked.connect(lambda: self.ui.show)#7
        self.ui.eight.clicked.connect(lambda:self.ui.show)#8
        self.ui.nine.clicked.connect(lambda:self.ui.show)#9

        self.ui.plus.clicked.connect(lambda:self.ui.show)#+
        self.ui.minus.clicked.connect(lambda:self.ui.show)#-
        self.ui.umnozhenie.clicked.connect(lambda:self.ui.show)#x
        self.ui.delenie.clicked.connect(lambda:self.ui.show)#/

        self.ui.dot.clicked.connect(lambda:self.ui.show)#.
        self.ui.Backspace.clicked.connect(lambda:self.ui.show)#<=
        self.ui.equal.clicked.connect(lambda:self.ui.show)#=
        self.ui.plusOrMinus.clicked.connect(lambda:self.ui.show)#+/-

        self.ui.AC.clicked.connect(lambda:self.ui.show)#AC
        self.ui.inThirdStepen.clicked.connect(lambda:self.ui.show)#x^3
        self.ui.percent.clicked.connect(lambda:self.ui.show)#%

        self.ui.oneFromX.clicked.connect(lambda:self.ui.show)#1/x
        self.ui.inSecondStepen.clicked.connect(lambda:self.ui.show)#x^2
        self.ui.radikal.clicked.connect(lambda:self.ui.show)#sqrt

        self.text = ''
        self.processed = False






    def process(self):
        try:
            inp=self.text
            inp = re.sub(r"\.(?![0-9])","", inp)
            val = eval(inp, {'__builtins__':None})
            self.text=str(val)
        except Exception as e:
            self.text = str(e)
        self.processed = True

#    def show(self):

        self.text = self.ui.symbols.toPlainText()

        num_list = [str(num) for num in [0,1,2,3,4,5,6,7,8,9,'.']]
        op_list = ['+','-','*','/','%']

        c_or_ce_list = ['AC']
        func_list=['1/x','x^2','sqrt','+/-','x^3']

        if self.sender().text()!='Backspace':
            if self.sender().text() in num_list :
                if self.processed == True:
                    self.text=''
                self.text+=self.sender().text()
                self.processed = False

            if self.sender().text() in op_list :

                self.text+=self.sender().text()
                self.processed = False

            if self.sender().text() =='=':
                self.process()
            if self.sender().text() in c_or_ce_list:
                self.text=''
                self.processed = False
            if self.sender().text() in func_list:
                if self.sender().text() == func_list[0]:
                    try:
                        self.text= str(1/eval(self.text))
                    except Exception as e:
                        self.text=str(e)
                    self.processed = False
                if self.sender().text() == func_list[1]:
                    self.text= str(eval(self.text)**2)
                    self.processed = False
                if self.sender().text() == func_list[2]:
                    self.text= str(eval(self.text)**0.5)
                    self.processed = False
                if self.sender().text() == func_list[3]:
                    self.text= str(-1*eval(self.text))
                    self.processed = False
                if self.sender().text() == func_list[4]:
                    self.text= str(eval(self.text)**3)
                    self.processed = False


        else:
            self.text = self.text[0:len(self.text)-1]

        self.ui.symbols.setText(self.text)

#########################3
    def openInfoWindow(self):
        self.info = Info_Screen()
        self.info.show()




# SPLASH SCREEN
class Info_Screen(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Info()

        self.ui.setupUi(self)

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()

        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO THE FUTURE")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_loading.setText("<strong>loading..</strong> BORSCHT"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_loading.setText("<strong>loading...</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()

    sys.exit(app.exec_())
