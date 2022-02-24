import re
import numpy as np
from pprint import pprint

from utils import Atom, MESSAGE, NMRSignal


class Parser:
    def __init__(self, filename) -> None:
        self.filename = filename
        self._RE_COMBINE_WHITESPACE = re.compile(r"\s+")


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
            if MESSAGE.FREQUENCY in l:
                signal = l.replace(MESSAGE.FREQUENCY, '').strip()
                for s in signal.split(' '):
                    if s: freq.append(float(s))

        return freq

    def load_ir_intensities(self):
        ir_ints = []
        for l in self.lines:
            if MESSAGE.IR_INTESITY in l:
                signal = l.replace(MESSAGE.IR_INTESITY, '').strip()
                for s in signal.split(' '):
                    if s: ir_ints.append(float(s))

        return ir_ints

    def load_raman_intensities(self):
        raman_ints = []
        for l in self.lines:
            if MESSAGE.RAMAN_INTESITY in l:
                signal = l.replace(MESSAGE.RAMAN_INTESITY, '').strip()
                for s in signal.split(' '):
                    if s: raman_ints.append(float(s))

        return raman_ints

    def load_depolar_p(self):
        depolar_p = []
        for l in self.lines:
            if MESSAGE.DEPOLAR_P in l:
                signal = l.replace(MESSAGE.DEPOLAR_P, '').strip()
                for s in signal.split(' '):
                    if s: depolar_p.append(float(s))

        return depolar_p

    def load_depolar_u(self):
        depolar_u = []
        for l in self.lines:
            if MESSAGE.DEPOLAR_U in l:
                signal = l.replace(MESSAGE.DEPOLAR_U, '').strip()
                for s in signal.split(' '):
                    if s: depolar_u.append(float(s))

        return depolar_u

    def load_red_masses(self):
        red_masses = []
        for l in self.lines:
            if MESSAGE.RED_MASSES in l:
                signal = l.replace(MESSAGE.RED_MASSES, '').strip()
                for s in signal.split(' '):
                    if s: red_masses.append(float(s))

        return red_masses

    def load_frc_consts(self):
        frc_consts = []
        for l in self.lines:
            if MESSAGE.FRC_CONSTS in l:
                signal = l.replace(MESSAGE.FRC_CONSTS, '').strip()
                for s in signal.split(' '):
                    if s: frc_consts.append(float(s))

        return frc_consts

    def load_nmr_spectrum(self):
        nmr_sheilding = []

        for l in self.lines:
            if MESSAGE.NMR_SHEILDING in l:
                trimmed_l = self._RE_COMBINE_WHITESPACE.sub(" ", l).strip().lstrip()
                data = trimmed_l.split(' ')
                sig = NMRSignal(int(data[0]), data[1], float(data[4]), float(data[-1]))
                nmr_sheilding.append(float(data[4]))

        return nmr_sheilding

    def load_uv_spectrum(self):
        uv_spectrum = []

        for l in self.lines:
            if MESSAGE.UV_SIGNAL in l:
                trimmed_l = self._RE_COMBINE_WHITESPACE.sub(" ", l).strip().lstrip()
                data = trimmed_l.split(' ')
                # print(data)
                uv_spectrum.append(float(data[6]))

        return uv_spectrum


    def get_atoms_count(self):
        for l in self.lines:
            if MESSAGE.ATOM_COUNT in l:
                stoichiometry = l.replace(MESSAGE.ATOM_COUNT, '').strip()
                atom_count = re.findall(r'\d+', stoichiometry)
                atoms_count = sum(list(map(int, atom_count)))

                return atoms_count


    def format_table(self, table):
        tb = []

        for l in table:
            try:
                tb_l = l.strip().replace('\n', '')
                trimmed_l = self._RE_COMBINE_WHITESPACE.sub(",", tb_l).strip().lstrip()
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
            if MESSAGE.GEOMETRY in l:
                table = self.lines[idx+5:idx+atoms_count+6]
                table = self.format_table(table)
                geom_tables.append(table)
        return geom_tables

    def load_geometry_table(self):
        bonds = []

        for idx, l in enumerate(self.lines):
            
            if MESSAGE.BOND in l:
                for gl in self.lines[idx+5:]:
                    if 'R(' in gl:
                        bonds.append(list(map(int, re.findall(r'\d+,\d+', gl)[0].split(','))))
                    if MESSAGE.SEPARATOR in gl:
                        break
                break

        return bonds

    def format_vibration_state(self, state):

        formated_state = []

        for l in state:
            try:
                trimmed_l = self._RE_COMBINE_WHITESPACE.sub(",", l.strip().lstrip())
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
            if MESSAGE.VIBRATION_STATE in l:
                state1, state2, state3 = self.format_vibration_state(self.lines[idx+1:idx+atoms_counts+1])
                vibration_states.append(state1)
                vibration_states.append(state2)
                vibration_states.append(state3)
        
        vibration_states = np.array(vibration_states)

        return vibration_states
