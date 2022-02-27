
import importlib
from time import time


def trigger_tight_layout(self, e):
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
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.ir_ints, self.p)
        self.populateTable(self.parser.freq, self.parser.ir_ints)
        self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'IR Intensities'])
        self.spectrumGraph.ax.set_title('IR Spectrum of #', fontsize=14)
        # self.p.ylim = (self.parser.ir_ints.min(), self.parser.ir_ints.max())
    
    elif index == 1:
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.raman_ints, self.p)
        self.populateTable(self.parser.freq, self.parser.raman_ints)
        self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Raman Intensities'])
        self.spectrumGraph.ax.set_title('Raman Spectrum of #', fontsize=14)
        # self.p.ylim = (self.parser.raman_ints.min(), self.parser.raman_ints.max())

    elif index == 2:
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.frc_consts, self.p)
        self.populateTable(self.parser.freq, self.parser.frc_consts)
        self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'FRC Consts'])
        self.spectrumGraph.ax.set_title('FRC consts of #', fontsize=14)
        # self.p.ylim = (self.parser.frc_consts.min(), self.parser.frc_consts.max())

    elif index == 3:
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.red_masses, self.p)
        self.populateTable(self.parser.freq, self.parser.red_masses)
        self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Red Masses'])
        self.spectrumGraph.ax.set_title('Red Masses of #', fontsize=14)
        # self.p.ylim = (self.parser.red_masses.min(), self.parser.red_masses.max())
    
    elif index == 4:
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.depolar_p, self.p)
        self.populateTable(self.parser.freq, self.parser.depolar_p)
        self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Depolar (P)'])
        self.spectrumGraph.ax.set_title('Depolar (P) of #', fontsize=14)
        # self.p.ylim = (self.parser.depolar_p.min(), self.parser.depolar_p.max())
    
    elif index == 5:
        self.spectrumGraph.PlotData(self.parser.freq, self.parser.depolar_u, self.p)
        self.populateTable(self.parser.freq, self.parser.depolar_u)
        self.ui.spectrum_table.setHorizontalHeaderLabels(['Frequency', 'Depolar (U)'])
        self.spectrumGraph.ax.set_title('Depolar (U) of #', fontsize=14)
        # self.p.ylim = (self.parser.depolar_u.min(), self.parser.depolar_u.max())

    s = time()

    if self.ui.broadening_check.isChecked():
        self.spectrumGraph.applyBroadening(self.p)
    print("took change: ", time()-s)

    self.spectrumGraph.draw()


def trigger_table_selection(self):
    idx = self.ui.spectrum_table.selectedIndexes()[-1].row()
    x, y = self.spectrumGraph.freq[idx], self.spectrumGraph.ints[idx]
    self.ui.intensity_label.setText(str((round(x, 3), round(y, 3))))



def trigger_change_style(self):
    self.style_dialog.exec()

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

    self.spectrumGraph.ax.set_title(self.p.title)
    self.spectrumGraph.ax.set_xlabel(self.p.xlabel)
    self.spectrumGraph.ax.set_ylabel(self.p.ylabel)
    
    self.spectrumGraph.ax.set_xlim(reversed(self.p.xlim))
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

def trigger_style_button(self, e):
    if e == 'Cancel':
        self.style_dialog.close()
    elif e == 'OK':
        trigger_apply_changes(self)
        self.style_dialog.close()
    elif e == 'Apply':
        trigger_apply_changes(self)

def trigger_pick_color(self, which):
    QtGui = importlib.import_module('PyQt5.QtWidgets')

    color = QtGui.QColorDialog(self).getColor()
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

def trigger_tab_change(self, index):
    self.ui.stackedWidget.setCurrentIndex(index)
    