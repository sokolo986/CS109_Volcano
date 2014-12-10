import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

class TimeModeler:
	def __init__(self,data,max_order=10,weightDecay=True,lamconst=10):
		self.data = self._standardize(data)
		self.order = np.arange(4,max_order+1)
		self.order_predictions,self.err = ([],[])

		self.poly = False  #if false uses the sinusodial basis
		self.weightDecay = weightDecay #if false then no weight decay is used
		self.lamConst = lamconst #weight decay constant 

	# preprocessor which standardizes the data before attempting to use the model 
	def _standardize(self,array):
		mean = np.mean(array,0)
		return (array - mean)/np.std(array,0)

	# returns the polynomial basis function transformation for a given input x
	def _basis_poly(self,x,w):
		return [w[i]*(x**i) for i in xrange(len(w))]

	# returns the linear basis function transformation for a given input x
	def _basis_lin(self,x,w):
		return [w[i]*(x) for i in xrange(len(w))]

	# returns the sinusoidal basis function transformation for a given input x
	def _basis_sinusodial(self,x,w):
		return np.array([w[i-1]*np.sin(np.pi*i*x) for i in np.arange(1,len(w)+1)])

	# takes vector t and w and turns transforms from basis functions
	def _matrix(self,t,w,isPoly=True):
		N = len(t)
		mat = [[]]*N
		for i in range(N):
			if isPoly:
				mat[i] = self._basis_poly(t[i],w)
			else:
				mat[i] = self._basis_sinusodial(t[i],w)
		mat = np.array(mat)
		return mat

	# solves for w by computing the Moore-Penrose pseduo inverse of input/output
	def _compute_w(self,design,t,decayWeight=False,lamConstant=5):
		if not decayWeight:
			return (np.linalg.pinv(design)).dot(t)
		else:
			lam = np.diag([lamConstant for i in xrange(len(design[0,:]))])
			inv = np.linalg.inv(np.diag(lam)+(np.transpose(design).dot(design)))
			return (inv).dot(np.transpose(design).dot(t))

	def _error(self,t,t_new,constant):
		return np.sum(((1.0/constant) * (t-t_new)**2))

	def _show(self,in_fun,out_fun,title):
			plt.plot(in_fun,out_fun,'r-')
			plt.title(title)
			plt.xlabel("Order")
			plt.ylabel("Error")
			plt.show()

	def _showCharts(self,in_fun, out_fun,title,x_lab,y_lab):
		plot_array = []
		plot_array.append(plt.plot(in_fun[:,0],in_fun[:,1],'bo'))
		color_array = ['g--','r--','y--','c--','d--','m--','k--']
		j = 0
		for i in out_fun:
			plot_array.append(plt.plot(in_fun[:,0],i,color_array[j]))
			j += 1
		plt.title(title)
		plt.xlabel(x_lab)
		plt.ylabel(y_lab)
		plt.show()

	#withCharts determine if an output of the plots are displayed
	def compute(self,withCharts=True):
		for i in xrange(len(self.order)):
			w = np.ones(self.order[i])
			design_matrix = self._matrix(self.data[:,0],w,self.poly)	
			w = self._compute_w(design_matrix,self.data[:,1],self.weightDecay,self.lamConst)	
			self.order_predictions.append(np.sum(self._matrix(self.data[:,0],w,self.poly),1))
			self.err.append(self._error(data[:,1],self.order_predictions[i],len(self.data)))
			#print "Order:",self.order[i],"Error:",self.err[i],"W:",w

		if withCharts:
			self._showCharts(self.data,np.array(self.order_predictions),"Target and Predictions using "+str(len(self.order_predictions))+" Sinusoidal Model","time (t)","number of eruptions")
			self._show(self.order,self.err,"Error by Order")
		return w


if __name__ == '__main__':

	#create artificial data
	x = np.linspace(1,50,400)
	y = .4 * np.sin(np.pi * .4* x) + .5* np.sin(np.pi * .5 * x) + np.random.rand(1,len(x))[0]
	data = np.array(zip(x,y))
	
	#compute function
	sin = TimeModeler(data,lamconst=5)
	#sin.compute() #uncomment to see result

