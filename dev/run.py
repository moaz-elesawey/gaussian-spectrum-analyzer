import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import importlib

from ui.ui_splash import Ui_Form
from utils import PATHS

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

counter = 0

class SplashScreen(QWidget):
    packages_loaded = False

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.SplashScreen | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0, 60))
        self.ui.mainFrame.setGraphicsEffect(self.shadow)

        self.ui.title_3.setPixmap(QPixmap(os.path.join(BASE_DIR, PATHS['icons'], 'spectrum-icon.png')))

        self.timer = QTimer()
        self.timer.timeout.connect(self.trigger_progress)
        self.timer.start(30)

        self.timer.singleShot(0, lambda: self.ui.loader.setText('<strong>WELCOME</strong> to <strong>GSA</strong>'))
        self.timer.singleShot(1000, lambda: self.ui.loader.setText('<strong>LOADING</strong> PACKAGES'))
        self.timer.singleShot(2500, lambda: self.ui.loader.setText('<strong>LOADING</strong> USER INTERFACE'))

        self.timer.singleShot(1750, self.trigger_load_packages)
        self.show()

    def trigger_progress(self):
        global counter

        self.ui.progress.setValue(counter)

        if counter > 100:
            self.timer.stop()

            from gaussian import SpectrumAnalyzer
            self.main_win = SpectrumAnalyzer()
            self.main_win.show()

            self.close()

        counter += 1

    def trigger_load_packages(self):
        from gaussian import SpectrumAnalyzer


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = SplashScreen()
    sys.exit(app.exec())