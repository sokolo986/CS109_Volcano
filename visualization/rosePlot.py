"""
This file creates a Rose Plot Diagram given the Angle and Height of the Histogram
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.projections import register_projection
from NorthPolarAxes import NorthPolarAxes
import ConfigParser
import sys

#histogram version
class RoseFreqPlot():
	#x is the size of the histogram and y is angle
	def __init__(self,data):
		data = np.asarray(data)
		register_projection(NorthPolarAxes)

		#define important parameters
		angle = 5
		nsection = 360 / angle
		self.direction = np.linspace(0, 360, nsection, False) / 180 * np.pi

		#put data in bins --- data needs to be 0-360
		self.frequency = [0] * (nsection)
		for i in data:
			tmp = int((i[1] - i[1] % angle) / angle)
			self.frequency[tmp] = self.frequency[tmp] + 1
		self.width = angle / 180.0 * np.pi * np.ones(nsection)
		
	def plot_rose(self,plot_title):
		#plot data
		ax = plt.subplot(1, 1, 1, projection = 'northpolar')
		ax.set_title(plot_title)
		bars = ax.bar(self.direction, self.frequency, width=self.width, bottom=0.0)
		for r,bar in zip(self.frequency, bars):
			bar.set_facecolor(plt.cm.jet(0.8))
			bar.set_edgecolor('grey')
			bar.set_alpha(0.8)
		plt.show()

#non-binned data version - takes avg value at angle theta
class RosePlot():
	#x is the size of the histogram and y is angle
	def __init__(self,data):
		data = np.asarray(data)
		register_projection(NorthPolarAxes)

		#define important parameters
		angle		= 5
		nsection = 360 / angle
		self.direction = np.linspace(0, 360, nsection, False) / 180 * np.pi

		#put data in bins
		frequency = {}#[0] * (nsection)
		for i in xrange(nsection):
			frequency[i] = []

		for d in data:
			tmp = int((d[1] - d[1] % angle) / angle)
			frequency[tmp].append(tmp)
		
		#average all freq values
		freq = []
		for k in sorted(frequency.iterkeys()):
			if len(frequency[k])==0:
				freq.append(0.)
			else:
				freq.append(np.mean(frequency[k]))
		self.width = angle / 180.0 * np.pi * np.ones(nsection)
		self.frequency = freq

		#print self.frequency,type(self.frequency),len(self.frequency)
		#sys.exit(0)

	def plot_rose(self,plot_title):
		#plot data
		ax = plt.subplot(1, 1, 1, projection = 'northpolar')
		ax.set_title(plot_title)
		bars = ax.bar(self.direction, self.frequency, width=self.width, bottom=0.0)
		for r,bar in zip(self.frequency, bars):
			bar.set_facecolor(plt.cm.jet(0.8))
			bar.set_edgecolor('grey')
			bar.set_alpha(0.8)
		plt.show()

if __name__ == '__main__':

	filename 	= 'dip_azim'
	plot_title	= 'Rose Plot'
	data 			= 	np.genfromtxt(filename)
	rp				=  RoseFreqPlot(data)
	rp.plot_rose(plot_title + ' - Histogram Version')

	rpr			=  RosePlot(data)
	rpr.plot_rose(plot_title + ' - Averaged Version')

