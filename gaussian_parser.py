class SIGNAL:
    frequency       = " Frequencies -- "
    ir_intensity    = " IR Inten    -- "
    raman_intesity  = " Raman Activ -- "

class Parser:
    def __init__(self, filename) -> None:
        self.filename = filename

        with open(self.filename) as f:
            self.lines = f.readlines()

        self.freq       = self.load_frequencies()
        self.ir_ints    = self.load_ir_intensities()
        self.raman_ints = self.load_raman_intensities()


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

