import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib import pyplot

from ui.ui_main import Ui_SpectrumAnalyzer
from ui.ui_style import Ui_StyleDialog
from spectrum_graph import SpectrumGraph, Toolbar
from gaussian_parser import Parser
from consts import EXPORT_FORMATS, LINESTYLES

import numpy as np


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
        self.setWindowIcon(QIcon("icons/spectrum-icon.jpg"))
        self.setWindowTitle("Spectrum Analyzer")
        self.resize(1280, 750)

        self.item_selected = False

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

        # add spectrum graph to it's frame
        self.ui.spectrum_frame_layout.addWidget(self.graphToolbar)
        self.ui.spectrum_frame_layout.addWidget(self.spectrumGraph)
        self.ui.export_formats_select.addItems(EXPORT_FORMATS)
        self.style_dialog.line_shape_select.addItems(LINESTYLES)

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
            lambda _: self.spectrumGraph.applyBroadening(
                float(self.ui.broadening_inp.text())
            )
        )
        self.ui.broadening_slider.valueChanged.connect(self.trigger_broadening_slider)
        self.ui.open_file_btn.clicked.connect(self.trigger_open_file)
        self.ui.spectrum_table.itemSelectionChanged.connect(self.trigger_table_selection)
        self.ui.spectrums_select.currentIndexChanged.connect(self.trigger_spectrum_select)
        self.ui.export_graph_btn.clicked.connect(
            lambda e:self.trigger_save_figure(self.ui.export_formats_select.currentText().lower())
        )
        self.ui.style_btn.clicked.connect(self.trigger_change_style)

    # togglers
    def toggle_broadening(self, state):
        
        self.ui.broadening_btn.setDisabled(not state)
        self.ui.broadening_inp.setDisabled(not state)
        self.ui.broadening_slider.setDisabled(not state)
        self.ui.broadening_select.setDisabled(not state)
        self.ui.label.setDisabled(not state)
        if not state:
            self.spectrumGraph.removeBroadening()
            return
        self.spectrumGraph.applyBroadening()
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
        self.spectrumGraph.togglePeaks(state)

    def trigger_tight_layout(self):
        self.spectrumGraph.fig.tight_layout()
        self.spectrumGraph.draw()

    def trigger_broadening_slider(self, broad):
        self.spectrumGraph.applyBroadening(broad)
        self.ui.broadening_inp.setText(str(broad))

    def trigger_spectrum_select(self, index):
        
        self.spectrumGraph.ax.cla()
        self.spectrumGraph.initStyle()
        self.ui.hide_verticals_check.setChecked(False)

        if index == 1:
            self.spectrumGraph.PlotData(self.freq, self.raman_ints)
            self.populateTable(self.freq, self.raman_ints)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Raman Intensities'])
            self.spectrumGraph.fig.suptitle('Raman Spectrum of #', fontsize=14)
        elif index == 0:
            self.spectrumGraph.PlotData(self.freq, self.ir_ints)
            self.populateTable(self.freq, self.ir_ints)
            self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'IR Intensities'])
            self.spectrumGraph.fig.suptitle('IR Spectrum of #', fontsize=14)
        
        if self.ui.broadening_check.isChecked():
            self.spectrumGraph.applyBroadening(self.ui.broadening_slider.value())

        self.spectrumGraph.draw()

    def trigger_table_selection(self):
        idx = self.ui.spectrum_table.selectedIndexes()[-1].row()
        x, y = self.spectrumGraph.freq[idx], self.spectrumGraph.ints[idx]
        self.ui.intensity_label.setText(str((round(x, 3), round(y, 3))))
    
    def trigger_open_file(self):
        filename, _  = QFileDialog.getOpenFileName(self, "Open Gaussian File",  './data/',"Gaussian files (*.LOG)")
        if filename:
            self.spectrumGraph.ax.cla()
            self.spectrumGraph.draw()
            self.applyLoadedData(filename)
            self.setState(False)
            self.ui.hide_verticals_check.setChecked(False)
            self.spectrumGraph.initStyle()
            self.item_selected = False
            _title = "#"+filename.split('/')[-1]
            self.ui.loaded_file_name.setText(_title)

            if self.ui.broadening_check.isChecked():
                self.spectrumGraph.applyBroadening(self.ui.broadening_slider.value())


    def trigger_save_figure(self, ext:str):
        if len(self.spectrumGraph.freq) != len(self.spectrumGraph.ints): return

        filename, _ = QFileDialog.getSaveFileName()
        if not filename: return
        if self.ui.hide_verticals_check.isChecked() and not self.ui.broadening_check.isChecked(): return
        
        fig, ax = pyplot.subplots(
            nrows=1, figsize=(
                self.style_dialog.figure_width.value(),
                self.style_dialog.figure_height.value(),
            )
        )
        fig.subplots_adjust(
            top=self.style_dialog.padding_top.value(),
            bottom=self.style_dialog.padding_bottom.value(),
            left=self.style_dialog.padding_left.value(),
            right=self.style_dialog.padding_right.value(),
        )

        if not self.ui.hide_verticals_check.isChecked():
            ax.vlines(
                self.spectrumGraph.freq, ymin=0, ymax=self.spectrumGraph.ints,
                colors='k', label='Intensity peaks' 
            )
        if self.ui.broadening_check.isChecked():
            x, gInts = self.generate_broadening_for_export(
                self.ui.broadening_slider.value(),
                self.spectrumGraph.freq,
                self.spectrumGraph.ints
            )
            ax.plot(
                x, gInts, color='#555555', 
                linewidth=self.style_dialog.linewidth_inp.value(), 
                linestyle=self.style_dialog.line_shape_select.currentText(),
                label='Gaussian Broaden'
            )

        ax.set_xlim([self.style_dialog.xlim_min.value(), self.style_dialog.xlim_max.value()])
        ax.set_ylim([self.style_dialog.ylim_min.value(), self.style_dialog.ylim_max.value()])
        ax.set_xticks(np.arange(-250, 4001, 250), fontsize=14)
        ax.set_yticks(np.arange(0, 101, 10), fontsize=self.style_dialog.fontsize_inp.value())
        ax.set_xlabel(self.style_dialog.xlabel_inp.text()+" $cm^{-1}$", fontsize=self.style_dialog.fontsize_inp.value())
        ax.set_ylabel(self.style_dialog.ylabel_inp.text()+' $\epsilon (M^{-1}\, cm^{-1})$', fontsize=self.style_dialog.fontsize_inp.value())
        ax.set_title(self.style_dialog.title_inp.text(), fontsize=self.style_dialog.fontsize_inp.value()+2)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        leg = ax.legend(loc='best', frameon=False, fontsize=self.style_dialog.fontsize_inp.value())

        fig.tight_layout()
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
        self.spectrumGraph.fig.suptitle(self.style_dialog.title_inp.text())
        self.spectrumGraph.ax.set_xlabel(self.style_dialog.xlabel_inp.text())
        self.spectrumGraph.ax.set_ylabel(self.style_dialog.ylabel_inp.text())
        self.spectrumGraph.ax.set_xlim(
            (self.style_dialog.xlim_min.value(), self.style_dialog.xlim_max.value())
        )
        self.spectrumGraph.ax.set_ylim(
            (self.style_dialog.ylim_min.value(), self.style_dialog.ylim_max.value())
        )
        self.spectrumGraph.draw()

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

    def load_ir_data(self, filename=None):
        p = Parser(filename)
        freq = np.array(p.freq)
        ir_ints = np.array(p.ir_ints)
        raman_ints = np.array(p.raman_ints)

        if len(ir_ints) > 0:
            ir_ints = (ir_ints/ir_ints.max())*100
        if len(raman_ints) > 0:
            raman_ints = (raman_ints/raman_ints.max())*100

        return freq, ir_ints, raman_ints

    def applyLoadedData(self, filename):
        self.freq, self.ir_ints, self.raman_ints = self.load_ir_data(filename)

        # apply to table
        self.populateTable(self.freq, self.ir_ints)

        # apply to graph
        self.spectrumGraph.PlotData(self.freq, self.ir_ints)
        

    def populateTable(self, freq:np.ndarray, ints:np.ndarray):
        self.ui.spectrum_table.setRowCount(len(freq))
        self.ui.spectrum_table.setColumnCount(2)

        header = ['Frequency', 'IR Intesity']
        self.ui.spectrum_table.setHorizontalHeaderLabels(header)

        for idx, (f, i) in enumerate(zip(freq, ints)):
            self.ui.spectrum_table.setItem(idx, 0, QTableWidgetItem("{:10.4f}".format(f)))
            self.ui.spectrum_table.setItem(idx, 1, QTableWidgetItem("{:10.4f}".format(i)))

    
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    win = SpectrumAnalyzer()
    sys.exit(app.exec())
