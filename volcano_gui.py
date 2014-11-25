#GUI for volcano - only function left to implement is a conversion between the location of a dot on a picture and a map - we can start migrating true data to this file
#will also clean up file so it looks neater 

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import sys

class SubplotAnimation(animation.TimedAnimation):
    def __init__(self,title,t1,func_y1,func_y2,title1,title2,map_file,volc_fun,tmax=15,repeat=True):
        fig = plt.figure(facecolor="black",figsize=(9,8))
        img = mpimg.imread(map_file)
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(2, 2, 3)
        ax3 = fig.add_subplot(2, 2, 4)

        self.t0 = 0
        self.init = self.t0
        self.tmax = tmax
        self.abs_max = np.max(t1)
        self.t = t1
        self.x = func_y1(self.t)
        self.y = func_y2(self.t)
        self.z = 10 * self.t
        self.volc_fun = volc_fun
        self.randint = 0
        self.dt = self.t[1]-self.t[0]

        ax1.imshow(img)
        ax1.set_axis_off()
        ax1.set_title(title,color='white')
        #ax1.set_xlim(-1, 3000)
        #ax1.set_ylim(-2, 2000)
        #ax1.set_aspect('equal', 'datalim')
        self.line1 = Line2D([], [], marker='^', markersize=15,color='green',drawstyle='steps-post',ls='None')
        ax1.add_line(self.line1)

        ax2.set_xlabel('\nTime (t)',color='white')
        ax2.set_ylabel('Num Volcanoes',color='white')
        ax2.set_title(title1,color='white')
        self.line2 = Line2D([], [], color='black')
        self.line2a = Line2D([], [], color='red', linewidth=2)
        self.line2e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax2.tick_params(axis='x',colors='white')
        ax2.add_line(self.line2)
        ax2.add_line(self.line2a)
        ax2.add_line(self.line2e)
        ax2.set_ylim(np.min(self.y)*1.1, np.max(self.y)*1.1)
        #ax2.set_xlim(0, 800)#changed
        ax2.set_xlim(self.t0, self.t0+self.tmax)# 800)#10*np.max(self.t))

        ax3.set_xlabel('\nTime (t)',color='white')
        ax3.set_ylabel('Tide Height',color='white')
        ax3.set_title(title2,color='white')
        ax3.tick_params(axis='x',colors='white')
        self.line3 = Line2D([], [], color='black')
        self.line3a = Line2D([], [], color='red', linewidth=2)
        self.line3e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax3.add_line(self.line3)
        ax3.add_line(self.line3a)
        ax3.add_line(self.line3e)
        ax3.set_ylim(np.min(self.x)*1.1, np.max(self.x)*1.1)#changed
        ax3.set_xlim(self.t0, self.t0+self.tmax)#800)#10*np.max(self.t))#changed
        animation.TimedAnimation.__init__(self, fig, interval=50, blit=True,repeat=repeat)
        #save axis
        self.ax2 = ax2
        self.ax3 = ax3

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_len = 10
        head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])
        vol   = self.volc_fun()

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

        if lastt > (self.t0 + self.tmax): # reset the arrays
             self.t0 = self.t0 + self.tmax
             self.ax2.set_xlim(self.t0, self.t0 + self.tmax)
             self.ax3.set_xlim(self.t0, self.t0 + self.tmax)
             self.ax2.figure.canvas.draw()
             self.ax3.figure.canvas.draw()
        
        self.line1.set_data(vol[0], vol[1])
        #self.line1.set_data(self.x[:i], self.y[:i])
        #self.line1a.set_data(self.x[head_slice], self.y[head_slice])
        #self.line1e.set_data(self.x[head], self.y[head])

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

#these can eventually go away once we input the data
#func1 and func2 must accept an array and produce and return an array of resulting values
def func(isfunc1):
	def func1(t):
		return np.random.randn(1,len(t))[0]#np.array([np.random.randn(1) for i in t])
		return np.cos(2 * np.pi * t / 10.)

	def func2(t):
		return np.sin(1.3 * np.pi * t / 10.)

	if isfunc1:
		return func1
	return func2

#these can eventually go away once we input the data
#function that returns the location of a volcano that erupted during an array of different time frames
def volc_location(t=None):
	n = np.random.randint(0,10)
	x = np.random.randint(0,1700,n)
	y = np.random.randint(0,1000,n)
	return x,y

if __name__=='__main__':

	map_name = 'world_map.png'   #picture that will display volcanoes
	time_data = np.linspace(0, 80, 400)  #x data for plot 1 (should be in terms of time (t))
	y1_data  = func(True)    #y data for plot 1
	y2_data  = func(False)   #y data for plot 2
	main_title = "Volcano Data Explorer \n"  #main title for interface
	title1	= 'Volcanoes over time'  #title for plot 1
	title2	= 'Tide over time'   #title for plot 2
	tmax     = 50  #max x (on x axis) shown at a time
	repeat   = True

	ani      = SubplotAnimation(main_title,time_data,y1_data,y2_data,title1,title2,map_name,volc_location,tmax,repeat)
	#ani.save('test_sub.mp4')
	plt.show()
