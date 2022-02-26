from pprint import pprint
from gaussian import Parser

p = Parser('/media/moaz/data/Gaussian_Spectrum_Analyzer/main/data/HF_CEFOVECIN.LOG')
pprint(p.load_optimized_geometry())