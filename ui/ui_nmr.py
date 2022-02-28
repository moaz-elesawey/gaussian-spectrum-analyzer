# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_nmr.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NMRDialog(object):
    def setupUi(self, NMRDialog):
        if not NMRDialog.objectName():
            NMRDialog.setObjectName(u"NMRDialog")
        NMRDialog.resize(560, 625)
        self.verticalLayout = QVBoxLayout(NMRDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(NMRDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Noto Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.data_table = QTableWidget(NMRDialog)
        self.data_table.setObjectName(u"data_table")
        font1 = QFont()
        font1.setFamily(u"Noto Mono")
        self.data_table.setFont(font1)

        self.verticalLayout.addWidget(self.data_table)

        self.frame = QFrame(NMRDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFont(font1)
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_spectrum = QPushButton(self.frame)
        self.show_spectrum.setObjectName(u"show_spectrum")
        self.show_spectrum.setMinimumSize(QSize(0, 28))
        self.show_spectrum.setFont(font1)

        self.horizontalLayout.addWidget(self.show_spectrum)

        self.export_btn = QPushButton(self.frame)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setMinimumSize(QSize(0, 28))
        self.export_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.export_btn)

        self.copy_values = QPushButton(self.frame)
        self.copy_values.setObjectName(u"copy_values")
        self.copy_values.setMinimumSize(QSize(0, 28))
        self.copy_values.setFont(font1)

        self.horizontalLayout.addWidget(self.copy_values)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(NMRDialog)

        self.show_spectrum.setDefault(True)


        QMetaObject.connectSlotsByName(NMRDialog)
    # setupUi

    def retranslateUi(self, NMRDialog):
        NMRDialog.setWindowTitle(QCoreApplication.translate("NMRDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("NMRDialog", u"NMR Sheilding Values", None))
        self.show_spectrum.setText(QCoreApplication.translate("NMRDialog", u"Show Spectrum", None))
        self.export_btn.setText(QCoreApplication.translate("NMRDialog", u"Export to CSV", None))
        self.copy_values.setText(QCoreApplication.translate("NMRDialog", u"Copy values", None))
    # retranslateUi

