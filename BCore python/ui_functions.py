from main import *

class UIFuncrions(MainWindow):
    def toggleMenu(self, maxHigh, enable):
        if enable == True:
            high = self.ui.frame_top_menu.height()
            maxExtended = maxHigh
            standart = 100

            if high == 100:
                heightExtended = maxExtended
            else:
                heightExtended = standart

            #Animation

            self.animation = QPropertyAnimation(self.ui.frame_top_menu, b"minimumHeight")
            self.animation.setDuration(400)
            self.animation.setStartValue(high)
            self.animation.setEndValue(heightExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
