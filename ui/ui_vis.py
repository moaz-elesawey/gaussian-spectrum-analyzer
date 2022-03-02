# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_vis.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UVDialog(object):
    def setupUi(self, UVDialog):
        if not UVDialog.objectName():
            UVDialog.setObjectName(u"UVDialog")
        UVDialog.resize(598, 329)
        self.verticalLayout = QVBoxLayout(UVDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(UVDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Noto Mono")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.data_table = QTableWidget(UVDialog)
        self.data_table.setObjectName(u"data_table")

        self.verticalLayout.addWidget(self.data_table)

        self.frame = QFrame(UVDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.show_spectrum_btn = QPushButton(self.frame)
        self.show_spectrum_btn.setObjectName(u"show_spectrum_btn")

        self.horizontalLayout.addWidget(self.show_spectrum_btn)

        self.export_to_csv = QPushButton(self.frame)
        self.export_to_csv.setObjectName(u"export_to_csv")

        self.horizontalLayout.addWidget(self.export_to_csv)

        self.copy_values = QPushButton(self.frame)
        self.copy_values.setObjectName(u"copy_values")

        self.horizontalLayout.addWidget(self.copy_values)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(UVDialog)

        QMetaObject.connectSlotsByName(UVDialog)
    # setupUi

    def retranslateUi(self, UVDialog):
        UVDialog.setWindowTitle(QCoreApplication.translate("UVDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("UVDialog", u"UV VIS and ECD Spectrum", None))
        self.show_spectrum_btn.setText(QCoreApplication.translate("UVDialog", u"Show Spectrum", None))
        self.export_to_csv.setText(QCoreApplication.translate("UVDialog", u"Export to CSV", None))
        self.copy_values.setText(QCoreApplication.translate("UVDialog", u"Copy Values", None))
    # retranslateUi

