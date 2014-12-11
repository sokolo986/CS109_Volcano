import os
import numpy as np
from tidal import tidal

def iter_tides(df, sjd_col, dlat_col, dlon_col, erup_col):
	"""Returns dictionary of arrays of tidal forces given a pandas dataframe.
	"""
	tide_dict = {}
	for p,q,r,s in zip(df[erup_col].values, df[sjd_col].values-150, df[dlat_col].values, df[dlon_col].values):
		tide_dict[p]=calculate_tide(q,r,s)

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

def findMax(tide_array, cycle, column, tide):
# for long period cycles if the max is at the end then it is probably on a slo
    minimum = np.around(15000-(cycle*100./2),0)
    maximum = np.around(15000+(cycle*100./2),0)
    ind = np.argmax(tide_array[minimum:maximum+1, column])
    time_shift = 0.05*cycle
    if (tide == 'semi') | (tide == 'diurnal') | (tide == 'ssa'):
        #time shift out
        while (ind+minimum == maximum) | (ind+minimum == minimum):
            if minimum+ind == maximum:
			    maximum = np.around(maximum +time_shift,0)
            elif minimum+ind == minimum:
                minimum = np.around(minimum - time_shift,0)
            ind = np.argmax(tide_array[minimum:maximum+1,column])
    else:
        #time shift in
        while (ind+minimum == maximum) | (ind+minimum == minimum):
            if minimum+ind == maximum:
                maximum = np.around(maximum - time_shift,0)
            elif minimum+ind == minimum:
                minimum = np.around(minimum + time_shift,0)
            ind = np.argmax(tide_array[minimum:maximum+1,column])
    final_ind = minimum+ind
    return final_ind

	
def periodMax(tide_array, cycle, column, tide):
    column = column
    #tide = mf, mm, ssa, diurnal, or semi
    # mf = moon fortnightly, mm = moon monthly, ssa = solar semiannual, diurnal = daily, semi = twice daily
    cycle = cycle
    # minimum = np.around(15000-(cycle*100./2),0)
    # maximum = np.around(15000+(cycle*100./2),0)
    # ind = np.argmax(tide_array[minimum:maximum+1,column])
    ind = findMax(tide_array, cycle, column, tide)
    max_t = tide_array[ind,0]
    max_amp = tide_array[ind,column]
    return max_t, max_amp

def periodPhase(tide_array, tide):
    if tide == 'mf':
        period = 13.66
        column = 1
        cycle = 1.5*period
    elif tide == 'mm':
        period = 27.56
        column = 1
        cycle = 1.5*period
    elif tide == 'ssa':
        period = 182.5
        column = 1
        cycle = 1.*period
    elif tide == 'diurnal':
        period = 15.
        column = 2
        cycle = 1.*period
    elif tide == 'semi':
        period = 30.
        column = 3
        cycle = 1.*period
    erup_t = tide_array[15000,0]
    max_t = periodMax(tide_array,cycle = cycle,column=column, tide = tide)[0]
    phase = (360./period)*(erup_t - max_t)
    if phase>180.0:
        phase = phase-360
    if phase<-180.0:
        phase = phase+360	
    return phase

def phasesDict(tide_dict,tide):
    phaseDict = {}
    for key in tide_dict:
	    phaseDict[key] = periodPhase(tide_dict[key],tide)
    return phaseDict

