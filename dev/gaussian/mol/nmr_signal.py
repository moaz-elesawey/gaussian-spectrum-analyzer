
class NMRSignal:
    def __init__(self, index, atom, sheilding, desheilding) -> None:
        self.index          = index
        self.atom           = atom
        self.sheilding      = sheilding
        self.desheilding    = desheilding

    def __repr__(self) -> str:
        return f"({self.index}, {self.atom}, {self.sheilding})"
