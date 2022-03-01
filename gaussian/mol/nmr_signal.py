import numpy as np

class NMRSignal:
    def __init__(self, index, atom, sheilding, desheilding) -> None:
        self.index          = index
        self.atom           = atom
        self.sheilding      = sheilding
        self.desheilding    = desheilding

        self.deg = None

    def __repr__(self) -> str:
        return f"({self.index}, {self.atom}, {self.sheilding})"

    @property
    def values(self):
        return self.index, self.atom, self.sheilding, self.desheilding, self.deg


class NMRSpectrum:
    def __init__(self, signals: list) -> None:
        self.signals = sorted(signals, key=lambda e: e.sheilding)

    def compute_deg(self):

        if len(self.signals) == 0:
            return

        sheilding = [sig.sheilding for sig in self.signals]

        appr_sheilding = np.array(sheilding, dtype=np.float32).round(1)
        unique_sheilding = np.unique(appr_sheilding, return_counts=True)
        sheilding_counts = unique_sheilding[1].tolist()
        sheilding_values = unique_sheilding[0].tolist()

        mask = unique_sheilding[1] != 1

        for itr, val in zip(unique_sheilding[1][mask], unique_sheilding[0][mask]):
            for _ in range(itr-1):
                sheilding_counts.append(itr)
                sheilding_values.append(val)
        
        deg = np.array(sheilding_counts)
        sheilding = np.array(sheilding_values)

        nmr_data = np.hstack((sheilding.reshape(-1, 1), deg.reshape(-1, 1)))
        nmr_data = np.array(sorted(nmr_data, key=lambda e: e[0])).round(4)


        self.sheilding = nmr_data[:, 0]
        self.deg = nmr_data[:, 1]

        for sig, sh, d in zip(self.signals, self.sheilding, self.deg):
            # sig.sheilding = sh
            sig.deg = d


    def compute_continous_spectrum(self):

        if len(self.signals) == 0:
            return

        continous_spectrum = []

        nx = np.linspace(min(self.sheilding)-100, max(self.sheilding)+100, 1000, endpoint=True)

        for Fi in nx:
            gI = np.sum(self.deg*np.exp(-((np.float_power((self.sheilding-Fi)/3, (2))))))
            continous_spectrum.append(gI)

        continous_spectrum = np.array(continous_spectrum)
        continous_spectrum = (continous_spectrum/continous_spectrum.max())*5

        return nx, continous_spectrum


    @property
    def spectrum_data(self):
        
        self.compute_deg()

        return [sig.values for sig in self.signals]

    @property
    def ok(self):
        return len(self.signals) != 0
