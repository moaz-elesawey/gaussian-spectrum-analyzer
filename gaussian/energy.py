
class Energy:
    def __init__(self, E, H, G, Z, ZE, SE, SH, SG) -> None:
        self.E = E
        self.H = H
        self.G = G
        self.Z = Z
        self.ZE = ZE
        self.SE = SE
        self.SH = SH
        self.SG = SG

        self.energies = [self.E, self.H, self.G, self.Z, self.ZE, self.SE, self.SH, self.SG]

    @property
    def au(self):
        return self.energies

    @property
    def Kcal_mol(self):
        return list(map(lambda e: e*627.5, self.energies))
    
    @property
    def KJ_mol(self):
        return list(map(lambda e: e*2625.5, self.energies))

    @property
    def eV(self):
        return list(map(lambda e: e*27.211, self.energies))

    def __repr__(self) -> str:
        return str(self.energies)

    @property
    def ok(self):
        return (len(self.energies) != 0) and (self.energies[0] is not None)

