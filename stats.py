#to run and test this file go down to the bottom, right under main, 
#and change phase_length and phase_diff (to be in the range of phase length). 
#This works by subtracting out the sine model from the main curve and determining 
#what the true phase is. If the true phase of the eruptions matches with one of the forces,
# we can associate that with a p-value 

import numpy as np
import scipy.stats as stat
import time_model
import matplotlib.pyplot as plt
import sys

def meanXY(array_of_phases):
	#assumes phases in radians
	x = np.cos(array_of_phases).sum()/len(array_of_phases)
	y = np.sin(array_of_phases).sum()/len(array_of_phases)
	return x,y
	
def meanVec(array_of_phases):
	x,y = meanXY(array_of_phases)
	y = np.sin(array_of_phases).sum()/len(array_of_phases)
	return x,y
	
def meanVec(array_of_phases):
	x,y = meanXY(array_of_phases)
	r = np.sqrt(x**2 + y**2)
	return r

def circularVar(array_of_phases):
	r =  meanVec(array_of_phases)
	v = 1-r
	return value

def circularStd(array_of_phases):
	r = meanVec(array_of_phases)
	std = np.sqrt(-2*np.log(r))
	return std

def meanAngle(array_of_phases):
	#returns theta in radians
	x,y = meanXY(array_of_phases)
	x,y = meanXY(array_of_phases)
	theta = np.arctan(y/x)
	if (x<0) & (y>0):
		theta = np.pi - theta 
	elif (x<0) & (y<0):
		theta = np.pi + theta
	elif (x>0) & (y<0):
		theta = 2*np.pi - theta
	return theta
	
def rayleighTest(array_of_phases):
	"""Returns rayleigh and modified rayleigh test value."""
	n = len(array_of_phases)
	r = meanVec(array_of_phases)
	ray = 2*n*(r**2)
	mod_ray = ((1.-(1./(2.*n)))*2.*n*(r**2)) + (n*(r**4)/2.)
	return ray,mod_ray
	
def rayleigh_prob(array_of_phases):
	r = meanAngle(array_of_phases)
	p = np.exp(-(r**2)*len(array_of_phases))
	return p
	
# rose_plot(array_of_phases, bins, figsize, rgrids, rlabel_pos, theta_grids, color):

	###finish this
	#fig = plt.figure(figsize = figsize)
	#p = fig.add_subplot(111, polar = True)
	#p.set_theta_zero_location('E')
	#p.set_theta_direction(-1)
	#p.set_rgrids(rgrids)
	#p.set_rlabel_position(rlabel_pos)
	#p.set_theta_grids(theta_grids)
	#hist, bin_edges = np.histogram(array_of_phases, bins)
	
"""	
#worked on this but did not like the direction it was going - so I started on the project below
class CorrelationTest:
	#data should already be segmented into phases
	#ex: [[1,2,3,4],[2,3,56,2],[23,3,33,2]]
	#ex: [[j1 k1, j1 k2, j1 k3, ...],[j2 k1, j2 k2, j2 k3,...]]
	#i = series# (1 to W), j = observation# (1 to T), k= phase# (1 to P)
	#In this example, the data is split into 3 buckets (hence 3 different phases)
	def __init__(self,series1=None,series2=None):
		self.series1 = series1
		self.series2 = series2

	def standardize(self,series):
		data = []
		for s in series:
			mean = np.mean(s)
			std = np.std(s)
			data.append((s-mean)/std)
		return np.array(data)

	def season_means(self,data1,data2):
		data = (data1 + data2)/2
		return np.mean(data,axis=1)
	#no change for standardize data			
	def season_residuals(self,data1,data2,dsm,isStand=False):
		if isStand:
			return data1,data2		
		ndata1 = []
		ndata2 = []
		data1 = np.transpose(data1)
		data2 = np.transpose(data2)
		for d1,d2 in zip(data1,data2):
			ndata1.append(d1-dsm)
			ndata2.append(d2-dsm)
		return np.array(ndata1),np.array(ndata2)
	#accepts a 1 dimensional series
	def test_for_normality(self,data):	
		_ , p = stat.shapiro(data)
		return p
	def test_for_equal_var(self,data1,data2):	
		_ , p = stat.bartlett(data1,data2)
		return p
	def mse(self,data1,data2,w=1,t=1,k=1):
		data = data1**2 + data2**2
		def sum_func(x,a):
			return np.sum(x,axis=a)
		s = sum_func
		return np.apply_over_axes(s,data,[0,1])[0][0]/(t*(w*k-1))

	def mst(self,smeans,data1,data2,t=1):
		a = np.sum(np.sum((np.transpose(data1) -smeans)**2))/(t-1)
		return a+np.sum(np.sum((np.transpose(data2) -smeans)**2))/(t-1)
		
if __name__ == '__main__':
	
	j = 6 #number of sampling events per phase
	k = 4 #number of seasons

	data1 = np.random.rand(j,k) * 10
	data2 = np.random.rand(j,k) * 15 + np.random.rand(j,k) * 3
	
	c = CorrelationTest()

	data1_s = c.standardize(data1)
	data2_s = c.standardize(data2)

	smeans = c.season_means(data1_s,data2_s)
	assert(np.max(np.shape(smeans))==j)
	d1_resi,d2_resi = c.season_residuals(data1_s,data2_s,smeans,True)
	print d2_resi
	p_eq_var = []
	for i1 in d1_resi:
		norm_results = c.test_for_normality(i1)
		if norm_results < .05:
			print "This is normal"
		else:
			print "This is not normal"
		for i2 in d2_resi:
			print c.test_for_equal_var(i1,i2)
			if c.test_for_equal_var(i1,i2) < .05:
				print "Variances are equal",np.var(i1),np.var(i2)
			else:
				print "Variances are not equal",np.var(i1),np.var(i2)
		

	p_eq_var #holds p-values for each phase
	#if any p-value is below .05 then we have reason to doubt that the variances are equal
	w,t,k = 2,j,k
	mse = c.mse(d1_resi,d2_resi,w,t,k)	
	mst = c.mst(smeans,d1_resi,d2_resi,t)	
	F = mse/mst
	alpha = .05

	for d1,d2 in zip(d1_resi,d2_resi):
		f,p = stat.f_oneway(d1,d2)
		print "F:",f
		print "p-value:",p
		if p < alpha:
			print "Significant seasonal pattern exist"
		else:
			print "Significant seasonal pattern does not exist"
		print
"""

#New direction: Will use the normal test after subtracting sine model out (test to see if the error is random)
#copies the amplitude of data and then recreates a sine model which is then subtracted from the original
#model can be tuned and adjusted to match and seasons and get rid of series in the data, then when ready can be subtracted.
#the residuals are tested for normality
class TestPhaseSimilarity:
	#x - x data to copy
	#y - y data to copy
	#phase - phase of model that will be created
	def __init__(self,x,y,phase,amp=None,shift=0):
		self.initial_data = [x,y]
		self.phase = phase
		self.data = [x,y-np.mean(y)] #subtracting the mean centers data on x-axis
		self.shift = shift
		self.amp = amp
		self.my = self.amp*np.sin((self.data[0]*self.phase)-self.shift) 
	def get_model(self):
		return self.my
	def add_to_model(self,phase=1,shift=0,amp=1):
		self.my = self.my + amp*np.sin(x*phase-shift)
	def sub_from_model(self,phase=1,shift=0,amp=1):
		self.my = self.my - amp*np.sin(x*phase-shift)
	def modify_model(self,phase=1,shift=0,amp=1):
		self.my = amp*np.sin(x*phase-shift)
	#use to subtract out any non-sign data
	def get_data(self):
		return self.data[1]
	def revert_data_to_original(self):
		self.data[1] = self.initial_data[1]
	def plot_data_and_model(self):
		plt.plot(self.data[0],self.data[1],'r-',label='Data')
		plt.plot(self.data[0],self.my,'b-',label='Model')
		plt.show()
	def test(self):
		_ , p = stat.shapiro(self.data[1]-self.my)
		if p < .05:
			#reject null hypothesis - data is not normal -- phases are not equal
			return p,False,self.data[1]
		else:
			#data is normal -- phases are equal
			return p,True,self.data[1]
			
if __name__ == '__main__':
	#import data -- here I construct an artificial data model
	phase_length = .026
	#we want to search for the phase_length by iterating through values before and after the range. A spike in the p-value past .05, means there is a pretty good chance we have found the right phase
	phase_diff = np.linspace(0.02,.04,50)



	x = np.linspace(0,1000,500)
	#create model with random noise
	y = np.sin(x*phase_length) + [p*q for p,q in zip(np.random.uniform(-3,3,len(x)),np.random.uniform(-.20,.20,len(x)))]
	#plt.plot(x,y)
	#plt.show()
	#sys.exit(0)

	phase_results = []
	for pd in phase_diff:
		t = TestPhaseSimilarity(x,y,pd,1,0)
		#t.plot_data_and_model() #subtracts out sine from curve so you are left with noise. Then we do a test to see if the "noise" is normal 
		p,valid,data = t.test()
		phase_results.append([pd,p])
		print p
		if valid:
			pass
			print "Phases are equal.  P-value:",p 
		else:
			pass
			print "We don't believe phases are equal.  P-value:",p 
	
	pr = np.array(phase_results)
	plt.plot(pr[:,0],pr[:,1],'b-')
	plt.show()

