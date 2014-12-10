import numpy as np
import matplotlib.pyplot as pl
from matplotlib.projections import register_projection
from NorthPolarAxes import NorthPolarAxes
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('configure')
filename = config.get('configure', 'filename')
angle = int(config.get('configure', 'angle'))

register_projection(NorthPolarAxes)

data = np.genfromtxt(filename)

nsection = 360 / angle
direction = np.linspace(0, 360, nsection, False) / 180 * np.pi
frequency = [0] * (nsection)
dipangle = [0] * (nsection)
for i in range(len(data)):
	tmp = int((data[i][1] - data[i][1] % angle) / angle)
	frequency[tmp] = frequency[tmp] + 1
	dipangle[tmp] = dipangle[tmp] + data[i][0]
for i in range(nsection):
	if frequency[i] > 0:
		dipangle[i] = dipangle[i] / frequency[i]
	
width = angle / 180.0 * np.pi * np.ones(nsection)

ax = pl.subplot(1, 1, 1, projection = 'northpolar')
bars = ax.bar(direction, dipangle, width=width, bottom=0.0)
for r,bar in zip(frequency, bars):
    bar.set_facecolor(pl.cm.jet(0.8))
    bar.set_edgecolor('grey')
    bar.set_alpha(0.8)

pl.show()
