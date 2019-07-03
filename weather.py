import requests
id="f331581e1725a93c28647659d1afcc02"

api = 'http://api.openweathermap.org/data/2.5/weather'
r=requests.get(url=api,params=dict(q='Lahore',APPID=id))
print(r.text)#The temperature is in Kelvins
