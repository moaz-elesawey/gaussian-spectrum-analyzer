from concurrent.futures import thread
import os
from pprint import pprint
import sys
import csv
from threading import Thread
from time import time
from PySide2.QtWidgets import (
    QDialog, QFileDialog, QTableWidgetItem, 
    QApplication, QMessageBox, QMainWindow, QToolBar, 
    QAction, QHeaderView, QSizePolicy
)
from PySide2.QtGui import QIcon, QPixmap
from matplotlib import pyplot as plt

from ui import Ui_SpectrumAnalyzer

from gaussian import *

from .dialogs import NMRDialog, StyleDialog, EnergyDialog, OptimizationDialog

from gaussian.togglers import (
    toggle_broadening, toggle_grid,
    toggle_hide_verticals,
    toggle_marks, toggle_peaks,
    toggle_scale_curve,
    toggle_scale_x, toggle_scale_y
)

from .triggers import (
    trigger_apply_changes, trigger_broadening_slider,
    trigger_broadening_text, trigger_change_page,
    trigger_change_style, trigger_linestyle_change,
    trigger_pick_color, trigger_spectrum_select,
    trigger_style_button, trigger_tab_change,
    trigger_table_selection, trigger_tight_layout
)

from utils import EXPORT_FORMATS, LINESTYLES, PATHS, BASE_DIR, SPECTRUM_TYPES, convert_to_csv, save_figure

import pyqtgraph.opengl as gl
import numpy as np

class SpectrumAnalyzer(QMainWindow):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.ui = Ui_SpectrumAnalyzer()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'] ,"spectrum-icon.png")))
        self.setWindowTitle("GSA Gaussian Spectrum Analyzer")
        self.resize(1280, 750)
        self.setMinimumWidth(1280)

        self.item_selected = False
        self.a_file_loaded = False

        self.p = Properties()

        self.compound = []
        self.original_compound = []
        self.grid_toggled = False

        self.optm_dialog = None
        self.energy_dialog = None
        self.nmr_dialog = None

        self.createActions()

        # init Ui Components
        self.uiComponents()

        # init Ui
        self.initUi()

        # init Actions
        self.initActions()

    def uiComponents(self):
        
        self.spectrumGraph = SpectrumGraph()
        self.spectrumGraph.setMaximumHeight(120000)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.spectrumGraph.sizePolicy().hasHeightForWidth())
        self.spectrumGraph.setSizePolicy(sizePolicy)

        self.graphToolbar = Toolbar(self.spectrumGraph, self)

        self.setStyleSheet("QFrame#spectrumGraph{background: rgb(100, 0, 0);}")

        self.viewer = gl.GLViewWidget()
        self.viewer_grid = gl.GLGridItem()

        self.style_dialog = StyleDialog()
        self.style_dialog.setModal(True)
        self.style_dialog.ok_btn.clicked.connect(lambda: trigger_style_button(self, 'OK'))
        self.style_dialog.apply_btn.clicked.connect(lambda: trigger_style_button(self, 'Apply'))
        self.style_dialog.cancel_btn.clicked.connect(lambda: trigger_style_button(self, 'Cancel'))


    def initUi(self):

        # set the state of all widget to disabled untill a file is loaded
        self.setState(True)

        self.ui.broadening_btn.setDisabled(True)
        self.ui.broadening_inp.setDisabled(True)
        self.ui.broadening_slider.setDisabled(True)
        self.ui.broadening_select.setDisabled(True)
        self.ui.label.setDisabled(True)

        self.ui.scale_curve_inp.setDisabled(True)
        self.ui.scale_curve_btn.setDisabled(True)

        self.ui.peaks_select.setDisabled(True)
        self.ui.marks_select.setDisabled(True)

        self.ui.scale_x_inp.setDisabled(True)
        self.ui.scale_x_btn.setDisabled(True)
        self.ui.scale_y_inp.setDisabled(True)
        self.ui.scale_y_btn.setDisabled(True)
        
        ico1 = QIcon()
        ico1.addPixmap(QPixmap(os.path.join(BASE_DIR, PATHS['icons'], 'zoom-out.png')))
        self.ui.zoom_out_btn.setIcon(ico1)
        ico2 = QIcon()
        ico2.addPixmap(QPixmap(os.path.join(BASE_DIR, PATHS['icons'], 'aspect-ratio.png')))
        self.ui.tight_graph_btn.setIcon(ico2)

        # add spectrum graph to it's frame
        self.ui.spectrum_frame_layout.addWidget(self.graphToolbar)
        self.ui.spectrum_frame_layout.addWidget(self.spectrumGraph)
        self.ui.export_formats_select.addItems(EXPORT_FORMATS)
        self.style_dialog.line_shape_select.addItems(LINESTYLES)
        self.style_dialog.spike_shape_select.addItems(LINESTYLES)
        self.ui.spectrumType.addItems(SPECTRUM_TYPES)

        self.viewer.setWindowTitle('STL Viewer')
        self.viewer.setCameraPosition(distance=25)
        self.ui.renderLayout.addWidget(self.viewer)
        
        self.ui.start_animation_btn.setMinimumWidth(0)
        self.ui.start_animation_btn.setText('')
        self.ui.start_animation_btn.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'] ,"grid_icon.png")))

        self.ui.frame_5.resize(300, 750)

    def createActions(self):
        menuBar = self.menuBar()
        self.toolBar = QToolBar()

        self.fileMenu = menuBar.addMenu('&File')
        self.editMenu = menuBar.addMenu('&Edit')
        # self.viewMenu = menuBar.addMenu('&View')
        self.resultsMenu = menuBar.addMenu('&Results')
        self.aboutMenu = menuBar.addMenu('&About')

        self.openAction = QAction("&Open Gaussian File (.LOG)")
        self.openAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'open-file.png')))
        self.openAction.setShortcut('Ctrl+o')

        self.saveAction = QAction("&Export Graph")
        self.saveAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'save-image.png')))
        self.saveAction.setShortcut("Ctrl+e")

        self.quitAction = QAction("&Quit")
        self.quitAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'quit.png')))
        self.quitAction.setShortcut("Ctrl+q")

        self.changeStyleAction = QAction('&Show Style Dialog')
        self.changeStyleAction.setShortcut("Ctrl+f")

        self.toggleBroaden = QAction("Show/Hide Broaden")
        self.toggleBroaden.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'broaden-icon.png')))
        self.toggleBroaden.setShortcut("Ctrl+b")

        self.toggleSpikes = QAction("Show/Hide Spike")
        self.toggleSpikes.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'spikes-icon.png')))
        self.toggleSpikes.setShortcut("Ctrl+p")

        self.tightFigureLayoutAction = QAction('&Tight Figure Layout')
        self.tightFigureLayoutAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'aspect-ratio.png')))
        self.tightFigureLayoutAction.setShortcut("Ctrl+t")

        self.zoomOutAction = QAction("&Zoom Out")
        self.zoomOutAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'zoom-out.png')))
        self.zoomOutAction.setShortcut("Ctrl+z")

        self.toggleGrid = QAction('&Show/Hid Grid')
        self.toggleGrid.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'grid_icon.png')))
        
        self.helpAction = QAction("&Help")

        self.showEnergiesAction = QAction("&Show Molecule Energies")
        self.showEnergiesAction.setShortcut("Ctrl+Shift+e")
        self.showEnergiesAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'energy-icon.png')))

        self.showOptmAction = QAction("&Show Optimization Steps")
        self.showOptmAction.setShortcut("Ctrl+Shift+o")
        self.showOptmAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'optm-icon.png')))

        self.showNMRAction = QAction("&Show NMR Spectrum")
        self.showNMRAction.setIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'], 'nmr-icon.png')))
        self.showNMRAction.setShortcut("Ctrl+Shift+n")

        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAction)

        self.aboutMenu.addAction(self.helpAction)

        self.editMenu.addAction(self.toggleBroaden)
        self.editMenu.addAction(self.toggleSpikes)
        self.editMenu.addAction(self.tightFigureLayoutAction)
        self.editMenu.addAction(self.zoomOutAction)
        self.editMenu.addAction(self.toggleGrid)
        self.editMenu.addAction(self.changeStyleAction)

        self.resultsMenu.addAction(self.showEnergiesAction)
        self.resultsMenu.addAction(self.showOptmAction)

        self.resultsMenu.addAction(self.showNMRAction)

        self.toolBar.addAction(self.openAction)
        self.toolBar.addAction(self.saveAction)
        self.toolBar.addAction(self.quitAction)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.toggleBroaden)
        self.toolBar.addAction(self.toggleSpikes)
        self.toolBar.addAction(self.tightFigureLayoutAction)
        self.toolBar.addAction(self.zoomOutAction)
        self.toolBar.addAction(self.toggleGrid)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.showEnergiesAction)
        self.toolBar.addAction(self.showOptmAction)
        self.toolBar.addAction(self.showNMRAction)

        self.addToolBar(self.toolBar)

    def initActions(self):
        self.ui.broadening_check.toggled.connect(lambda e: toggle_broadening(self, e))
        self.ui.scale_curve_check.toggled.connect(lambda e: toggle_scale_curve(self, e))
        self.ui.scale_x_check.toggled.connect(lambda e: toggle_scale_x(self, e))
        self.ui.scale_y_check.toggled.connect(lambda e: toggle_scale_y(self, e))
        self.ui.show_peaks_check.toggled.connect(lambda e: toggle_peaks(self, e))
        self.ui.show_marks_check.toggled.connect(lambda e: toggle_marks(self, e))
        self.ui.hide_verticals_check.toggled.connect(lambda e: toggle_hide_verticals(self, e))

        # connect actions to buttons
        self.ui.zoom_out_btn.clicked.connect(self.graphToolbar.home)
        self.ui.tight_graph_btn.clicked.connect(lambda e: trigger_tight_layout(self, e))
        self.ui.broadening_btn.clicked.connect(
            lambda _: self.spectrumGraph.applyBroadening(self.p))
        self.ui.broadening_slider.valueChanged.connect(lambda e: trigger_broadening_slider(self, e))
        # self.ui.open_file_btn.clicked.connect(self.trigger_open_file)
        self.ui.spectrum_table.itemSelectionChanged.connect(lambda e: trigger_table_selection(self, e))
        self.ui.spectrums_select.currentIndexChanged.connect(lambda e: trigger_spectrum_select(self, e))
        self.ui.export_graph_btn.clicked.connect(self.trigger_save_figure)
        self.ui.style_btn.clicked.connect(lambda e: trigger_change_style(self))
        self.ui.broadening_inp.textChanged.connect(lambda e: trigger_broadening_text(self, e))
        
        self.style_dialog.line_color_pick.clicked.connect(lambda : trigger_pick_color(self, 'line'))
        self.style_dialog.spike_color_pick.clicked.connect(lambda : trigger_pick_color(self, 'spike'))
        self.style_dialog.marker_color_pick.clicked.connect(lambda : trigger_pick_color(self, 'marker'))

        self.style_dialog.line_shape_select.currentIndexChanged.connect(
            lambda e: trigger_linestyle_change(self, LINESTYLES[e], which='line')
        )
        self.style_dialog.spike_shape_select.currentIndexChanged.connect(
            lambda e: trigger_linestyle_change(self, LINESTYLES[e], which='spike')
        )

        self.ui.close_btn.clicked.connect(self.close)

        self.ui.start_animation_btn.clicked.connect(lambda e: toggle_grid(self))
        self.ui.spectrumTabWidget.currentChanged.connect(lambda e: trigger_tab_change(self, e))

        # actions
        self.openAction.triggered.connect(self.trigger_open_file)
        self.zoomOutAction.triggered.connect(self.graphToolbar.home)
        self.tightFigureLayoutAction.triggered.connect(lambda e: trigger_tight_layout(self, e))
        self.toggleGrid.triggered.connect(lambda e: toggle_grid(self))
        self.toggleBroaden.triggered.connect(lambda e: self.ui.broadening_check.setChecked(not self.ui.broadening_check.isChecked()))
        self.toggleSpikes.triggered.connect(lambda e: self.ui.hide_verticals_check.setChecked(not self.ui.hide_verticals_check.isChecked()))
        self.saveAction.triggered.connect(self.trigger_save_figure)
        self.quitAction.triggered.connect(self.close)

        self.ui.optimization_list.currentRowChanged.connect(self.trigger_optimization_select)
        self.ui.spectrumType.currentIndexChanged.connect(self.trigger_change_spectrum_type)

        self.showEnergiesAction.triggered.connect(self.trigger_energy_dialog)
        self.showOptmAction.triggered.connect(self.trigger_optm_dialog)
        self.showNMRAction.triggered.connect(self.trigger_nmr_dialog)
    
    def trigger_open_file(self):
        filename, _  = QFileDialog.getOpenFileName(self, "Open Gaussian File",  '',"Gaussian files (*.LOG)")
        if filename:
            self.spectrumGraph.ax.cla()
            self.spectrumGraph.draw()
            self.setState(False)
            self.applyLoadedData(filename)
            self.ui.hide_verticals_check.setChecked(False)
            self.spectrumGraph.initStyle()
            self.item_selected = False
            _title = "#"+filename
            self.ui.loaded_file_name.setText(_title)
            self.a_file_loaded = True

            if self.ui.broadening_check.isChecked():
                self.spectrumGraph.applyBroadening(self.p)

    def trigger_save_figure(self):
        if len(self.spectrumGraph.freq) != len(self.spectrumGraph.ints): return

        filename, _ = QFileDialog.getSaveFileName()
        if not filename: return
        if self.ui.hide_verticals_check.isChecked() and not self.ui.broadening_check.isChecked(): return
        fig = save_figure(self)
        fig.savefig(filename.split('.')[0]+'.{}'.format(self.ui.export_formats_select.currentText().lower()))

    def setState(self, state):
        self.ui.broadening_check.setDisabled(state)
        self.ui.spectrum_table.setDisabled(state)
        self.ui.hide_verticals_check.setDisabled(state)
        self.ui.scale_x_check.setDisabled(state)
        self.ui.scale_y_check.setDisabled(state)
        self.ui.scale_curve_check.setDisabled(state)
        self.ui.show_marks_check.setDisabled(state)
        self.ui.show_peaks_check.setDisabled(state)
        self.ui.show_numbers_check.setDisabled(state)
        self.ui.spectrums_select.setDisabled(state)
        self.ui.loaded_file_name.setDisabled(state)
        self.ui.style_btn.setDisabled(state)
        self.ui.export_graph_btn.setDisabled(state)
        self.ui.export_formats_select.setDisabled(state)
        self.ui.zoom_out_btn.setDisabled(state)
        self.ui.tight_graph_btn.setDisabled(state)
        self.ui.start_animation_btn.setDisabled(state)
        self.spectrumGraph.setDisabled(state)
        self.graphToolbar.setDisabled(state)
        self.saveAction.setDisabled(state)
        self.toggleBroaden.setDisabled(state)
        self.toggleSpikes.setDisabled(state)
        self.zoomOutAction.setDisabled(state)
        self.tightFigureLayoutAction.setDisabled(state)
        self.toggleGrid.setDisabled(state)
        self.ui.optimization_list.setDisabled(state)
        self.ui.spectrumType.setDisabled(state)
        self.changeStyleAction.setDisabled(state)
        self.showEnergiesAction.setDisabled(state)
        self.showOptmAction.setDisabled(state)
        self.showNMRAction.setDisabled(state)

    def applyLoadedData(self, filename):
        self.parser: Parser = Parser(filename)
        self.load_and_render()
        
        # apply to table
        self.populateTable(self.parser.freq, self.parser.ir_ints)

        self.populateOptimization()


        self.showNMRAction.setDisabled(not self.parser.load_nmr_spectrum().ok)
        self.showOptmAction.setDisabled(not (len(self.parser.load_optimization_values()[0]) != 0))
        self.showEnergiesAction.setDisabled(not self.parser.load_energies().ok)

        self.spectrumGraph.PlotData(self.parser.freq, self.parser.ir_ints, self.p)

        s = time()
        # apply to graph
        # self.ui.log_file_text.setText("")
        # self.ui.log_file_text.setText("".join(self.parser.lines))

        print('took: ', time()-s)
        
        
    def populateTable(self, freq:np.ndarray, ints:np.ndarray):
        self.ui.spectrum_table.setRowCount(len(freq))
        self.ui.spectrum_table.setColumnCount(2)

        header = ['Frequency', 'IR Intesity']
        self.ui.spectrum_table.setHorizontalHeaderLabels(header)

        for idx, (f, i) in enumerate(zip(freq, ints)):
            self.ui.spectrum_table.setItem(idx, 0, QTableWidgetItem("{:10.4f}".format(f)))
            self.ui.spectrum_table.setItem(idx, 1, QTableWidgetItem("{:10.4f}".format(i)))

    def populateOptimization(self):
        self.ui.optimization_list.clear()

        self.ui.optimization_list.addItems(
            [f" {i+1}\tΔE: {o}" for i, o in enumerate(self.parser.load_optimization_values()[0])]
        )

    def trigger_optimization_select(self, index):
        try:
            selected_optm = self.parser.load_optimized_geometry()[index]

            self.viewer.clear()

            for idx, b in enumerate(self.bonds):
                l = selected_optm[b[0]-1]
                r = selected_optm[b[1]-1]
                plt = gl.GLLinePlotItem(pos=np.array([l.pos, r.pos]), width=5, antialias=False, color="#dcdfe0")
                self.viewer.addItem(plt)
                self.compound_bonds.append(plt)

            for optm_step in selected_optm:
                md = gl.MeshData.sphere(rows=40, cols=40)
                m3 = gl.GLMeshItem(meshdata=md, smooth=False, shader='shaded', color=optm_step.color)
                m3.translate(optm_step.x, optm_step.y, optm_step.z)
                m3.scale(.4, .4, .4)
                self.viewer.addItem(m3)
        except Exception as e:
            print(str(e))


    def trigger_change_spectrum_type(self, index):
        self.p.trans = index == 0

        self.spectrumGraph.ax.cla()
        spectrum_type = "Absorbance ($A = \epsilon c l$)" if index else "Transmittance (T%)"
        self.p.ylabel = spectrum_type

        if not self.ui.hide_verticals_check.isChecked():
            self.spectrumGraph.PlotData(self.spectrumGraph.freq, self.spectrumGraph.ints, self.p)

        if self.ui.broadening_check.isChecked():
            self.spectrumGraph.applyBroadening(self.p)

        self.spectrumGraph.ax.set_xlim(reversed(self.p.xlim))
        self.spectrumGraph.ax.set_xticks(np.arange(-250, 4251, 250))
        self.spectrumGraph.ax.set_ylim([-3, 105])
        self.spectrumGraph.ax.set_title(self.p.title)
        self.spectrumGraph.ax.set_xlabel(self.p.xlabel)
        self.spectrumGraph.ax.set_ylabel(self.p.ylabel)

        self.spectrumGraph.draw()

    def trigger_energy_dialog(self):
        self.energy_dialog = EnergyDialog()
        self.energy_dialog.energies_table.clearContents()

        en = self.parser.load_energies()
        header = self.energy_dialog.energies_table.horizontalHeader()

        
        for j, en_typ in enumerate([en.au, en.Kcal_mol, en.KJ_mol, en.eV]):
            for i, e in enumerate(en_typ):
                self.energy_dialog.energies_table.setItem(i, j, QTableWidgetItem("{:.5f}".format(e)))
            header.setSectionResizeMode(j, QHeaderView.ResizeToContents)

            
        self.energy_dialog.show()

    def trigger_optm_dialog(self):
        self.optms = np.vstack(self.parser.load_optimization_values())

        self.optm_dialog = OptimizationDialog(data=self.optms)

        self.optm_dialog.export_csv.clicked.connect(self.trigger_export_optm_data)

        tb = self.optm_dialog.data_table
        tb.clearContents()

        header = tb.horizontalHeader()


        tb.setRowCount(self.optms.shape[1])
        tb.setColumnCount(self.optms.shape[0])

        tb.setHorizontalHeaderLabels([' ΔE ', ' RMS Force ', " RMS Displ ", " Max Force ", " Max Displ "])

        for j, col in enumerate(self.optms):
            for i, val in enumerate(col):
                tb.setItem(i, j, QTableWidgetItem("{:.5f}".format(val)))
            header.setSectionResizeMode(j, QHeaderView.ResizeToContents)

        self.optm_dialog.show()

    def trigger_nmr_dialog(self):
        nmr_spectrum = self.parser.load_nmr_spectrum()

        self.nmr_data = nmr_spectrum.spectrum_data
        self.nmr_data = sorted(self.nmr_data, key=lambda e: e[0])

        x, y = nmr_spectrum.compute_continous_spectrum()

        self.nmr_dialog = NMRDialog(x=x, y=y, sheilding=nmr_spectrum.sheilding, deg=nmr_spectrum.deg)
        self.nmr_dialog.export_btn.clicked.connect(self.trigger_export_nmr_data)

        tb = self.nmr_dialog.data_table
        tb.clearContents()

        header = tb.horizontalHeader()

        tb.setRowCount(len(self.nmr_data))
        tb.setColumnCount(len(self.nmr_data[0]))

        tb.setHorizontalHeaderLabels([' Index ', " Atom ", " Sheilding ", " Desheilding ", " Degeneracy "])

        for i, row in enumerate(self.nmr_data):
            for j, val in enumerate(row):
                tb.setItem(i, j, QTableWidgetItem(str(val)))
                header.setSectionResizeMode(j, QHeaderView.ResizeToContents)
        
        self.nmr_dialog.show()

    def trigger_export_optm_data(self):
        filename, _ = QFileDialog.getSaveFileName(filter="*.csv")
        if not filename: return
        convert_to_csv(['E ', 'RMS Force', "RMS Displ", "Max Force", "Max Displ"], filename, self.optms.reshape(-1, 5).round(6))

    def trigger_export_nmr_data(self):
        filename, _ = QFileDialog.getSaveFileName(filter="*.csv")
        if not filename: return
        convert_to_csv(filename, ['Index', 'Atom', "Sheidling", "Desheilding", "Degeneracy"], self.nmr_data)

    def trigger_show_spectrum(self, x, y, sheilding, deg):
        fig, ax = plt.subplots(nrows=1, figsize=(10, 4))
        ax.vlines(sheilding, ymin=0, ymax=deg, color='k', lw=1)
        ax.plot(x, y, color='#FF0000', ls='-')

        ax.set_xlabel('Sheilding (ppm)', fontsize=14)
        ax.set_ylabel('Degenaracy', fontsize=14)
        ax.set_title("NMR Spectrum", fontsize=15)

        fig.tight_layout()

        fig.show()


    def load_and_render(self):

        self.viewer.clear()
        self.grid_toggled = False
        self.compound = []
        self.compound_bonds = []

        self.viewer.setBackgroundColor("#333333")
        self.viewer.setCameraPosition(distance=25)

        geom_tables = np.array(self.parser.get_position_table())

        struct1 = geom_tables[0]

        self.bonds = self.parser.load_geometry_table()

        for idx, b in enumerate(self.bonds):
            l = struct1[b[0]-1]
            r = struct1[b[1]-1]
            plt = gl.GLLinePlotItem(pos=np.array([l.pos, r.pos]), width=5, antialias=False, color="#dcdfe0")
            self.viewer.addItem(plt)
            self.compound_bonds.append(plt)

        for atom in struct1:
            md = gl.MeshData.sphere(rows=40, cols=40)
            m3 = gl.GLMeshItem(meshdata=md, smooth=False, shader='shaded', color=atom.color)
            m3.translate(atom.x, atom.y, atom.z)
            m3.scale(.4, .4, .4)
            self.viewer.addItem(m3)
            self.compound.append(m3)
            self.original_compound.append(atom)


    @staticmethod
    def generate_broadening_for_export(sigma, freq, ints):
        x= np.linspace(-250, 4100, num=1000, endpoint=True)

        gInts = []
        for Fi in x:
            gI = np.sum(ints*np.exp(-((((freq-Fi)/sigma)**2))))
            gInts.append(gI)
        
        gInts = np.array(gInts)

        return x, gInts

    @staticmethod
    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)

    def closeEvent(self, event):
        if not self.a_file_loaded: return super().closeEvent(event)

        reply = QMessageBox.question(self, 'Quit!', "Save changes?",
                                     QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                     QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.trigger_save_figure()
            event.accept()
        elif reply == QMessageBox.No:
            event.accept()
            if self.optm_dialog: self.optm_dialog.close()
            if self.energy_dialog: self.energy_dialog.close()
            if self.nmr_dialog: self.nmr_dialog.close()
        elif reply == QMessageBox.Cancel:
            event.ignore()
        else:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sp = SpectrumAnalyzer()
    sys.exit(app.exec_())