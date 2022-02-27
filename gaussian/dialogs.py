
from PyQt5 import QtWidgets
from ui.ui_energy import Ui_Dialog
from ui.ui_style import Ui_StyleDialog

class StyleDialog(QtWidgets.QDialog, Ui_StyleDialog):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.setupUi(self)
        self.setWindowTitle('Change Graph Style')


class EnergyDialog(Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.setupUi(self)
        self.setWindowTitle('Molecule Energies')

