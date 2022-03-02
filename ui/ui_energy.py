# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_energy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(941, 337)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Noto Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.energies_table = QTableWidget(Dialog)
        if (self.energies_table.columnCount() < 4):
            self.energies_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.energies_table.rowCount() < 8):
            self.energies_table.setRowCount(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(7, __qtablewidgetitem11)
        self.energies_table.setObjectName(u"energies_table")
        font1 = QFont()
        font1.setFamily(u"Noto Mono")
        font1.setPointSize(12)
        self.energies_table.setFont(font1)
        self.energies_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.energies_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.energies_table.setAlternatingRowColors(True)
        self.energies_table.setTextElideMode(Qt.ElideLeft)
        self.energies_table.setSortingEnabled(True)
        self.energies_table.setWordWrap(False)
        self.energies_table.horizontalHeader().setCascadingSectionResizes(True)
        self.energies_table.horizontalHeader().setStretchLastSection(False)
        self.energies_table.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.energies_table)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Energies of the Molecule", None))
        ___qtablewidgetitem = self.energies_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Hartree (a.u)", None));
        ___qtablewidgetitem1 = self.energies_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Kcal/mol", None));
        ___qtablewidgetitem2 = self.energies_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"KJ/mol", None));
        ___qtablewidgetitem3 = self.energies_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"eV", None));
        ___qtablewidgetitem4 = self.energies_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Thermal correction to Energy=", None));
        ___qtablewidgetitem5 = self.energies_table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Thermal correction to Enthalpy=", None));
        ___qtablewidgetitem6 = self.energies_table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Thermal correction to Gibbs Free Energy=", None));
        ___qtablewidgetitem7 = self.energies_table.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Zero-point correction=", None));
        ___qtablewidgetitem8 = self.energies_table.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Sum of electronic and zero-point Energies=", None));
        ___qtablewidgetitem9 = self.energies_table.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog", u"Sum of electronic and thermal Energies=", None));
        ___qtablewidgetitem10 = self.energies_table.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dialog", u"Sum of electronic and thermal Enthalpies=", None));
        ___qtablewidgetitem11 = self.energies_table.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dialog", u"Sum of electronic and thermal Free Energies=", None));
    # retranslateUi

