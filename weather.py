import json
import requests
def getWeather(c):
    id = "f331581e1725a93c28647659d1afcc02"

    api = 'http://api.openweathermap.org/data/2.5/weather'
    r = requests.get(url=api, params=dict(q=c, APPID=id))
    return r
id="f331581e1725a93c28647659d1afcc02"

api = 'http://api.openweathermap.org/data/2.5/weather'
cities=["Attock","Bahawalnagar","Bahawalpur","Bhakkar","Chakwal","Chiniot","Faisalabad","Gujranwala","Gujrat","Hafizabad",
        "Jhang","Jhelum","Kasur","Khanewal","Khushab","Lahore","Layyah","Lodhran","Mandi Bahauddin","Multan"]
d={}
print('Fetching results...')
for c in cities:
    r=getWeather(c)
    obj=json.loads(r.text)
    d[obj['name']]=obj
for k in sorted(d,key =lambda name: d[name]['main']['temp']):
    print(k,end='\t')
    print(d[k]['main']['temp']-273)

    
