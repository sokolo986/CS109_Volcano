import os
import numpy as np
from tidal import tidal

def iter_tides(df, sjd_col, dlat_col, dlon_col, erup_col):
	"""Returns dictionary of arrays of tidal forces given a pandas dataframe.
	"""
	tide_dict = {}
	for p,q,r,s in zip(df[erup_col].values, df[sjd_col].values-150, df[dlat_col].values, df[dlon_col].values):
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
	
def mfPeriodMax(tide_array, period = 13.66):
	#Mf is the fortnightly tide - - 13.66
    min = np.around(15000-(period*100./2),0)
    max = np.around(15000+(period*100./2),0)
    ind = np.argmax(tide_array[min:max+1,1])
    max_t = tide_array[ind,0]
    max = tide_array[ind,1]
    return max_t, max

def mfPeriodPhase(tide_array, period = 13.66):
    erup_t = tide_array[0,0]
    t_max = mfPeriodMax(tide_array)[0]
    phase = (360./period)*(t_max - erup_t)
    return phase

def mfPhasesDict(tide_dict):
    mfPhaseDict = {}
    for key in tide_dict:
	    mfPhaseDict[key] = mfPeriodPhase(tide_dict[key])
    return mfPhaseDict

def mmPeriodMax(tide_array, period = 27.56):
	#Mm is the monthly tide --27.56
    min = np.around(15000-(period*100./2),0)
    max = np.around(15000+(period*100./2),0)
    ind = np.argmax(tide_array[min:max+1,1])
    max_t = tide_array[ind,0]
    max = tide_array[ind,1]
    return max_t, max

def mmPeriodPhase(tide_array, period = 27.56):
	# the major long period tide is 27.555 days
    erup_t = tide_array[0,0]
    t_max = mmPeriodMax(tide_array)[0]
    phase = (360./period)*(t_max - erup_t)
    return phase

def mmPhasesDict(tide_dict):
    mmPhaseDict = {}
    for key in tide_dict:
	    mmPhaseDict[key] = mmPeriodPhase(tide_dict[key])
    return mmPhaseDict	
	
def ssaPeriodMax(tide_array, period = 182.5):
	#Ssa is the solar semi annual tide --- 182.5
    min = np.around(15000-(period*100./2),0)
    max = np.around(15000+(period*100./2),0)
    ind = np.argmax(tide_array[min:max+1,1])
    max_t = tide_array[ind,0]
    max = tide_array[ind,1]
    return max_t, max

def ssaPeriodPhase(tide_array, period = 182.5):
	# the major ssa tide is 182.5 days (.5 years)
    erup_t = tide_array[0,0]
    t_max = ssaPeriodMax(tide_array)[0]
    phase = (360./period)*(t_max - erup_t)
    return phase

def ssaPhasesDict(tide_dict):
    ssaPhaseDict = {}
    for key in tide_dict:
	    ssaPhaseDict[key] = ssaPeriodPhase(tide_dict[key])
    return ssaPhaseDict	

def diurnalPeriodMax(tide_array, period = 15):
    min = np.around(15000-(period*100./2),0)
    max = np.around(15000+(period*100./2),0)
    ind = np.argmax(tide_array[min:max+1,2])
    max_t = tide_array[ind,0]
    max = tide_array[ind,2]
    return max_t, max

def diurnalPeriodPhase(tide_array, period = 15):
	# the diurnal phase is approximately 15 days
    erup_t = tide_array[0,0]
    t_max = diurnalPeriodMax(tide_array)[0]
    phase = (360./period)*(t_max - erup_t)
    return phase

def diurnalPhasesDict(tide_dict):
    diurnalPhaseDict = {}
    for key in tide_dict:
	    diurnalPhaseDict[key] = diurnalPeriodPhase(tide_dict[key])
    return diurnalPhaseDict
	
def semiPeriodMax(tide_array, period = 30):
    min = np.around(15000-(period*100./2),0)
    max = np.around(15000+(period*100./2),0)
    ind = np.argmax(tide_array[min:max+1,3])
    max_t = tide_array[ind,0]
    max = tide_array[ind,3]
    return max_t, max

def semiPeriodPhase(tide_array, period = 30):
    erup_t = tide_array[0,0]
    t_max = semiPeriodMax(tide_array)[0]
    phase = (360./period)*(t_max - erup_t)
    return phase

def semiPhasesDict(tide_dict):
    semiPhaseDict = {}
    for key in tide_dict:
	    semiPhaseDict[key] = semiPeriodPhase(tide_dict[key])
    return semiPhaseDict
    
