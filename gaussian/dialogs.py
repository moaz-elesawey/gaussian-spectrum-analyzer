from PySide2 import QtWidgets
import matplotlib
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar
)


from ui.ui_energy import Ui_Dialog
from ui.ui_nmr import Ui_NMRDialog
from ui.ui_style import Ui_StyleDialog
from ui.ui_optimization import Ui_Optimization

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
        

class OptmGraph(QtWidgets.QDialog):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.setWindowTitle("Optimization Graph")

        self.fig = Figure(figsize=(15, 9))

        self.energy_ax    = self.fig.add_subplot(313)
        
        self.rms_force_ax = self.fig.add_subplot(321)
        self.rms_displ_ax = self.fig.add_subplot(322)

        self.max_force_ax = self.fig.add_subplot(323)
        self.max_displ_ax = self.fig.add_subplot(324)

        self.energy_ax.set_title('Change in Enegry')
        self.rms_force_ax.set_title('RMS Force')
        self.rms_displ_ax.set_title('RMS Displacement')
        self.max_force_ax.set_title('Max Force')
        self.max_displ_ax.set_title('Max Displacement')
        
        self.graph = FigureCanvasQTAgg(self.fig)
        self.toolbar = NavigationToolbar(self.graph, self)

        self.lay = QtWidgets.QVBoxLayout(self)
        self.lay.addWidget(self.toolbar)
        self.lay.addWidget(self.graph)

        self.fig.tight_layout()

        self.setLayout(self.lay)


class OptimizationDialog(Ui_Optimization, QtWidgets.QDialog):
    def __init__(self, *a, data=None, **kw):
        super().__init__(*a, **kw)

        self.setupUi(self)
        self.setWindowTitle('Molecule Optimization Steps')

        self.data = data

        self.show_spectrum.clicked.connect(self.show_spectrum_func)

    def show_spectrum_func(self):

        self.optm_graph = OptmGraph()

        energy = self.data[0]
        rms_force = self.data[1]
        rms_displ = self.data[2]
        max_force = self.data[3]
        max_displ = self.data[4]

        self.optm_graph.energy_ax.plot(range(1, energy.shape[0]+1), energy, color='k', markeredgecolor='k', markerfacecolor='w', marker='o')
        self.optm_graph.rms_force_ax.plot(range(1, energy.shape[0]+1), rms_force, color='k', markeredgecolor='k', markerfacecolor='w', marker='o')
        self.optm_graph.rms_displ_ax.plot(range(1, energy.shape[0]+1), rms_displ, color='k', markeredgecolor='k', markerfacecolor='w', marker='o')
        self.optm_graph.max_force_ax.plot(range(1, energy.shape[0]+1), max_force, color='k', markeredgecolor='k', markerfacecolor='w', marker='o')
        self.optm_graph.max_displ_ax.plot(range(1, energy.shape[0]+1), max_displ, color='k', markeredgecolor='k', markerfacecolor='w', marker='o')

        self.optm_graph.energy_ax.set_xticks(range(1, energy.shape[0]+1, energy.shape[0]//10))
        self.optm_graph.rms_force_ax.set_xticks(range(1, energy.shape[0]+1, energy.shape[0]//10))
        self.optm_graph.rms_displ_ax.set_xticks(range(1, energy.shape[0]+1, energy.shape[0]//10))
        self.optm_graph.max_force_ax.set_xticks(range(1, energy.shape[0]+1, energy.shape[0]//10))
        self.optm_graph.max_displ_ax.set_xticks(range(1, energy.shape[0]+1, energy.shape[0]//10))

        self.optm_graph.fig.tight_layout()

        self.optm_graph.show()


class NMRGraph(QtWidgets.QDialog):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.setWindowTitle("NMR Graph")

        self.fig = Figure(figsize=(10, 4))

        self.ax = self.fig.add_subplot(111)
        
        self.ax.set_xlabel('Sheilding (ppm)', fontsize=14)
        self.ax.set_ylabel('Degenaracy', fontsize=14)
        self.ax.set_title("NMR Spectrum", fontsize=15)

        self.fig.tight_layout()

        self.graph = FigureCanvasQTAgg(self.fig)
        self.toolbar = NavigationToolbar(self.graph, self)

        self.lay = QtWidgets.QVBoxLayout(self)
        self.lay.addWidget(self.toolbar)
        self.lay.addWidget(self.graph)

        self.setLayout(self.lay)


class NMRDialog(Ui_NMRDialog, QtWidgets.QDialog):
    def __init__(self, *a, x=None, y=None, sheilding=None, deg=None, **kw):
        super().__init__(*a, **kw)

        self.setupUi(self)
        self.setWindowTitle('Molecule NMR Spectrum')

        self.x = x
        self.y = y
        self.sheilding = sheilding
        self.deg = deg

        self.show_spectrum.clicked.connect(self.show_spectrum_func)

    def show_spectrum_func(self):

        self.nmr_graph = NMRGraph()
        self.nmr_graph.ax.vlines(x=self.sheilding, ymin=0, ymax=self.deg, color='k', lw=.9)
        self.nmr_graph.ax.plot(self.x, self.y, color='#FF0000', lw=1.1)
        
        self.nmr_graph.fig.tight_layout()

        self.nmr_graph.show()
