#returns empty json - submitted a ticket

import json
import requests
import pandas as pd
#import sys
import numpy as np

class Climate:
	def __init__(self):
		countries = "http://api.worldbank.org/countries?format=json"
		self.r = requests.get(countries)
		
	def get_countries_data(self,country_csv,max_countries=None):
		country_data = []
		countries = pd.read_csv(country_csv,sep=';')
		codes = countries['code']
		if (max_countries is None):
			max_countries = len(codes)
		for i,c in zip(np.arange(len(countries)),countries['code']):
			if i == max_countries:
				break
			data = self._get_country_data(c)
			if len(data)!=0:
				country_data.append(data)
		return pd.DataFrame(country_data)

	#handles errors
	def _get_country_data(self,ISO2):
		try:
			c = "http://api.worldbank.org/countries/"+str(ISO2)+"?format=json"
			r = requests.get(c)
			i = r.json()[1][0]#for countries remove [0] and iterate through i
			return [i['id'],i['name'],i['longitude'],i['latitude']]
		except:
			return []

	def get_closest_country(lat,lon):
		#take a lat and long and return the closest country to that location

	def get_weather_data(self,type_u,start_yr,end_yr,ISO3):
		#construct url
		precipitation_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"+ str(type_u) + "/pr/" + str(start_yr) + "/"+ str(end_yr) + "/"+ str(ISO3) +".json"
		climate_url = "http://climatedataapi.worldbank.org/climateweb/rest/v1/country/"+ str(type_u) + "/tas/" + str(start_yr) + "/" + str(end_yr) + "/"+ str(ISO3) +".json"

		#request data
		r = requests.get(precipitation_url)
		q = requests.get(climate_url)

		return r.json(),q.json()

def print_info(start_yr,end_yr,country,data):
	for i in data:
		print "From Date (YMD):\t",str(start_yr)+"-"+str(end_yr),"\nCountry:\t",country,"\nData:\t",i
		print

if __name__ == '__main__':

	#Return lat and long of various country codes 
	country_code_csv = 'country_codes.csv'
	weather = Climate()	
	max_countries_to_lookup = 20
	print weather.get_countries_data(country_code_csv,max_countries_to_lookup).values

	print
	print 

	#ask for weather from a specific country code
	type_u	= ['mavg','annualavg','manom','annualanom']
	start_yr = [2010]
	end_yr	= [2010]
	ISO3		= ['USA']
	data = weather.get_weather_data(type_u[2],start_yr[0],end_yr[0],ISO3[0])
	print_info(start_yr[0],end_yr[0],ISO3[0],data)


