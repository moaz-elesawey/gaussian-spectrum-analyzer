import csv
import importlib
from math import atan2, hypot, pi, sqrt
import os
from numpy import arange, array
from pyqtgraph.opengl import MeshData, GLMeshItem


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class MESSAGE:
    FREQUENCY       = " Frequencies -- "
    IR_INTESITY     = " IR Inten    -- "
    RAMAN_INTESITY  = " Raman Activ -- "
    RED_MASSES      = " Red. masses -- "
    FRC_CONSTS      = " Frc consts  -- "
    DEPOLAR_P       = " Depolar (P) -- "
    DEPOLAR_U       = " Depolar (U) -- "
    NMR_SHEILDING   = " Isotropic ="
    ATOM_COUNT      = "Stoichiometry"
    VIBRATION_STATE = "Atom AN      X      Y      Z        X      Y      Z        X      Y      Z"
    GEOMETRY        = " Center     Atomic     Atomic              Coordinates (Angstroms)"
    BOND            = "                           !    Initial Parameters    !"
    SEPARATOR       = " --------------------------------------------------------------------------------"
    RMS_FORCE       = "RMS     Force"
    RMS_DISPL       = "RMS     Displacement"
    MAX_FORCE       = "Maximum Force"
    MAX_DISPL       = "Maximum Displacement"
    TOT_ENERGY      = "Predicted change in Energy="
    OPTMIZED_GEOM   = " Center     Atomic     Atomic              Coordinates (Angstroms)"

    THERMAL_ENERGY          = " Thermal correction to Energy="
    THERMAL_ENTHALPY        = " Thermal correction to Enthalpy="
    THERMAL_GIBBS           = " Thermal correction to Gibbs Free Energy="

    SUM_THERMAL_ENERGY      = " Sum of electronic and thermal Energies="
    SUM_THERMAL_ENTHALPY    = " Sum of electronic and thermal Enthalpies="
    SUM_THERMAL_GIBBS       = " Sum of electronic and thermal Free Energies="

    ZERO_POINT_CORR     = " Zero-point correction="
    ZERO_POINT_ENERGY   = " Sum of electronic and zero-point Energies="

    UV_SIGNAL       = " Excited State "
    UV_OSC_START    = "Ground to excited state Transition electric dipole moments (Au):"
    UV_OSC_END      = "Ground to excited state transition velocity dipole Moments (Au):"
    ECD_OSC_START   = "<0|del|b> * <b|rxdel|0>  (Au), Rotatory Strengths (R) in"
    ECD_OSC_END     = "<0|r|b> * <b|rxdel|0>  (Au), Rotatory Strengths (R) in"

EXPORT_FORMATS = [
    'PNG',
    'JPG',
    'SVG',
    'PDF',
]

LINESTYLES = [
    '-', '--', '-.', ':'
]

PATHS = {
    'icons': 'icons/',
    'ui': 'ui/'
}

SPECTRUM_TYPES = [
    'Transmittance',
    'Absorbance',
]

def save_figure(self, ):
    pyplot = importlib.import_module('matplotlib.pyplot')

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
            self.spectrumGraph.freq, ymin=100, ymax=100-self.spectrumGraph.ints,
            colors=self.p.spikes_color, label='Peaks' 
        )
    if self.ui.broadening_check.isChecked():
        x, gInts = self.generate_broadening_for_export(
            self.ui.broadening_slider.value(),
            self.spectrumGraph.freq,
            self.spectrumGraph.ints
        )
        gInts = (1-(gInts/gInts.max()))*100
        ax.plot(
            x, gInts, color=self.p.broaden_color, 
            linewidth=self.p.broaden_width, 
            linestyle=self.p.broaden_style,
            label='Spectrum'
        )

    ax.set_ylim([-3, 106])
    ax.set_xticks(arange(-250, 4251, 250), fontsize=14)
    ax.set_yticks(arange(0, 101, 10), fontsize=self.style_dialog.fontsize_inp.value())
    ax.set_xlabel(self.style_dialog.xlabel_inp.text(), fontsize=self.style_dialog.fontsize_inp.value())
    ax.set_ylabel(self.style_dialog.ylabel_inp.text(), fontsize=self.style_dialog.fontsize_inp.value())
    ax.set_title(self.style_dialog.title_inp.text(), fontsize=self.style_dialog.fontsize_inp.value()+2)
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    ax.minorticks_on()
    ax.tick_params(which='major', length=5, direction='in', left=True,right=False,top=False,bottom=True)
    ax.tick_params(which='minor', length=2.5, direction='in', left=True,right=False,top=False,bottom=True)
    leg = ax.legend(loc='lower left', ncol=2, frameon=True, fancybox=False, fontsize=self.style_dialog.fontsize_inp.value())
    ax.invert_xaxis()
    ax.set_xlim(reversed(self.p.xlim))
    fig.tight_layout()

    return fig


def convert_to_csv(filename, header, data):
    with open(filename, 'w') as w:
        writer = csv.writer(w, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(header)
        writer.writerows(data)


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def create_gl_bond(atom1, atom2):
    v = [atom2.x-atom1.x, atom2.y-atom1.y, atom2.z-atom1.z]
    height = sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    axis = (1, 0, 0) if hypot(v[0], v[1]) < 0.001 else cross(v, (0, 0, 1))
    angle = -atan2(hypot(v[0], v[1]), v[2])*180/pi
    
    shader = 'shaded'
    radius = [0.1, 0.1]
    glOptions = 'opaque'
    col = array([.5,.5,.5,1])

    # s = time()

    md = MeshData.cylinder(rows=20, cols=20, radius=radius, length=height)
    m3 = GLMeshItem(meshdata=md, smooth=False, 
            drawFaces=True, drawEdges=False, shader=shader,
            edgeColor=col, color=col, glOptions=glOptions, antialias=True)

    m3.rotate(angle, *axis)
    m3.translate(*atom1.pos)

    return m3