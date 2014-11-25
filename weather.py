import urllib2, urllib, json
api_key = '6d41a12cd1c3221c'
baseurl = "http://api.wunderground.com/api/6d41a12cd1c3221c/history_20140101/q/CA/San_Francisco.json"
#yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"

result = urllib2.urlopen(baseurl).read()
data = json.loads(result)

for i in data['history']['observations']:
    #print i
    pass

tideurl = 'http://api.wunderground.com/api/6d41a12cd1c3221c/tide/q/CA/San_Francisco.json'
result = urllib2.urlopen(baseurl).read()
data = json.loads(result)

for i in data['history']['dailysummary']:
    for j in i:
        j['maxheight']
        if True: #j[:4]=='max':
            #print j[']

