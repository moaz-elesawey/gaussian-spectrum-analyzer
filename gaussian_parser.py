import re
import numpy as np


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


# p = Parser('data/UVVIS_CEFPODOXIME.LOG')
# print(p.load_uv_spectrum())