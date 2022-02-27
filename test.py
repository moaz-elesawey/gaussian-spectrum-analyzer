from pprint import pprint
from gaussian import Parser

p = Parser('/media/moaz/data/Gaussian_Spectrum_Analyzer/data/HF_CEFTRIAXONE.LOG')
pprint(p.load_energies())