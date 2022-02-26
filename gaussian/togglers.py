
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

    # self.ui.broadening_inp.setText(str(self.ui.broadening_slider.value()))

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

def toggle_grid(self):
    if self.grid_toggled:
        self.viewer.removeItem(self.viewer_grid)
        self.grid_toggled = False
    else:
        self.viewer.addItem(self.viewer_grid)
        self.grid_toggled = True
