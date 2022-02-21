
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from ui.ui_main import Ui_SpectrumAnalyzer
from ui.ui_style import Ui_StyleDialog

from matplotlib import pyplot
from spectrum_graph import Properties, SpectrumGraph, Toolbar
from gaussian_parser import Parser, get_position_table, load_geometry_table
from consts import EXPORT_FORMATS, LINESTYLES, PATHS

import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import json


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class StyleDialog(QDialog, Ui_StyleDialog):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.setupUi(self)
        self.setWindowTitle('Change Graph Style')


class SpectrumAnalyzer(QDialog):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

        self.ui = Ui_SpectrumAnalyzer()
        self.ui.setupUi(self)
        self.setWindowFlags(
            Qt.WindowCloseButtonHint | 
            Qt.WindowMaximizeButtonHint | 
            Qt.WindowMinimizeButtonHint
        )
        self.setWindowIcon(QIcon(os.path.join(BASE_DIR, PATHS['icons'] ,"spectrum-icon.png")))
        self.setWindowTitle("GSA Gaussian Spectrum Analyzer")
        self.resize(1280, 750)

        self.item_selected = False
        self.a_file_loaded = False

        self.p = Properties()

        self.x_signals = []
        self.y_signals = []

        # init Ui Components
        self.uiComponents()

        # init Ui
        self.initUi()

        # init Actions
        self.initActions()

        self.show()

    def uiComponents(self):
        self.spectrumGraph = SpectrumGraph()

        self.viewer = gl.GLViewWidget()
        
        self.graphToolbar = Toolbar(self.spectrumGraph, self.ui.spectrumFrame)
        self.style_dialog = StyleDialog()
        self.style_dialog.setModal(True)
        self.style_dialog.ok_btn.clicked.connect(lambda: self.trigger_style_button('OK'))
        self.style_dialog.apply_btn.clicked.connect(lambda: self.trigger_style_button('Apply'))
        self.style_dialog.cancel_btn.clicked.connect(lambda: self.trigger_style_button('Cancel'))


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

        self.viewer.setWindowTitle('STL Viewer')
        self.viewer.setCameraPosition(distance=25)
        self.ui.renderLayout.addWidget(self.viewer)


    def initActions(self):
        self.ui.broadening_check.toggled.connect(self.toggle_broadening)
        self.ui.scale_curve_check.toggled.connect(self.toggle_scale_curve)
        self.ui.scale_x_check.toggled.connect(self.toggle_scale_x)
        self.ui.scale_y_check.toggled.connect(self.toggle_scale_y)
        self.ui.show_peaks_check.toggled.connect(self.toggle_peaks)
        self.ui.show_marks_check.toggled.connect(self.toggle_marks)
        self.ui.hide_verticals_check.toggled.connect(self.toggle_hide_verticals)

        # connect actions to buttons
        self.ui.zoom_out_btn.clicked.connect(self.graphToolbar.home)
        self.ui.tight_graph_btn.clicked.connect(self.trigger_tight_layout)
        self.ui.broadening_btn.clicked.connect(
            lambda _: self.spectrumGraph.applyBroadening(self.p)
        )
        self.ui.broadening_slider.valueChanged.connect(self.trigger_broadening_slider)
        self.ui.open_file_btn.clicked.connect(self.trigger_open_file)
        self.ui.spectrum_table.itemSelectionChanged.connect(self.trigger_table_selection)
        self.ui.spectrums_select.currentIndexChanged.connect(self.trigger_spectrum_select)
        self.ui.export_graph_btn.clicked.connect(self.trigger_save_figure)
        self.ui.style_btn.clicked.connect(self.trigger_change_style)
        self.ui.broadening_inp.textChanged.connect(self.trigger_broadening_text)
        
        self.style_dialog.line_color_pick.clicked.connect(lambda : self.trigger_pick_color('line'))
        self.style_dialog.spike_color_pick.clicked.connect(lambda : self.trigger_pick_color('spike'))
        self.style_dialog.marker_color_pick.clicked.connect(lambda : self.trigger_pick_color('marker'))

        self.style_dialog.line_shape_select.currentIndexChanged.connect(
            lambda e: self.trigger_linestyle_change(LINESTYLES[e], which='line')
        )
        self.style_dialog.spike_shape_select.currentIndexChanged.connect(
            lambda e: self.trigger_linestyle_change(LINESTYLES[e], which='spike')
        )
        # self.ui.render_btn.clicked.connect(lambda: self.ui.spectrumStackedWidget.setCurrentIndex(1))
        # self.ui.spectrum_btn.clicked.connect(lambda: self.ui.spectrumStackedWidget.setCurrentIndex(0))

        self.ui.close_btn.clicked.connect(self.close)

    # togglers
    def toggle_broadening(self, state):
        self.ui.broadening_btn.setDisabled(not state)
        self.ui.broadening_inp.setDisabled(not state)
        self.ui.broadening_slider.setDisabled(not state)
        self.ui.broadening_select.setDisabled(not state)
        self.ui.label.setDisabled(not state)

        if not state:
            self.spectrumGraph.removeBroadening(self.p)
            self.spectrumGraph.draw()
            return
        else:
            self.spectrumGraph.applyBroadening(self.p)
            self.spectrumGraph.draw()
            return

        self.ui.broadening_inp.setText(str(self.ui.broadening_slider.value()))

    def toggle_scale_curve(self, state):
        self.ui.scale_curve_inp.setDisabled(not state)
        self.ui.scale_curve_btn.setDisabled(not state)

    def toggle_peaks(self, state):
        self.ui.peaks_select.setDisabled(not state)

    def toggle_marks(self, state):
        self.ui.marks_select.setDisabled(not state)

    def toggle_scale_x(self, state):
        self.ui.scale_x_inp.setDisabled(not state)
        self.ui.scale_x_btn.setDisabled(not state)

    def toggle_scale_y(self, state):
        self.ui.scale_y_inp.setDisabled(not state)
        self.ui.scale_y_btn.setDisabled(not state)

    def toggle_hide_verticals(self, state):
        self.spectrumGraph.togglePeaks(state, self.p.spikes_color)

    def trigger_tight_layout(self):
        self.spectrumGraph.fig.tight_layout()
        self.spectrumGraph.draw()

    def trigger_broadening_slider(self, broad):
        self.p.broaden_sigma = broad
        self.spectrumGraph.applyBroadening(self.p)

    def trigger_broadening_text(self, sigma):
        try:
            sigma = float(sigma)
            self.p.broaden_sigma = sigma
            self.spectrumGraph.applyBroadening(self.p)
            # self.ui.broadening_slider.setValue(sigma)
        except Exception as e: 
            print(str(e))

    def trigger_spectrum_select(self, index):
        
        self.spectrumGraph.ax.cla()
        self.spectrumGraph.initStyle()
        self.ui.hide_verticals_check.setChecked(False)

        if index == 0:
            self.spectrumGraph.PlotData(self.parser.freq, self.parser.ir_ints)
            self.populateTable(self.parser.freq, self.parser.ir_ints)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'IR Intensities'])
            self.spectrumGraph.fig.suptitle('IR Spectrum of #', fontsize=14)
            # self.p.ylim = (self.parser.ir_ints.min(), self.parser.ir_ints.max())
        
        elif index == 1:
            self.spectrumGraph.PlotData(self.parser.freq, self.parser.raman_ints)
            self.populateTable(self.parser.freq, self.parser.raman_ints)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Raman Intensities'])
            self.spectrumGraph.fig.suptitle('Raman Spectrum of #', fontsize=14)
            # self.p.ylim = (self.parser.raman_ints.min(), self.parser.raman_ints.max())

        elif index == 2:
            self.spectrumGraph.PlotData(self.parser.freq, self.parser.frc_consts)
            self.populateTable(self.parser.freq, self.parser.frc_consts)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'FRC Consts'])
            self.spectrumGraph.fig.suptitle('FRC consts of #', fontsize=14)
            # self.p.ylim = (self.parser.frc_consts.min(), self.parser.frc_consts.max())

        elif index == 3:
            self.spectrumGraph.PlotData(self.parser.freq, self.parser.red_masses)
            self.populateTable(self.parser.freq, self.parser.red_masses)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Red Masses'])
            self.spectrumGraph.fig.suptitle('Red Masses of #', fontsize=14)
            # self.p.ylim = (self.parser.red_masses.min(), self.parser.red_masses.max())
        
        elif index == 4:
            self.spectrumGraph.PlotData(self.parser.freq, self.parser.depolar_p)
            self.populateTable(self.parser.freq, self.parser.depolar_p)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Depolar (P)'])
            self.spectrumGraph.fig.suptitle('Depolar (P) of #', fontsize=14)
            # self.p.ylim = (self.parser.depolar_p.min(), self.parser.depolar_p.max())
        
        elif index == 5:
            self.spectrumGraph.PlotData(self.parser.freq, self.parser.depolar_u)
            self.populateTable(self.parser.freq, self.parser.depolar_u)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Depolar (U)'])
            self.spectrumGraph.fig.suptitle('Depolar (U) of #', fontsize=14)
            # self.p.ylim = (self.parser.depolar_u.min(), self.parser.depolar_u.max())

        elif index == 6:
            deg = np.ones(self.parser.nmr_sheilding.shape[0])
            self.spectrumGraph.PlotData(self.parser.nmr_sheilding, deg)
            self.populateTable(self.parser.nmr_sheilding, deg)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Sheilding', 'Degeneracy'])
            self.spectrumGraph.fig.suptitle('NMR Spectrum of #', fontsize=14)
            # self.p.ylim = (self.parser.depolar_u.min(), self.parser.depolar_u.max())
        
        elif index == 7:
            deg = np.ones(self.parser.uv_spectrum.shape[0])
            self.spectrumGraph.PlotData(self.parser.uv_spectrum, deg)
            self.populateTable(self.parser.uv_spectrum, deg)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['UV Vis Wavelength', 'Degeneracy'])
            self.spectrumGraph.fig.suptitle('UV Vis Spectrum of #', fontsize=14)
            # self.p.ylim = (self.parser.depolar_u.min(), self.parser.depolar_u.max())

        if self.ui.broadening_check.isChecked():
            self.spectrumGraph.applyBroadening(self.p)

        self.spectrumGraph.draw()

    def trigger_table_selection(self):
        idx = self.ui.spectrum_table.selectedIndexes()[-1].row()
        x, y = self.spectrumGraph.freq[idx], self.spectrumGraph.ints[idx]
        self.ui.intensity_label.setText(str((round(x, 3), round(y, 3))))
    
    def trigger_open_file(self):
        filename, _  = QFileDialog.getOpenFileName(self, "Open Gaussian File",  '',"Gaussian files (*.LOG)")
        if filename:
            self.spectrumGraph.ax.cla()
            self.spectrumGraph.draw()
            self.applyLoadedData(filename)
            self.setState(False)
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
        
        fig, ax = pyplot.subplots(
            nrows=1, figsize=(
                self.p.figure_width,
                self.p.figure_height,
            )
        )
        fig.subplots_adjust(
            top=self.p.padding_top,
            bottom=self.p.padding_bottom,
            left=self.p.padding_left,
            right=self.p.padding_right,
        )

        if not self.ui.hide_verticals_check.isChecked():
            ax.vlines(
                self.spectrumGraph.freq, ymin=0, ymax=self.spectrumGraph.ints,
                colors=self.p.spikes_color, label='Intensity peaks' 
            )
        if self.ui.broadening_check.isChecked():
            x, gInts = self.generate_broadening_for_export(
                self.ui.broadening_slider.value(),
                self.spectrumGraph.freq,
                self.spectrumGraph.ints
            )
            ax.plot(
                x, gInts, color=self.p.broaden_color, 
                linewidth=self.p.broaden_width, 
                linestyle=self.p.broaden_style,
                label='Gaussian Broaden'
            )

        ax.set_xlim(self.p.xlim)
        ax.set_ylim(self.p.ylim)
        ax.set_xticks(np.arange(-250, 4001, 250), fontsize=14)
        ax.set_yticks(np.arange(0, 101, 10), fontsize=self.style_dialog.fontsize_inp.value())
        ax.set_xlabel(self.style_dialog.xlabel_inp.text(), fontsize=self.style_dialog.fontsize_inp.value())
        ax.set_ylabel(self.style_dialog.ylabel_inp.text(), fontsize=self.style_dialog.fontsize_inp.value())
        ax.set_title(self.style_dialog.title_inp.text(), fontsize=self.style_dialog.fontsize_inp.value()+2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        leg = ax.legend(loc='best', frameon=False, fontsize=self.style_dialog.fontsize_inp.value())

        # fig.tight_layout()
        fig.savefig(filename.split('.')[0]+'.{}'.format(self.ui.export_formats_select.currentText().lower()))

    def trigger_change_style(self):
        self.style_dialog.exec()

    def trigger_style_button(self, e):
        if e == 'Cancel':
            self.style_dialog.close()
        elif e == 'OK':
            self.trigger_apply_changes()
            self.style_dialog.close()
        elif e == 'Apply':
            self.trigger_apply_changes()

    # trigger style changes
    def trigger_apply_changes(self):
        sd = self.style_dialog

        self.p.figure_width = sd.figure_width.value()
        self.p.figure_height = sd.figure_height.value()
        
        self.p.padding_top    = sd.padding_top.value()
        self.p.padding_bottom = sd.padding_bottom.value()
        self.p.padding_left   = sd.padding_left.value()
        self.p.padding_right  = sd.padding_right.value()

        self.p.broaden_width = sd.linewidth_inp.value()
        self.p.broaden_style = sd.line_shape_select.currentText()
        self.p.broaden_sigma = self.ui.broadening_slider.value()

        self.p.spikes_width = sd.spike_width.value()
        self.p.spikes_style = sd.spike_shape_select.currentText()

        self.p.title = sd.title_inp.text()
        self.p.xlabel = sd.xlabel_inp.text()
        self.p.ylabel = sd.ylabel_inp.text()

        self.p.xlim = sd.xlim_min.value(), sd.xlim_max.value()
        self.p.ylim = sd.ylim_min.value(), sd.ylim_max.value()

        self.spectrumGraph.fig.subplots_adjust(
            top=self.p.padding_top,
            bottom=self.p.padding_bottom,
            left=self.p.padding_left,
            right=self.p.padding_right,
        )

        self.spectrumGraph.fig.suptitle(self.p.title)
        self.spectrumGraph.ax.set_xlabel(self.p.xlabel)
        self.spectrumGraph.ax.set_ylabel(self.p.ylabel)
        
        self.spectrumGraph.ax.set_xlim(self.p.xlim)
        self.spectrumGraph.ax.set_ylim(self.p.ylim)

        if not self.ui.hide_verticals_check.isChecked():
            self.spectrumGraph.peaks_plot.set_lw(self.p.spikes_width)
            self.spectrumGraph.peaks_plot.set_ls(self.p.spikes_style)
            self.spectrumGraph.peaks_plot.set_color(self.p.spikes_color)

        if self.spectrumGraph._broaden:
            self.spectrumGraph._broaden[0].set_lw(self.p.broaden_width)
            self.spectrumGraph._broaden[0].set_ls(self.p.broaden_style)
            self.spectrumGraph._broaden[0].set_color(self.p.broaden_color)
        self.spectrumGraph.fig.tight_layout()
        self.spectrumGraph.draw()

    def trigger_pick_color(self, which):
        color = QColorDialog(self).getColor()
        r, g, b, a = color.getRgb()
        back_color = "background-color: rgb({}, {}, {})".format(r, g, b)
        hex_color = self.rgb2hex(r, g, b)
        
        if which == 'line':
            self.p.broaden_color = hex_color
            self.style_dialog.line_color_pick.setStyleSheet(back_color)

        elif which == 'spike':
            self.p.spikes_color = hex_color
            self.style_dialog.spike_color_pick.setStyleSheet(back_color)

        elif which == 'marker':
            self.p.marker_color = hex_color
            self.style_dialog.marker_color_pick.setStyleSheet(back_color)
        else:
            return

    def trigger_linestyle_change(self, ls, which):
        if which == 'line':
            if self.spectrumGraph._broaden:
                self.spectrumGraph._broaden[0].set_linestyle(ls)
        elif which == 'spike':
            self.spectrumGraph.peaks_plot.set_linestyles(ls)

    def trigger_change_page(self):
        current_index = self.ui.spectrumStackedWidget.currentIndex()

        if current_index == 0:
            self.ui.render_btn.setText('3D Render')
            self.ui.render_btn.clicked.connect(lambda: self.ui.spectrumStackedWidget.setCurrentIndex(1))
        elif current_index == 1:
            self.ui.render_btn.setText('Spectrum Graph')
            self.ui.render_btn.clicked.connect(lambda: self.ui.spectrumStackedWidget.setCurrentIndex(0))
        

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
        self.spectrumGraph.setDisabled(state)
        self.graphToolbar.setDisabled(state)


    def load_ir_data(self, filename=None):
        self.parser: Parser = Parser(filename)

    def applyLoadedData(self, filename):
        self.load_ir_data(filename)
        self.load_and_render(filename)
        
        # apply to table
        self.populateTable(self.parser.freq, self.parser.ir_ints)

        # apply to graph
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.ir_ints)
        
    def populateTable(self, freq:np.ndarray, ints:np.ndarray):
        self.ui.spectrum_table.setRowCount(len(freq))
        self.ui.spectrum_table.setColumnCount(2)

        header = ['Frequency', 'IR Intesity']
        self.ui.spectrum_table.setHorizontalHeaderLabels(header)

        for idx, (f, i) in enumerate(zip(freq, ints)):
            # self.ui.spectrum_table.setItem(idx, 0, QTableWidgetItem(idx+1))
            self.ui.spectrum_table.setItem(idx, 0, QTableWidgetItem("{:10.4f}".format(f)))
            self.ui.spectrum_table.setItem(idx, 1, QTableWidgetItem("{:10.4f}".format(i)))


    def load_and_render(self, filename):

        self.viewer.clear()

        self.viewer.setBackgroundColor("#292929")

        with open(filename) as f:
            data = f.readlines()

        geom_tables = np.array(get_position_table(data))

        struct1 = geom_tables[0]
        json_objects = {}
        atoms_list = [atm.get_object() for atm in struct1]
        bonds = load_geometry_table(data)
        
        # json_objects['atoms'] = atoms_list
        # json_objects['bonds'] = bonds

        # with open('compound.json', 'w') as w:
        #     json.dump(json_objects, w, indent=4)
        
        
        for idx, b in enumerate(bonds):
            l = struct1[b[0]-1]
            r = struct1[b[1]-1]

            plt = gl.GLLinePlotItem(pos=np.array([l.pos, r.pos]), width=5, antialias=True)
            self.viewer.addItem(plt)


        for atom in struct1:
            md = gl.MeshData.sphere(rows=50, cols=50)
            m3 = gl.GLMeshItem(meshdata=md, smooth=False, shader='shaded', color=atom.color)
            m3.translate(atom.x, atom.y, atom.z)
            m3.scale(.4, .4, .4)
            self.viewer.addItem(m3)

            # txtitem2 = gl.GLTextItem()
            # txtitem2.setData(pos=(atom.x, atom.y, atom.z), color=(255, 0, 0, 255), text=str(int(atom.index)))
            # self.viewer.addItem(txtitem2)

    @staticmethod
    def generate_broadening_for_export(sigma, freq, ints):
        x= np.linspace(-250, 4100, num=1000, endpoint=True)

        gInts = []
        for Fi in x:
            gI = np.sum(ints*np.exp(-((((freq-Fi)/sigma)**2))))
            gInts.append(gI)
        
        gInts = np.array(gInts)
        gInts = (gInts/gInts.max())*100

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
        elif reply == QMessageBox.Cancel:
            event.ignore()
        else:
            pass
