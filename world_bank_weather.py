#returns empty json - submitted a ticket

import json
import requests
#from tidal_forces import calculate_tide as tide_calc

class Climate:
	def __init__(self):
		pass
	def get_weather_data(self,type_u,start_yr,end_yr,ISO3):
		#construct url
		precipitation_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"+ str(type_u) + "/pr/" + str(start_yr) + "/"+ str(end_yr) + "/"+ str(ISO3) +".json"
		climate_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"+ str(type_u) + "/tas/" + str(start_yr) + "/" + str(end_yr) + "/"+ str(ISO3) +".json"

		#print url
		print precipitation_url
		print climate_url

		#request data
		r = requests.get(precipitation_url)
		q = requests.get(climate_url)

		return r.json(),q.json()

def print_info(start_yr,end_yr,country,data):
	for i in data:
		print "From Date (YMD):\t",str(start_yr)+"-"+str(end_yr),"\nCountry:\t",country,"\nData:\t",i

if __name__ == '__main__':

	type_u	= ['mavg','annualavg','manom','annualanom']
	start_yr = [2010]
	end_yr	= [2010]
	ISO3		= ['USA']

	weather = Climate()	
	data = weather.get_weather_data(type_u[2],start_yr[0],end_yr[0],ISO3[0])
	print_info(start_yr[0],end_yr[0],ISO3[0],data)


