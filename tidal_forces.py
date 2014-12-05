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
	
def findMax(tide_array, minimum, maximum, tide):
    ind = np.argmax(tide_array[minimum:maximum+1, column])
	while (ind == maximum) or (ind == minimum):
		cycle = period
	if ind == maximum:
	    
	while slope != zero:
	    if maximu
		new_max = maximum - time
		ind = np.argmax(tide_array[minimum:new_max+1,column])
	return ind
	
def periodMax(tide_array, period, column):
	#tide = mf, mm, ssa, diurnal, or semi
	# mf = moon fortnightly, mm = moon monthly, ssa = solar semiannual, diurnal = daily, semi = twice daily
    cycle = 1.6*period
    minimum = np.around(15000-(cycle*100./2),0)
    maximum = np.around(15000+(cycle*100./2),0)
    ind = np.argmax(tide_array[minimum:maximum+1,column])
    max_t = tide_array[ind+minimum,0]
    max_amp = tide_array[ind+minimum,column]
    return max_t, max_amp

def periodPhase(tide_array, tide):
    if tide == 'mf':
        period = 13.66
        column = 1
    elif tide == 'mm':
	    period = 27.56
	    column = 1
    elif tide == 'ssa':
        period = 182.5
        column = 1
    elif tide == 'diurnal':
        period = 15.
        column = 2
    elif tide == 'semi':
        period = 30.
        column = 3
    erup_t = tide_array[15000,0]
    t_max = periodMax(tide_array,period=period,column=column)[0]
    phase = (360./period)*(erup_t - t_max)
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

# def mmPeriodMax(tide_array, period = 27.56):
	# #Mm is the monthly tide --27.56
    # min = np.around(15000-(period*100./2),0)
    # max = np.around(15000+(period*100./2),0)
    # ind = np.argmax(tide_array[min:max+1,1])
    # max_t = tide_array[ind,0]
    # max = tide_array[ind,1]
    # return max_t, max

# def mmPeriodPhase(tide_array, period = 27.56):
	# # the major long period tide is 27.555 days
    # erup_t = tide_array[15000,0]
    # t_max = mmPeriodMax(tide_array)[0]
    # phase = (360./period)*(erup_t - t_max)
    # return phase

# def mmPhasesDict(tide_dict):
    # mmPhaseDict = {}
    # for key in tide_dict:
	    # mmPhaseDict[key] = mmPeriodPhase(tide_dict[key])
    # return mmPhaseDict	
	
# def ssaPeriodMax(tide_array, period = 182.5):
	# #Ssa is the solar semi annual tide --- 182.5
    # min = np.around(15000-(period*100./2),0)
    # max = np.around(15000+(period*100./2),0)
    # ind = np.argmax(tide_array[min:max+1,1])
    # max_t = tide_array[ind,0]
    # max = tide_array[ind,1]
    # return max_t, max

# def ssaPeriodPhase(tide_array, period = 182.5):
	# # the major ssa tide is 182.5 days (.5 years)
    # erup_t = tide_array[15000,0]
    # t_max = ssaPeriodMax(tide_array)[0]
    # phase = (360./period)*(erup_t - t_max)
    # return phase

# def ssaPhasesDict(tide_dict):
    # ssaPhaseDict = {}
    # for key in tide_dict:
	    # ssaPhaseDict[key] = ssaPeriodPhase(tide_dict[key])
    # return ssaPhaseDict	

# def diurnalPeriodMax(tide_array, period = 15):
    # min = np.around(15000-(period*100./2),0)
    # max = np.around(15000+(period*100./2),0)
    # ind = np.argmax(tide_array[min:max+1,2])
    # max_t = tide_array[ind,0]
    # max = tide_array[ind,2]
    # return max_t, max

# def diurnalPeriodPhase(tide_array, period = 15):
	# # the diurnal phase is approximately 15 days
    # erup_t = tide_array[15000,0]
    # t_max = diurnalPeriodMax(tide_array)[0]
    # phase = (360./period)*(erup_t - t_max)
    # return phase

# def diurnalPhasesDict(tide_dict):
    # diurnalPhaseDict = {}
    # for key in tide_dict:
	    # diurnalPhaseDict[key] = diurnalPeriodPhase(tide_dict[key])
    # return diurnalPhaseDict
	
# def semiPeriodMax(tide_array, period = 30):
    # min = np.around(15000-(period*100./2),0)
    # max = np.around(15000+(period*100./2),0)
    # ind = np.argmax(tide_array[min:max+1,3])
    # max_t = tide_array[ind,0]
    # max = tide_array[ind,3]
    # return max_t, max

# def semiPeriodPhase(tide_array, period = 30):
    # erup_t = tide_array[15000,0]
    # t_max = semiPeriodMax(tide_array)[0]
    # phase = (360./period)*(erup_t - t_max)
    # return phase

# def semiPhasesDict(tide_dict):
    # semiPhaseDict = {}
    # for key in tide_dict:
	    # semiPhaseDict[key] = semiPeriodPhase(tide_dict[key])
    # return semiPhaseDict
    
