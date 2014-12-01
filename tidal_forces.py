import os
import numpy as np
from tidal import tidal

def iter_tides(df, sjd_col, dlat_col, dlon_col, erup_col):
	"""Returns dictionary of arrays of tidal forces given a pandas dataframe.
	"""
	tide_dict = {}
	for erup_number in df[erup_col]:
                tide_dict[erup_number] = calculate_tide(df[df[erup_col]==erup_number].iloc[0][sjd_col],
								df[df[erup_col]==erup_number].iloc[0][dlat_col],
								df[df[erup_col]==erup_number].iloc[0][dlon_col])
	return tide_dict
	
	
def calculate_tide(sjd=2452262, dlat=15, dlon=15):
    """ Returns arrays of tidal forces given the julian day, latitude,
    longitude."""
    
    output_file = 'out.txt'
    outfile = os.open(output_file, os.O_RDWR|os.O_CREAT)
    save = os.dup(1)
    os.dup2(outfile,1)

    #run file
    tidal.tidal(sjd, dlat, dlon)
    os.dup2(save,1)
    os.close(outfile)

    #save as numpy array
    tides = np.loadtxt(output_file)
    os.remove(output_file)
    return tides
	
def longPeriodMax(tide_array):
    # should change this to find the first max, could be 2 max's in 30 days
    ind = np.argmax(tide_array[:3000,1])
    max = tide_array[ind,1]
    return ind, max

def longPeriodPhase(tide_array):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = longPeriodMax(tide_array)
    phase = (360./27.555)*(t_max - erup_t)
    return phase

def longPeriodPhases(tide_dict):
    longPhaseDict = {}
    for key in tide_dict:
	    longPhaseDict[key] = longPeriodPhase(tide_dict[key])
    return longPhaseDict		
    
