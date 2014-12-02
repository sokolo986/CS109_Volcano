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
	
	
def calculate_tide(sjd, dlat, dlon):
    """ Returns arrays of tidal forces given the julian day, latitude,
    longitude."""
    
    output_file = 'out.txt'
    outfile = os.open(output_file, os.O_RDWR|os.O_CREAT)
    save = os.dup(1)
    os.dup2(outfile,1)

    #run file
    tidal(sjd, dlat, dlon)
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

def longPeriodPhase(tide_array, period = 27.555):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = longPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def longPhasesDict(tide_dict):
    longPhaseDict = {}
    for key in tide_dict:
	    longPhaseDict[key] = longPeriodPhase(tide_dict[key])
    return longPhaseDict

def diurnalPeriodMax(tide_array):
    # should change this to find the first max, could be 2 max's in 30 days
    ind = np.argmax(tide_array[:3000,2])
    max = tide_array[ind,2]
    return ind, max

def diurnalPeriodPhase(tide_array, period = 27.555):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = diurnalPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def diurnalPhasesDict(tide_dict):
    diurnalPhaseDict = {}
    for key in tide_dict:
	    diurnalPhaseDict[key] = diurnalPeriodPhase(tide_dict[key])
    return diurnalPhaseDict
	
def semiPeriodMax(tide_array):
    # should change this to find the first max, could be 2 max's in 30 days
    ind = np.argmax(tide_array[:3000,2])
    max = tide_array[ind,3]
    return ind, max

def semiPeriodPhase(tide_array, period = 27.555):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = semiPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def semiPhasesDict(tide_dict):
    semiPhaseDict = {}
    for key in tide_dict:
	    semiPhaseDict[key] = semiPeriodPhase(tide_dict[key])
    return semiPhaseDict
    
