import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from matplotlib import pyplot

from ui.ui_main import Ui_SpectrumAnalyzer
from ui.ui_style import Ui_StyleDialog
from spectrum_graph import Properties, SpectrumGraph, Toolbar
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
        self.setMinimumSize(1280, 750)
        self.resize(1280, 750)

        self.item_selected = False

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
        self.style_dialog.spike_shape_select.addItems(LINESTYLES)

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
                self.p,
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

        self.style_dialog.line_color_pick.clicked.connect(lambda : self.trigger_pick_color('line'))
        self.style_dialog.spike_color_pick.clicked.connect(lambda : self.trigger_pick_color('spike'))
        self.style_dialog.marker_color_pick.clicked.connect(lambda : self.trigger_pick_color('marker'))

        self.style_dialog.line_shape_select.currentIndexChanged.connect(
            lambda e: self.trigger_linestyle_change(LINESTYLES[e], which='line')
        )
        self.style_dialog.spike_shape_select.currentIndexChanged.connect(
            lambda e: self.trigger_linestyle_change(LINESTYLES[e], which='spike')
        )

    # togglers
    def toggle_broadening(self, state):
        self.ui.broadening_btn.setDisabled(not state)
        self.ui.broadening_inp.setDisabled(not state)
        self.ui.broadening_slider.setDisabled(not state)
        self.ui.broadening_select.setDisabled(not state)
        self.ui.label.setDisabled(not state)

        if not self.spectrumGraph._broaden:
            self.spectrumGraph.applyBroadening(self.p, self.ui.broadening_slider.value())

        if not state:
            self.spectrumGraph.removeBroadening(self.p)
        else:
            self.spectrumGraph.applyBroadening(self.p)
        self.spectrumGraph.draw()

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
        self.spectrumGraph.applyBroadening(self.p, broad)
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
            self.spectrumGraph.applyBroadening(self.p, self.ui.broadening_slider.value())

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
            _title = "#"+filename
            self.ui.loaded_file_name.setText(_title)

            if self.ui.broadening_check.isChecked():
                self.spectrumGraph.applyBroadening(self.p, self.ui.broadening_slider.value())

    def trigger_save_figure(self, ext:str):
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

    @staticmethod
    def rgb2hex(r,g,b):
        return "#{:02x}{:02x}{:02x}".format(r,g,b)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Windows')
    win = SpectrumAnalyzer()
    sys.exit(app.exec())
