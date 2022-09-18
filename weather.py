import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

class weather_data:

	def hello_world():
		print("HELLO!!")
	
	def get_weather_data():

		url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

		# adding the location
		print("What location would you like to look at: ")
		location = input()

		querystring = {"q":location,"days":"3"}

		# my api key
		key = os.getenv("key")
		headers = {
			"X-RapidAPI-Key": key,
			"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
		}

		# this is all the json stuff i have to do
		response = requests.get(url, headers=headers, params=querystring)
		x = response.json()
		weather = json.dumps(x, indent = 1)

		# this is just me getting my moonrise stuff
		moonrise = x['forecast']['forecastday'][0]['astro']['moonrise']

		# returning the moonnrise
		return moonrise

		# print("location: " + " " + x['location']['name'] + " " + x['location']['region'] + " " + x['location']['country'])
		# print("current temp: " + str(x['current']['temp_f']))
		# print("current condition: " + x['current']['condition']['text'])
		# print("current windspeed: " + str(x['current']['wind_mph']))
		# print("sunrise " + str(x['forecast']['forecastday'][0]['astro']['sunrise']))
		# print("sunset " + str(x['forecast']['forecastday'][0]['astro']['sunset']))
		# print("moonrise " + str(x['forecast']['forecastday'][0]['astro']['moonrise']))
		# print("moonset " + str(x['forecast']['forecastday'][0]['astro']['moonset']))
		# print("moonphase " + str(x['forecast']['forecastday'][0]['astro']['moon_phase']))