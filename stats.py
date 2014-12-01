import numpy as np

def meanXY(array_of_phases):
	#assumes phases in radians
	x = np.cos(list_of_phases).sum()/len(list_of_phases)
	y = np.sin(list_of_phases).sum()/len(list_of_phases)
	return x,y
	
def meanVec(array_of_phases):
	x,y = getMeanXY(list_of_phases)
	r = np.sqrt(x**2 + y**2)
	return r

def meanAngle(array_of_phases):
	#returns theta in radians
	x,y = getMeanXY(list_of_phases)
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
	r = meanAngle(list_of_phases)
	p = np.exp(-(r**2)*len(list_of_phases))
	return p
	
def rose_plot(array_of_phases, bins, figsize, rgrids, rlabel_pos, theta_grids, color):

	###finish this
	fig = plt.figure(figsize = figsize)
	p = fig.add_subplot(111, polar = True)
	#p.set_theta_zero_location('N')
	#p.set_theta_direction(-1)
	p.set_rgrids(rgrids)
	p.set_rlabel_position(rlabel_pos)
	p.set_theta_grids(theta_grids)
	hist, bin_edges = np.histogram(array_of_phases, bins)
	
	
	
	
