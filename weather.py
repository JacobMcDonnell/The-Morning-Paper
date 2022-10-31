import requests
import json
from time import sleep
from datetime import datetime
from settings import getSettings

weather = getSettings("weather")
gridX = weather["gridX"]
gridY = weather["gridY"]
wfo = weather["WFO"]
units = weather["Units"]  # either si or us
hours = weather["Hours"]


def getHourlyForecast():
	output = []

	hourlyForecastUrl = f"https://api.weather.gov/gridpoints/{wfo}/{gridX},{gridY}/forecast/hourly?units={units}"

	hourResp = requests.get(hourlyForecastUrl)

	while hourResp.status_code != 200:
		hourResp = requests.get(hourlyForecastUrl)
		sleep(10)

	hourData = json.loads(hourResp.text)
	hourPeriods = hourData["properties"]["periods"]

	output.append(f"{hours} Hour Forecast")
	for i in range(hours):
		forecast = hourPeriods[i]
		sTime = datetime.strptime(forecast["startTime"], "%Y-%m-%dT%H:%M:%S%z")
		formatTime = sTime.strftime("%m-%d %H:%M")
		temp = str(forecast["temperature"]) + "°" + forecast["temperatureUnit"] + " " + forecast["shortForecast"]
		hourlyForecast = f"{formatTime}: {temp}"
		output.append(hourlyForecast)

	return output


def getDetailedForecast():
	output = []

	dayForecastUrl = f"https://api.weather.gov/gridpoints/{wfo}/{gridX},{gridY}/forecast?units={units}"
	dayResp = requests.get(dayForecastUrl)

	while dayResp.status_code != 200:
		dayResp = requests.get(dayForecastUrl)
		sleep(10)

	dayData = json.loads(dayResp.text)
	dayPeriods = dayData["properties"]["periods"]

	todayFor = dayPeriods[0]
	tonightFor = dayPeriods[1]

	output.append("Today's Forecast: " + todayFor["detailedForecast"])
	output.append("\nTonight's Forecast: " + tonightFor["detailedForecast"] + "\n")

	return output
