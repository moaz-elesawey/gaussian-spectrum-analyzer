import matplotlib
from pyparsing import col
matplotlib.use('Qt5Agg')

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg,
    NavigationToolbar2QT as NavigationToolbar
)
from matplotlib import pyplot
import numpy as np
from time import time

# pyplot.style.use('')
pyplot.rcParams.update({'font.family':'sans-serif'})
pyplot.rcParams['font.size'] = 9


class Toolbar(NavigationToolbar):
    def __init__(self, canvas, parent, coordinates=True):
        super().__init__(canvas, parent, coordinates)
        # 'Customize',
        unwanted_buttons = [ 'Back', 'Forward', 'Pan']
        for x in self.actions():
            if x.text() in unwanted_buttons:
                self.removeAction(x)

class SpectrumGraph(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig, self.ax = pyplot.subplots(nrows=1)
        super(SpectrumGraph, self).__init__(self.fig)

        self.freq, self.ints = [], []
        self.peaks_plot = None
        self._broaden = None

        self.initStyle()
        
    def PlotData(self, freq:np.ndarray, ints:np.ndarray):
        self.freq = freq
        self.ints = ints
        if len(self.freq) != len(self.ints): return
        self.peaks_plot = self.ax.vlines(self.freq, ymin=0, ymax=self.ints, colors='k', label='Intensities Peaks')
        self.ax.set_ylim([-2, max(self.ints)])
        self.draw()

    def initStyle(self):
        # if len(self.ints) == 0: return

        self.fig.subplots_adjust(top=0.90, left=0.09, right=1, bottom=0.13)

        self.ax.spines["top"].set_visible(False)
        self.ax.spines["right"].set_visible(False)

        self.ax.set_xlabel('Wavenumber $(cm^{-1})$', fontsize=10)
        self.ax.set_ylabel('Intensity ($\epsilon$)', fontsize=10)
        self.fig.suptitle('IR Spectrum of #', fontsize=14)

        self.ax.set_xticks(np.arange(-250, 4001, 250), fontsize=12)
        self.ax.set_xlim((-300, 4200))
        self.draw()

    def removeBroadening(self):
        if len(self.ints) == 0: return
        if self._broaden:
            l = self._broaden.pop(0)
            l.remove()
            self.ax.set_ylim([-2, max(self.ints)])
        self.draw()


    def applyBroadening(self, sigma=40):
        self.removeBroadening()
        if len(self.ints) == 0: return

        x= np.linspace(-250, 4100, num=1000, endpoint=True)

        gInts = []
        for Fi in x:
            gI = np.sum(self.ints*np.exp(-((((self.freq-Fi)/sigma)**2))))
            gInts.append(gI)
        
        gInts = np.array(gInts)
        gInts = (gInts/gInts.max())*100
        self._broaden = self.ax.plot(x, gInts, color='#555555', linestyle='-', linewidth=1.2, label='Smoothed Data')
        self.ax.set_ylim([-2, max(gInts)])
        self.draw()


    def togglePeaks(self, state):
        if not state:
            if not self.peaks_plot: return
            self.peaks_plot.set_color('k')
            self.draw()
            return
        self.peaks_plot.set_color('#FFFFFF')
        self.draw()