#weather - returns the pressure and the temperature at a location at a specific date
#currently set up for individual queries, but can expand for bulk entries

import urllib2, urllib, json

class Climate:
	def __init__(self):
		#init key 
		self.api_key = '6d41a12cd1c3221c'

	def _thresh(self,var,threshold):
		if int(var) < threshold:
			return '0'+str(var)
		return str(var)
	def get_weather_data(self,year,month,day,lat,lon):
		#create url
		url = "http://api.wunderground.com/api/"+self.api_key
		history = "/history_"+self._thresh(year,1000)+self._thresh(month,10)+self._thresh(day,10)+"/q/CA/San_Francisco.json"
		baseurl = url + history
		#yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
		
		#read url data
		result = urllib2.urlopen(baseurl).read()
		data = json.loads(result)

		for i in data['history']['dailysummary']:
			temp = i['meantempi']
			press = i['meanpressurei']
		return temp,press

if __name__ == '__main__':

	year  = 2014
	month = 2
	day   = 1
	lat	= 23#does not currently work-will be a little more challenging than I initially thought because the url does not do any calculations to determine the closest city
	lon	= 23	

	weather = Climate()	
	temp,press = weather.get_weather_data(year,month,day,lat,lon)
	print "Date (YMD):\t",str(year)+"-"+str(month)+"-"+str(day),"\nAvg temp:\t",temp,"\nAvg pressure:\t",press

