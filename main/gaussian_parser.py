import re
import numpy as np
from pprint import pprint


class SIGNAL:
    frequency       = " Frequencies -- "
    ir_intensity    = " IR Inten    -- "
    raman_intesity  = " Raman Activ -- "
    red_masses      = " Red. masses -- "
    frc_consts      = " Frc consts  -- "
    depolar_p       = " Depolar (P) -- "
    depolar_u       = " Depolar (U) -- "
    nmr_sheilding   = " Isotropic =   "
    uv_signal       = " Excited State   "
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

class Parser:
    def __init__(self, filename) -> None:
        self.filename = filename

        with open(self.filename) as f:
            self.lines = f.readlines()

        self.freq           = np.array(self.load_frequencies())
        self.ir_ints        = np.array(self.load_ir_intensities())
        self.raman_ints     = np.array(self.load_raman_intensities())
        self.depolar_p      = np.array(self.load_depolar_p())
        self.depolar_u      = np.array(self.load_depolar_u())
        self.frc_consts     = np.array(self.load_frc_consts())
        self.red_masses     = np.array(self.load_red_masses())
        self.nmr_sheilding  = np.array(self.load_nmr_spectrum())
        self.uv_spectrum    = np.array(self.load_uv_spectrum())

        self.ir_ints        = (self.ir_ints/self.ir_ints.max())*100 if len(self.ir_ints) > 0 else self.ir_ints
        self.raman_ints     = (self.raman_ints/self.raman_ints.max())*100 if len(self.raman_ints) > 0 else self.raman_ints
        self.depolar_p      = (self.depolar_p/self.depolar_p.max())*100 if len(self.depolar_p) > 0 else self.depolar_p
        self.depolar_u      = (self.depolar_u/self.depolar_u.max())*100 if len(self.depolar_u) > 0 else self.depolar_u
        self.frc_consts     = (self.frc_consts/self.frc_consts.max())*100 if len(self.frc_consts) > 0 else self.frc_consts
        self.red_masses     = (self.red_masses/self.red_masses.max())*100 if len(self.red_masses) > 0 else self.red_masses
        self.nmr_sheilding  = (self.nmr_sheilding/self.nmr_sheilding.max())*100 if len(self.nmr_sheilding) > 0 else self.nmr_sheilding
        self.uv_spectrum    = (self.uv_spectrum/self.uv_spectrum.max())*100 if len(self.uv_spectrum) > 0 else self.uv_spectrum

        self.animations     = self.load_vibration_states()


    def load_frequencies(self):
        freq = []
        for l in self.lines:
            if SIGNAL.frequency in l:
                signal = l.replace(SIGNAL.frequency, '').strip()
                for s in signal.split(' '):
                    if s: freq.append(float(s))

        return freq

    def load_ir_intensities(self):
        ir_ints = []
        for l in self.lines:
            if SIGNAL.ir_intensity in l:
                signal = l.replace(SIGNAL.ir_intensity, '').strip()
                for s in signal.split(' '):
                    if s: ir_ints.append(float(s))

        return ir_ints

    def load_raman_intensities(self):
        raman_ints = []
        for l in self.lines:
            if SIGNAL.raman_intesity in l:
                signal = l.replace(SIGNAL.raman_intesity, '').strip()
                for s in signal.split(' '):
                    if s: raman_ints.append(float(s))

        return raman_ints

    def load_depolar_p(self):
        depolar_p = []
        for l in self.lines:
            if SIGNAL.depolar_p in l:
                signal = l.replace(SIGNAL.depolar_p, '').strip()
                for s in signal.split(' '):
                    if s: depolar_p.append(float(s))

        return depolar_p


    def load_depolar_u(self):
        depolar_u = []
        for l in self.lines:
            if SIGNAL.depolar_u in l:
                signal = l.replace(SIGNAL.depolar_u, '').strip()
                for s in signal.split(' '):
                    if s: depolar_u.append(float(s))

        return depolar_u


    def load_red_masses(self):
        red_masses = []
        for l in self.lines:
            if SIGNAL.red_masses in l:
                signal = l.replace(SIGNAL.red_masses, '').strip()
                for s in signal.split(' '):
                    if s: red_masses.append(float(s))

        return red_masses


    def load_frc_consts(self):
        frc_consts = []
        for l in self.lines:
            if SIGNAL.frc_consts in l:
                signal = l.replace(SIGNAL.frc_consts, '').strip()
                for s in signal.split(' '):
                    if s: frc_consts.append(float(s))

        return frc_consts


    def load_nmr_spectrum(self):
        nmr_sheilding = []
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

        for l in self.lines:
            if SIGNAL.nmr_sheilding in l:
                trimmed_l = _RE_COMBINE_WHITESPACE.sub(" ", l).strip().lstrip()
                data = trimmed_l.split(' ')
                sig = NMRSignal(int(data[0]), data[1], float(data[4]), float(data[-1]))
                nmr_sheilding.append(float(data[4]))

        return nmr_sheilding

    def load_uv_spectrum(self):
        uv_spectrum = []
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

        for l in self.lines:
            if SIGNAL.uv_signal in l:
                trimmed_l = _RE_COMBINE_WHITESPACE.sub(" ", l).strip().lstrip()
                data = trimmed_l.split(' ')
                # print(data)
                uv_spectrum.append(float(data[6]))

        return uv_spectrum


    def get_atoms_count(self):
        for l in self.lines:
            if SIGNAL.ATOM_COUNT in l:
                stoichiometry = l.replace(SIGNAL.ATOM_COUNT, '').strip()
                atom_count = re.findall(r'\d+', stoichiometry)
                atoms_count = sum(list(map(int, atom_count)))

                return atoms_count


    def format_table(self, table):
        tb = []
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

        for l in table:
            try:
                tb_l = l.strip().replace('\n', '')
                trimmed_l = _RE_COMBINE_WHITESPACE.sub(",", tb_l).strip().lstrip()
                ent = list(map(float, trimmed_l.split(',')))
                atom = Atom(ent[0], ent[1], ent[2], ent[3], ent[4], ent[5])
                tb.append(atom)
            except Exception as e:
                print(str(e))

        return tb


    def get_position_table(self):
        atoms_count = self.get_atoms_count()
        
        geom_tables = []

        for idx, l in enumerate(self.lines):
            if SIGNAL.GEOMETRY in l:
                table = self.lines[idx+5:idx+atoms_count+6]
                table = self.format_table(table)
                geom_tables.append(table)
        return geom_tables


    def load_geometry_table(self):
        bonds = []

        for idx, l in enumerate(self.lines):
            
            if SIGNAL.BOND in l:
                for gl in self.lines[idx+5:]:
                    if 'R(' in gl:
                        bonds.append(list(map(int, re.findall(r'\d+,\d+', gl)[0].split(','))))
                    if SIGNAL.SEPARATOR in gl:
                        break
                break

        return bonds

    def format_vibration_state(self, state):
        _RE_COMBINE_WHITESPACE = re.compile(r"\s+")

        formated_state = []

        for l in state:
            try:
                trimmed_l = _RE_COMBINE_WHITESPACE.sub(",", l.strip().lstrip())
                trimmed_l = list(map(float, trimmed_l.split(',')))
                formated_state.append(trimmed_l)
            except Exception as e:
                pass
        formated_state = np.array(formated_state)
        
        return formated_state[:, 2:5], formated_state[:, 5:8], formated_state[:, 8:11]

    def load_vibration_states(self):
        vibration_states = []
        atoms_counts = self.get_atoms_count()
        for idx, l in enumerate(self.lines):
            if SIGNAL.VIBRATION_STATE in l:
                state1, state2, state3 = self.format_vibration_state(self.lines[idx+1:idx+atoms_counts+1])
                vibration_states.append(state1)
                vibration_states.append(state2)
                vibration_states.append(state3)
        
        vibration_states = np.array(vibration_states)

        return vibration_states