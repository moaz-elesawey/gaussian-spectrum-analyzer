from pprint import pprint
from gaussian import Parser, Writer

p = Parser('/media/moaz/data/Gaussian_Spectrum_Analyzer/data/HF_CEFTRIAXONE.LOG')
# pprint(p.load_nmr_spectrum())
w = Writer(p)
w.generate_doc()
print(w)
