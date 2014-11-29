#returns empty json - submitted a ticket

import json
import requests

class Climate:
	def __init__(self):
		pass
	def get_weather_data(self,type_u,var_u,start_yr,end_yr,ISO3):
		#create url
		url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"
		url = url + str(type_u) + "/"
		url = url + str(var_u) + "/"
		url = url + str(start_yr) + "/"
		url = url + str(end_yr) + "/"
		url = url + str(ISO3) +".json"
		baseurl = url#'http://api.worldbank.org/countries?format=json'
		print baseurl
		
		#read url data
		"""
		result = urllib2.urlopen(baseurl).read()
		print result
		data = json.loads(result)
		"""
		r = requests.get(baseurl)
		return r.json()

def print_info(start_yr,end_yr,country,data):
	print "From Date (YMD):\t",str(start_yr)+"-"+str(end_yr),"\nCountry:\t",country,"\nData:\t",data

if __name__ == '__main__':

	type_u	= ['mavg','annualavg','manom','annualanom']
	var_u		= ['pr','tas']
	start_yr = [2010]
	end_yr	= [2010]
	ISO3		= ['USA']

	weather = Climate()	
	data = weather.get_weather_data(type_u[2],var_u[0],start_yr[0],end_yr[0],ISO3[0])
	print_info(start_yr[0],end_yr[0],ISO3[0],data)

