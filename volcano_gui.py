import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
import matplotlib.image as mpimg
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# This example uses subclassing, but there is no reason that the proper function
# couldn't be set up and then use FuncAnimation. The code is long, but not
# really complex. The length is due solely to the fact that there are a total
# of 9 lines that need to be changed for the animation as well as 3 subplots
# that need initial set up.
class SubplotAnimation(animation.TimedAnimation):
    def __init__(self,title,t1,func_y1,func_y2,map_file,volc_fun):
        fig = plt.figure(facecolor="black",figsize=(7,8))
        img = mpimg.imread(map_file)
        ax1 = fig.add_subplot(2, 1, 1)
        ax2 = fig.add_subplot(3, 3, 7)
        ax3 = fig.add_subplot(3, 3, 9)

        self.t = t1
        self.x = func_y1(t1)
        self.y = func_y2(t1)
        self.z = 10 * self.t
        self.volc_fun = volc_fun
        self.randint = np.random.randint(0,50)

        ax1.imshow(img)
        ax1.set_axis_off()
        title_obj = ax1.set_title(title,color='white')
        ax1.scatter(self.volc_fun(self.randint)[0],self.volc_fun(self.randint)[1],color='r')
        #ax1.set_xlim(-1, 3000)
        #ax1.set_ylim(-2, 2000)
        #ax1.set_aspect('equal', 'datalim')
        self.ax1 = ax1
        ax2.set_xlabel('Time (t)',color='white')
        ax2.set_ylabel('Num Volcanoes',color='white')
        self.line2 = Line2D([], [], color='black')
        self.line2a = Line2D([], [], color='red', linewidth=2)
        self.line2e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax2.add_line(self.line2)
        ax2.add_line(self.line2a)
        ax2.add_line(self.line2e)
        ax2.set_ylim(np.min(self.y)*1.1, np.max(self.y)*1.1)
        #ax2.set_xlim(0, 800)#changed
        ax2.set_xlim(0, 10*np.max(t))

        ax3.set_xlabel('Time (t)',color='white')
        ax3.set_ylabel('Tide Height',color='white')
        self.line3 = Line2D([], [], color='black')
        self.line3a = Line2D([], [], color='red', linewidth=2)
        self.line3e = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        ax3.add_line(self.line3)
        ax3.add_line(self.line3a)
        ax3.add_line(self.line3e)
        ax3.set_ylim(np.min(self.x)*1.1, np.max(self.x)*1.1)#changed
        ax3.set_xlim(0, 10*np.max(t))#changed
        animation.TimedAnimation.__init__(self, fig, interval=50, blit=True)

    def _draw_frame(self, framedata):
        i = framedata
        head = i - 1
        head_len = 10
        head_slice = (self.t > self.t[i] - 1.0) & (self.t < self.t[i])

        self.randint = np.random.randint(0,50)
        self.ax1.scatter(self.volc_fun(self.randint)[0],self.volc_fun(self.randint)[1],color='r')

        #self.line1.set_data(self.x[:i], self.y[:i])
        #self.line1a.set_data(self.x[head_slice], self.y[head_slice])
        #self.line1e.set_data(self.x[head], self.y[head])
        #switched y/z and x/z in this section
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
        self._drawn_artists = [self.line2, self.line2a, self.line2e, self.line3, self.line3a, self.line3e]

    def new_frame_seq(self):
        return iter(range(self.t.size))

    def _init_draw(self):
        """
        lines =  [self.line1, self.line1a, self.line1e,
            self.line2, self.line2a, self.line2e,
            self.line3, self.line3a, self.line3e]
        """
        lines =  [self.line2, self.line2a, self.line2e,self.line3, self.line3a, self.line3e]

        for l in lines:
            l.set_data([], [])

#func1 and func2 must accept an array and produce and return an array of resulting values
def func(isfunc1):
	def func1(t):
		return np.array([np.random.randn(1) for i in t])
		return np.cos(2 * np.pi * t / 10.)

	def func2(t):
		return np.sin(1.3 * np.pi * t / 10.)

	if isfunc1:
		return func1
	return func2

#function that returns the location of a volcano that erupted during an array of different time frames
def volc_location(n,t=None):
	x = np.random.randint(0,1700,n)
	y = np.random.randint(0,1000,n)
	return x,y

t        = np.linspace(0, 80, 400)
map_name = 'world_map.png'
ani      = SubplotAnimation("Volcano Data Explorer \n",t,func(True),func(False),map_name,volc_location)
#ani.save('test_sub.mp4')
plt.show()
