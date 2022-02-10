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

pyplot.rcParams["font.family"] = "serif"
# pyplot.rcParams["mathtext.fontset"] = "dejavuserif"
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
        
        # self.ax.set_ylim([min(self.ints), max(self.ints)])
        if not len(self.freq) == 0:
            self.ax.set_xlim(min(self.freq), max(self.freq))

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

    def removeBroadening(self, p):
        if len(self.ints) == 0: return
        if self._broaden:
            l = self._broaden.pop(0)
            l.remove()

            xmin, xmax = min(self.ints), max(self.ints)
            if xmin == xmax:
                xmin = 0
            p.ylim = (xmin, xmax)
            self.ax.set_ylim(p.ylim)
        self.draw()

    def applyBroadening(self, p):
        self.removeBroadening(p)
        if len(self.ints) == 0 or len(self.freq) == 0: return

        x= np.linspace(min(self.freq)-200, max(self.freq)+200, num=800, endpoint=True)

        gInts = []
        for Fi in x:
            gI = np.sum(self.ints*np.exp(-((((self.freq-Fi)/p.broaden_sigma)**2))))
            gInts.append(gI)
        
        gInts = np.array(gInts)
        gInts = (gInts/gInts.max())*100
        self._broaden = self.ax.plot(x, gInts, color=p.broaden_color, linestyle=p.broaden_style, 
                linewidth=p.broaden_width, label='Smoothed Data')
        
        xmin, xmax = gInts.min(), gInts.max()
        if xmin == xmax:
            xmin = 0
        p.ylim = (xmin, xmax)
        self.ax.set_ylim(p.ylim)
        self.ax.set_xlim(min(x), max(x))

        self.draw()

    def togglePeaks(self, state, color):
        if not state:
            if not self.peaks_plot: return
            self.peaks_plot.set_color(color)
            self.draw()
            return
        self.peaks_plot.set_color('#FFFFFF')
        self.draw()


class Properties:
    def __init__(self):
        self.xlabel          = ''
        self.ylabel          = ''
        self.title           = ''
        self.broaden_color   = '#333333'
        self.broaden_style   = '-'
        self.broaden_width   = 1
        self.broaden_sigma   = 40
        self.spikes_color    = '#000000'
        self.spikes_style    = '-'
        self.spikes_width    = 1
        self.xlim            = -250, 4200
        self.ylim            = -2, 105
        self.minor_ticks     = False
        self.marker_color    = 'r'
        self.figure_width    = 11.79
        self.figure_height   = 4.27
        self.padding_top     = 0.90
        self.padding_bottom  = 0.13
        self.padding_left    = 0.13
        self.padding_right   = 0.98

    @property
    def xlim(self):
        return self._xlim

    @xlim.setter
    def xlim(self, xlim):
        self._xlim = xlim[0]-200, xlim[1]+200

    @property
    def ylim(self):
        return self._ylim

    @ylim.setter
    def ylim(self, ylim):
        self._ylim = ylim[0]-2, ylim[1]+8
