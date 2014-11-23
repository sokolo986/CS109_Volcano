import os
import numpy as np
import tidal

def eruption_tides(sjd, dlat, dlon):
    """ Returns arrays of tidal forces given the julian day, latitude,
    longitude."""
    
    output_file = 'out.txt'
    outfile = os.open(output_file, os.O_RDWR|os.O_CREAT)
    save = os.dup(1)
    os.dup2(outfile,1)
    #parameters
    sjd = 2452262
    dlat = 15
    dlon = 15
    #run file
    tidal.tidal(sjd, dlat, dlon)
    os.dup2(save,1)
    os.close(outfile)
    #save as numpy array
    tides = np.loadtxt(output_file)
    return tides
    
