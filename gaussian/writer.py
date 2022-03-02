from pprint import pprint

from .parser import Parser

class Writer:
    def __init__(self, parser: Parser) -> None:
        self.parser = parser

        self.doc = []

    def generate_optm_structures(self):
        optms = self.parser.load_optimized_geometry()
        
        for idx, opt in enumerate(optms):
            self.doc.append(" "+"-"*71+"\n")
            self.doc.append(f"#\t\t\t Optimization Structure [{idx+1}] \t\t\t#"+"\n")
            self.doc.append(" "+"-"*71+"\n")
            for i in opt:
                self.doc.append(f"! \t {i.index} \t {i.atomic_number} \t {i.x} \t {i.y} \t {i.z} \t !"+"\n")
            self.doc.append(" "+"-"*71+"\n")

    def generate_nmr_values(self):
        nmr = self.parser.load_nmr_spectrum()
        pprint(nmr)

    def generate_initial_parameter(self):
        poss = self.parser.get_position_table()[0]

        self.doc.append(" "+"-"*71+"\n")
        self.doc.append(f"#\t\t\t Initial Parameters \t\t\t\t#"+"\n")
        self.doc.append(" "+"-"*71+"\n")
        for i in poss:
            self.doc.append(f"! \t {i.index} \t {i.atomic_number} \t {i.x} \t {i.y} \t {i.z} \t !"+"\n")
        self.doc.append(" "+"-"*71+"\n")

    def generate_bonds(self):
        bonds = self.parser.load_geometry_table()
        pprint(bonds)

    def generate_energies(self):
        energy = self.parser.load_energies()
        pprint(energy)        

    def generate_freqs(self):
        freq = self.parser.freq
        ir_ints = self.parser.ir_ints
        raman_ints = self.parser.raman_ints
        frc_consts = self.parser.frc_consts
        depolar_p = self.parser.depolar_p
        depolar_u = self.parser.depolar_u

        # for 

    def generate_doc(self):
        self.generate_initial_parameter()
        self.generate_optm_structures()
        # self.generate_bonds()
        # self.generate_energies()

        return "".join(self.doc)
