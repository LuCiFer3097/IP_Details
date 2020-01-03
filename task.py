from ip2geotools.databases.noncommercial import DbIpCity
import socket
import requests, json 
from requests import get
ip=get("https://api.ipify.org").text
response = DbIpCity.get(ip, api_key='free')
print(response.ip_address,response.region,response.country)
city=response.region
import pyowm

owm = pyowm.OWM("aa564802ee440c54cbd386043367a2d1")
observation = owm.weather_at_place('India')
w = observation.get_weather()
temperature = w.get_temperature('celsius')
# tomorrow = pyowm.timeutils.tomorrow()
# wind = w.get_wind()
# print(w)
# print(wind)
print(temperature)
# print(tomorrow)