# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_optimization.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Optimization(object):
    def setupUi(self, Optimization):
        if not Optimization.objectName():
            Optimization.setObjectName(u"Optimization")
        Optimization.resize(565, 663)
        self.verticalLayout = QVBoxLayout(Optimization)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Optimization)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Noto Mono")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.data_table = QTableWidget(Optimization)
        self.data_table.setObjectName(u"data_table")
        font1 = QFont()
        font1.setFamily(u"Noto Mono")
        self.data_table.setFont(font1)

        self.verticalLayout.addWidget(self.data_table)

        self.frame = QFrame(Optimization)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_spectrum = QPushButton(self.frame)
        self.show_spectrum.setObjectName(u"show_spectrum")
        self.show_spectrum.setFont(font1)

        self.horizontalLayout.addWidget(self.show_spectrum)

        self.export_csv = QPushButton(self.frame)
        self.export_csv.setObjectName(u"export_csv")
        self.export_csv.setFont(font1)

        self.horizontalLayout.addWidget(self.export_csv)

        self.copy_values = QPushButton(self.frame)
        self.copy_values.setObjectName(u"copy_values")
        self.copy_values.setFont(font1)

        self.horizontalLayout.addWidget(self.copy_values)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Optimization)

        QMetaObject.connectSlotsByName(Optimization)
    # setupUi

    def retranslateUi(self, Optimization):
        Optimization.setWindowTitle(QCoreApplication.translate("Optimization", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Optimization", u"Molcule Optimization Steps", None))
        self.show_spectrum.setText(QCoreApplication.translate("Optimization", u"Show Graph", None))
        self.export_csv.setText(QCoreApplication.translate("Optimization", u"Export to CSV", None))
        self.copy_values.setText(QCoreApplication.translate("Optimization", u"Copy Values", None))
    # retranslateUi

