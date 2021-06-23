#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from datetime import datetime

api_key = '09a4d8c2fd07be5903f984a0d2b429dc'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("=============================================================")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("=================================================================")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')

print(temp_city,weather_desc)
f = open("demofile3.txt", "w")
f.write(f'{temp_city} \n  {weather_desc} \n {hmdt} \n {wind_spd} ')
f.close()
print("text file is also created, please see the the folder")

print("weather conditions are displayed")

