#!/usr/bin/python

import requests, json, sys

ad = 'http://api.openweathermap.org/data/2.5/forecast?q=Bratislava&APPID=2290ca0515d1d4165a22ff1baadbdfcf'
api_key = '2cad41f6918861f57a8ab4a4956cb141'

if len(sys.argv) < 2:
    print('Usage: weather_api.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
api_call = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' % (location, api_key)

response = requests.get(api_call)
# check for exceptions
response.raise_for_status()
weather_data = json.loads(response.text)
w = weather_data['list']

print(w[0]['weather'])
