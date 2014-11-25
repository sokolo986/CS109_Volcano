import numpy as np
#accepts a lat and long and converts it to a position on the map

def convert_loc_to_map(lat,lon,px_x,px_y,map_l_lat,map_u_lat,map_l_lon,map_u_lon,map_file):
	#mat_x_lxx = The actual latitude/longitude that the map starts and ends with along a certain axis
	
	#get length and width of the picture through np
	#determine the width/px use it to calculate the px location of a given lat/lon
	#return the map conversion of the given lat and long for the picture
	#create class -- one that accepts a file and stores the width/height
	#another that does the conversion
	#another that outputs the data point conversion for a lat and lon on an axis
