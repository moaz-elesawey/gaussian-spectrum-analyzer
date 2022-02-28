# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_energy.ui'
#
# Created by: PySide2 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 337)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.energies_table = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("Noto Mono")
        font.setPointSize(12)
        self.energies_table.setFont(font)
        self.energies_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.energies_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.energies_table.setAlternatingRowColors(True)
        self.energies_table.setTextElideMode(QtCore.Qt.ElideLeft)
        self.energies_table.setWordWrap(False)
        self.energies_table.setObjectName("energies_table")
        self.energies_table.setColumnCount(4)
        self.energies_table.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.energies_table.setHorizontalHeaderItem(3, item)
        self.energies_table.horizontalHeader().setCascadingSectionResizes(True)
        self.energies_table.horizontalHeader().setStretchLastSection(False)
        self.energies_table.verticalHeader().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.energies_table)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Energies of the Molecule"))
        self.energies_table.setSortingEnabled(True)
        item = self.energies_table.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "Energy="))
        item = self.energies_table.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "Enthalpy="))
        item = self.energies_table.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "Gibbs Free Energy="))
        item = self.energies_table.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "Zero-point correction="))
        item = self.energies_table.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "Zero-point Energies="))
        item = self.energies_table.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Hartree (u.a)"))
        item = self.energies_table.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Kcal/mol"))
        item = self.energies_table.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "KJ/mol"))
        item = self.energies_table.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "eV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
