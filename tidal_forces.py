import os
import numpy as np
from tidal import tidal

def iter_tides(df, sjd_col, dlat_col, dlon_col, erup_col):
	"""Returns dictionary of arrays of tidal forces given a pandas dataframe.
	"""
	tide_dict = {}
	for p,q,r,s in zip(df[erup_col].values, df[sjd_col].values, df[dlat_col].values, df[dlon_col].values):
		tide_dict[p]=calculate_tide(q,r,s)
		
	#for erup_number in df[erup_col]:
				
                #tide_dict[erup_number] = calculate_tide(df[df[erup_col]==erup_number].iloc[0][sjd_col],
								#df[df[erup_col]==erup_number].iloc[0][dlat_col],
								#df[df[erup_col]==erup_number].iloc[0][dlon_col])
	return tide_dict
	
	
def calculate_tide(sjd, dlat, dlon):
    """ Returns arrays of tidal forces given the julian day, latitude,
    longitude."""
    
    output_file = 'tidal_info.txt'
    #outfile = os.open(output_file, os.O_RDWR|os.O_CREAT)
    #save = os.dup(1)
    #os.dup2(outfile,1)

    #run file
    tidal(sjd, dlat, dlon)
    #os.dup2(save,1)
    #os.close(outfile)

    #save as numpy array
    tides = np.loadtxt(output_file)
    os.remove(output_file)
    return tides
	
def mfPeriodMax(tide_array):
	#Mf is the fortnightly tide
    # should change this to find the first max, could be 2 max's in 30 days
    ind = np.argmax(tide_array[:1400,1])
    max = tide_array[ind,1]
    return ind, max

def mfPeriodPhase(tide_array, period = 13.66):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = mfPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def mfPhasesDict(tide_dict):
    mfPhaseDict = {}
    for key in tide_dict:
	    mfPhaseDict[key] = mfPeriodPhase(tide_dict[key])
    return mfPhaseDict

def mmPeriodMax(tide_array):
	#Mm is the monthly tide
    ind = np.argmax(tide_array[:2800,1])
    max = tide_array[ind,1]
    return ind, max

def mmPeriodPhase(tide_array, period = 27.56):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = mmPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def mmPhasesDict(tide_dict):
    mmPhaseDict = {}
    for key in tide_dict:
	    mmPhaseDict[key] = mmPeriodPhase(tide_dict[key])
    return mmPhaseDict	
	
def ssaPeriodMax(tide_array):
	#Ssa is the solar semi annual tide
    ind = np.argmax(tide_array[:18300,1])
    max = tide_array[ind,1]
    return ind, max

def ssaPeriodPhase(tide_array, period = 182.5):
	# the major ssa tide is 182.5 days (.5 years)
    erup_t = tide_array[0,0]
    t_max = ssaPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def ssaPhasesDict(tide_dict):
    mmPhaseDict = {}
    for key in tide_dict:
	    ssaPhaseDict[key] = ssaPeriodPhase(tide_dict[key])
    return mmPhaseDict	

def diurnalPeriodMax(tide_array):
    # should change this to find the first max, could be 2 max's in 30 days
    ind = np.argmax(tide_array[:1600,2])
    max = tide_array[ind,2]
    return ind, max

def diurnalPeriodPhase(tide_array, period = 15):
	# the diurnal phase is approximately 15 days
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
    ind = np.argmax(tide_array[:3100,2])
    max = tide_array[ind,3]
    return ind, max

def semiPeriodPhase(tide_array, period = 30):

    erup_t = tide_array[0,0]
    t_max = semiPeriodMax(tide_array)
    phase = (360./period)*(t_max - erup_t)
    return phase

def semiPhasesDict(tide_dict):
    semiPhaseDict = {}
    for key in tide_dict:
	    semiPhaseDict[key] = semiPeriodPhase(tide_dict[key])
    return semiPhaseDict
    
