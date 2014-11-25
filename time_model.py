import numpy as np
import pandas as pd
import sys
import math
import matplotlib.pyplot as plt

# need to take into account the calculation for w0 - need to find out why my solution for pseudo inverse is producing a line, need t incorporate the regularization constants

# extract data from csv
def extract(filename):
	return pd.read_csv(filename,header=True,sep=',')

# preprocessor which standardizes the data before processing is done 
def standardize(array):
  mean = np.mean(array,0)
  return (array - mean)/np.std(array,0)
 
# returns the polynomial basis function transformation for a given input x
def basis(x,w):
	return [w[i]*(x**i) for i in xrange(len(w))]

# returns the polynomial basis function transformation for a given input x
def basis_sinusodial(x,w):
	return [w[i]*math.sin(math.pi*i*x) for i in xrange(len(w))]

# given an array transforms it into basis approximation
# def transform_with_basis(array):
#	return np.apply_along_axis(basis,0,array)

# takes vector t and w and turns transforms from basis functions
def matrix(t,w,isPoly=True):
	N = len(t)
	mat = [[]]*N
	for i in range(N):
		if isPoly:
			mat[i] = basis(t[i],w)
		else:
			mat[i] = basis_sinusodial(t[i],w)
	mat = np.array(mat)
	return mat

# solves for w by computing the Moore-Penrose pseduo inverse of the design matrix
# or uses a weight decay for weight decay calculations
def compute_w(design,t,decayWeight=False,lamConstant=5):
	if not decayWeight:
		return (np.linalg.pinv(design)).dot(t)
	else:
		lam = np.diag([lamConstant for i in xrange(len(design[0,:]))])
		inv = np.linalg.inv(np.diag(lam)+(np.transpose(design).dot(design)))
		return (inv).dot(np.transpose(design).dot(t))

def error(t,t_new,constant):
	return np.sum(((1.0/constant) * (t-t_new)**2))

# Plots distortion versus run number
def show(in_fun,out_fun,title):
	plt.plot(in_fun,out_fun,'r-')
	plt.title(title)
	plt.xlabel("Order")
	plt.ylabel("Error")
	plt.show()

def showCharts(in_fun, out_fun,yerr,title,x_lab,y_lab):
  plot_array = []
  plot_array.append(plt.plot(in_fun[:,0],in_fun[:,1],'bo'))
  color_array = ['g--','r--','y--','c--','d--','m--','k--']
  j = 0
  for i in out_fun:
    plot_array.append(plt.errorbar(in_fun[:,0],i,yerr,color_array[j],yerr=5))
    j += 1
  plt.title(title)
  plt.xlabel(x_lab)
  plt.ylabel(y_lab)
  plt.show()

def showCharts(in_fun, out_fun,title,x_lab,y_lab):
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

if __name__ == '__main__':

	#data = np.array(extract('motorcycle.csv'))
	data = [[1,2],[3,2],[4,5],[5,7],[8,5],[9,10]]
	data = standardize(data)
	order = [4,5,6,7,8,9,10] #where order[x] == max polynomial of x**(order[x]-1)
	order_predictions,err,beta = ([],[],[])

	poly = False  #if false uses the sinusodial basis
	weightDecay = True #if false then no weight decay is used
	lamConst = 10 #weight constant to use for to reduce weights -> higher constant causes weights to decay to 0

	for i in xrange(len(order)):
		w = np.ones(order[i])
		design_matrix = matrix(data[:,0],w,poly)	
		w = compute_w(design_matrix,data[:,1],weightDecay,lamConst)	
		order_predictions.append(np.sum(matrix(data[:,0],w,poly),1))
		err.append(error(data[:,1],order_predictions[i],2))
		beta.append(error(data[:,1],order_predictions[i],len(data)))
		print "Error of an order",order[i],"Error:",err[i],"Variance:",beta[i]

	showCharts(data,np.array(order_predictions),"Target and Predictions using "+str(len(order_predictions))+" Sinusoidal Model","time (t)","number of eruptions")
	show(order,err,"Error by Order")


