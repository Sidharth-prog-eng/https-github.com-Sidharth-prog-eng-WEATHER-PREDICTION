import datetime as dt
import requests


base_url = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key','r').read()

CITY="Kerala"

def kelvin_to_celcius_faranheit(kelvin):
    celsius=kelvin-273.15
    faranheit=celsius*(9/5)+32
    return celsius,faranheit


url=base_url+ "appid=" + API_KEY + "&q=" + CITY
response=requests.get(url).json()  

temp_kelvin=response['main']['temp']
temp_celsius,temp_faraheit=kelvin_to_celcius_faranheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius,feels_like_faranheit = kelvin_to_celcius_faranheit(temp_kelvin)
wind_speed=response['wind']['speed']
humidity=response['main']["humidity"]
description = response["weather"][0]["description"]
sunrisetime=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response["timezone"])
sunsettime=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])


print(f"temperature in {CITY}:{temp_celsius:2f}c or faranheit{temp_faraheit:2f}f")
print(f"temperature in {CITY}:feels like:{feels_like_celsius:2f}c or feels like:{feels_like_faranheit:2f}f")
print(f"Humidity in {CITY}:{humidity}%")
print(f"Wind speed in {CITY}:{wind_speed}m/s")
print(f"General weather in  {CITY}:{description}")
print(f"sunrise time in {CITY}:{sunrisetime} local time")
print(f"sunsets in {CITY}:{sunsettime} local time")

