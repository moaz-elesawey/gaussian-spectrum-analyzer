import numpy as np


class MESSAGE:
    FREQUENCY       = " Frequencies -- "
    IR_INTESITY     = " IR Inten    -- "
    RAMAN_INTESITY  = " Raman Activ -- "
    RED_MASSES      = " Red. masses -- "
    FRC_CONSTS      = " Frc consts  -- "
    DEPOLAR_P       = " Depolar (P) -- "
    DEPOLAR_U       = " Depolar (U) -- "
    NMR_SHEILDING   = " Isotropic =   "
    UV_SIGNAL       = " Excited State   "
    ATOM_COUNT      = "Stoichiometry"
    VIBRATION_STATE = "Atom AN      X      Y      Z        X      Y      Z        X      Y      Z"
    GEOMETRY        = "Standard orientation:"
    BOND            = "Optimized Parameters"
    SEPARATOR       = "GradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGradGrad"


class Atom:
    def __init__(self, index, atomic_number, v, x, y, z) -> None:
        self.index = int(index)
        self.atomic_number = int(atomic_number)
        self.v = v
        self.x = x
        self.y = y
        self.z = z
        self.color = self.get_color()


    def get_color(self):
        Z = int(self.atomic_number)
        color = [125, 125, 125, 1]

        if Z == 8:
            color = [1, 0, 0, 1]
        elif Z == 6:
            color = [.2, .2, .2, 1]
        elif Z == 1:
            color = [1, 1, 1, 1]
        elif Z == 7:
            color = [0, 0, 1, 1]
        elif Z == 16:
            color = [1, 1, 0, 1]

        return np.array(color)
        
    def get_object(self):
        return {'index': self.index, "x": self.x, "y": self.y, "z": self.z, "atomicNumber": self.atomic_number}

    @property
    def pos(self):
        return self.x, self.y, self.z

    def __repr__(self) -> str:
        return f'Atom({self.index}, {self.atomic_number})'

class Bond:
    def __init__(self, l:int, r:int) -> None:
        self.l = l
        self.r = r

class NMRSignal:
    def __init__(self, index, atom, sheilding, desheilding) -> None:
        self.index          = index
        self.atom           = atom
        self.sheilding      = sheilding
        self.desheilding    = desheilding

    def __repr__(self) -> str:
        return f"({self.index}, {self.atom}, {self.sheilding})"


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