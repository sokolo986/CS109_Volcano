import os, sys

lib_path = os.path.abspath('rose_diagram_plot/')
sys.path.append(lib_path)

import rosePlot as rp

print "Hello World"

rp.RoseFreqPlot()

