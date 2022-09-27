import requests
import json
from time import sleep
from datetime import datetime
from settings import weather

gridX = weather["gridX"]
gridY = weather["gridY"]
wfo = weather["WFO"]
units = weather["Units"]  # either si or us
hourly = weather["Hourly"]
detailed = weather["Detailed"]
hours = weather["Hours"]


def getForecast():
    output = []

    dayForecastUrl = f"https://api.weather.gov/gridpoints/{wfo}/{gridX},{gridY}/forecast?units={units}"
    hourlyForecastUrl = f"https://api.weather.gov/gridpoints/{wfo}/{gridX},{gridY}/forecast/hourly?units={units}"

    dayResp = requests.get(dayForecastUrl)
    hourResp = requests.get(hourlyForecastUrl)

    while (dayResp.status_code != 200) and (hourResp.status_code != 200):
        dayResp = requests.get(dayForecastUrl)
        hourResp = requests.get(hourlyForecastUrl)
        sleep(10)

    dayData = json.loads(dayResp.text)
    hourData = json.loads(hourResp.text)
    dayPeriods = dayData["properties"]["periods"]
    hourPeriods = hourData["properties"]["periods"]

    todayFor = dayPeriods[0]
    tonightFor = dayPeriods[1]

    if detailed:
        output.append("Today's Forecast: " + todayFor["detailedForecast"])
        output.append("\nTonight's Forecast: " + tonightFor["detailedForecast"] + "\n")

    if hourly:
        output.append(f"{hours} Hour Forecast")
        for i in range(hours):
            forecast = hourPeriods[i]
            sTime = datetime.strptime(forecast["startTime"], "%Y-%m-%dT%H:%M:%S%z")
            formatTime = sTime.strftime("%m-%d %H:%M")
            temp = str(forecast["temperature"]) + "°" + forecast["temperatureUnit"] + " " + forecast["shortForecast"]
            hourlyForecast = f"{formatTime}: {temp}"
            output.append(hourlyForecast)
    return output
