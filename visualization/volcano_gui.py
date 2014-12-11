"""
GUI for volcano 
Main visualization
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import sys
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import json
import sys

class SubplotAnimation(animation.TimedAnimation):
    def __init__(self,title,t1,func_y1,func_y2,title1,title2,volc_fun,tmax=15,repeat=True,speed=50,start_year=None,data=None):

        fig = plt.figure(facecolor="black",figsize=(9,8))
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 2, 3)
        ax3 = fig.add_subplot(2, 2, 4)

	#map for axis 1	
	m = Basemap(ax=ax1, projection='kav7',resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
	m.bluemarble()
	volcanoes = pd.io.parsers.read_csv('../data_files/volc_loc.csv').values
	volc_lon = volcanoes[:,0]
	volc_lat = volcanoes[:,1]
	x,y = m(volc_lon,volc_lat)
        self.m = m
	cr = np.random.rand(len(x))
	volc_dot_size = np.random.randint(80,200,len(x))

        self.t0 = 0
	self.data = data
	self.start_year = start_year
        self.init = self.t0
        self.tmax = tmax
        self.abs_max = np.max(t1)
        self.t = t1
        self.x = func_y1
        self.y = func_y2
        self.z = self.t
        self.volc_fun = volc_fun
        self.randint = 0
        self.dt = self.t[1]-self.t[0]
	self.lon = x	
	self.lat = y

        ax1.set_axis_off()
        ax1.set_title(title,color='white',fontsize=30)
	self.line1 = Line2D([], [], marker='o', c='r', markersize=17, alpha=.5,markeredgecolor='k',ls='None')
        ax1.add_line(self.line1)

	if start_year is None:
		text = '\nTime (t)'
	else:
		text = '\nMonths since January ' + str(start_year)
        ax2.set_xlabel(text,color='white')
        ax2.set_ylabel('Num Volcanoes',color='white')
        ax2.set_title(title1,color='white')
        self.line2 = Line2D([], [], color='black')
        self.line2a = Line2D([], [], color='red', linewidth=2)
        self.line2e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax2.tick_params(axis='x',colors='white')
        ax2.tick_params(axis='y',colors='white')
        ax2.add_line(self.line2)
        ax2.add_line(self.line2a)
        ax2.add_line(self.line2e)
        ax2.set_ylim(np.min(self.y)*1.1, np.max(self.y)*1.1)
        ax2.set_xlim(self.t0, self.t0+self.tmax)#

        ax3.set_xlabel(text,color='white')
        ax3.set_ylabel('Meters of Displacement',color='white')
        ax3.set_title(title2,color='white')
        ax3.tick_params(axis='y',colors='white')
        ax3.tick_params(axis='x',colors='white')
        self.line3 = Line2D([], [], color='black')
        self.line3a = Line2D([], [], color='red', linewidth=2)
        self.line3e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax3.add_line(self.line3)
        ax3.add_line(self.line3a)
        ax3.add_line(self.line3e)
        ax3.set_ylim(np.min(self.x)*1.1, np.max(self.x)*1.1)
        ax3.set_xlim(self.t0, self.t0+self.tmax)
        animation.TimedAnimation.__init__(self, fig, interval=speed, blit=True,repeat=repeat)

        #save axis
	self.ax1 = ax1
        self.ax2 = ax2
        self.ax3 = ax3

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_len = 10
        head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])
        lon,lat = location_of_eruption(self.data,i,self.start_year)
        x_loc,y_loc = self.m(lon,lat)

        if i > 0:
            lastt = self.z[i-1:i][0]
        else:
            lastt = -1

        if i == 0:
            self.t0  = self.init
            self.ax2.set_xlim(self.t0, self.t0 + self.tmax)
            self.ax3.set_xlim(self.t0, self.t0 + self.tmax)  

            self.ax2.figure.canvas.draw()
            self.ax3.figure.canvas.draw()  

        if lastt > (self.t0 + self.tmax): 
             self.t0 = self.t0 + self.tmax
             self.ax2.set_xlim(self.t0, self.t0 + self.tmax)
             self.ax3.set_xlim(self.t0, self.t0 + self.tmax)

             self.ax2.figure.canvas.draw()
             self.ax3.figure.canvas.draw()
        
        self.line1.set_data(x_loc,y_loc)

        self.line2.set_data(self.z[:i], self.y[:i])
        self.line2a.set_data(self.z[head_slice], self.y[head_slice])
        self.line2e.set_data(self.z[head], self.y[head])

        self.line3.set_data(self.z[:i], self.x[:i])
        self.line3a.set_data(self.z[head_slice], self.x[head_slice])
        self.line3e.set_data(self.z[head], self.x[head])

        """
        #self._drawn_artists = [self.line1, self.line1a, self.line1e,
           # self.line2, self.line2a, self.line2e,
            #self.line3, self.line3a, self.line3e]
        """
        self._drawn_artists = [self.line1,self.line2, self.line2a, self.line2e, self.line3, self.line3a, self.line3e]

    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        """
        lines =  [self.line1, self.line1a, self.line1e,
            self.line2, self.line2a, self.line2e,
            self.line3, self.line3a, self.line3e]
        """
        lines =  [self.line1,self.line2, self.line2a, self.line2e,self.line3, self.line3a, self.line3e]

        for l in lines:
            l.set_data([], [])


def func(isfunc1,time,data,start_year):
	def func1(data,time,start_year):
		e = []
		for t in time:
			year = int(t/12)
			month = t % 12
			e.append(data[(data['Start Year']==(year+start_year)) & (data['Start Month']==month)].shape[0])
		return e


	def func2(data,t,start_year):
		return np.sin(1.3 * np.pi * t / 10.)

	if isfunc1:
		return np.asarray(func1(data,time,start_year))
	return np.asarray(func2(data,time,start_year))


def volc_location(t,x,y):
	n = np.random.randint(0,10)
	delta = datetime.datetime.now() - datetime.datetime(1970,1,1)
	seed = delta.microseconds
	np.random.seed(seed%1000)

	x = x + np.random.randint(1000,1500,len(x))*2000
	return x,y

def location_of_eruption(data,t,start_year):
	year = int(t/12)
	month = t % 12
	result = data[(data['Start Year']==(year+start_year)) & (data['Start Month']==month)][['Longitude','Latitude']]
	result = np.array(result)
	return result[:,0],result[:,1]

if __name__=='__main__':

	data = pd.read_json('../data_files/conf_erup.json')
	#start_year = np.min(data['Start Year'])
	start_year = 1950 #start year was chosen because years before 1900 tend to be very sparse (less recorded sightings of volcanoes) -this can change
	dif = 2015-start_year
	time_data = np.arange(0, 12*(dif), 1)  #starting at year 46 going to 2014
	main_title = "Volcano Data Explorer\n"  #main title for interface
	title1 = 'Number of Volcanic Eruptions'  #title for plot 1
	title2 = 'Tidal Force'   #title for plot 2
	tmax = 12  #max amount of time (on x axis) shown at a time
	repeat = True
	speed = 200 #speed of animation: higher number == lower speed; 60 is normal 

	
	#do not uncomment these lines -- ensure eruptions file is available
	#y1_data = func(True,time_data,data,start_year)    #y data for plot 1
	#np.savetxt('eruptions',y1_data)
	print "\n\n\n"
	print "=========================================="
	print "Welcome to the Volcano Visualization and Data Explorer"
	print
	print
	print "Be patient: This may take anywhere from 20-60 seconds to load!"
	print

	#loading volcanic data
	y2_data = np.loadtxt('../data_files/eruptions')
	y2_data = y2_data[len(y2_data)-len(time_data):len(y2_data)]
	y1_data = func(False,time_data,data,start_year)   #y data for plot 2
	
	print "In a second you will see two plots and a map"
	print "One of the plots will show the number of eruptions versus time"
	print
	print "The other plot will show the changing tidal forces"
	print "The point of this visualization is to notice patterns and trends through their visual juxtaposition"
	print
	print "The red dots indicate volcanoes that exploded in a certain month of the year (All step sizes for time are in months)"

	
	ani = SubplotAnimation(main_title,time_data,y1_data,y2_data,title1,title2,location_of_eruption,tmax,repeat,speed,start_year,data)
	#ani.save('test_sub.mp4')
	#plt.legend(loc=2)
	plt.show()
