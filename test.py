from pprint import pprint
from gaussian import Parser, Writer

p = Parser('/media/moaz/data/Gaussian_Spectrum_Analyzer/data/UVVIS_CEFPODOXIME.LOG')
pprint(p.load_uv_ecd())
