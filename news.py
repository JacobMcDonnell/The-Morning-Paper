import requests
import json
from time import sleep
from settings import getSettings

news = getSettings("news")
apiKey = news["apikey"]
countryCode = news["country"]

url = f"https://newsapi.org/v2/top-headlines?country={countryCode}&apiKey={apiKey}"


def getHeadlines():
	resp = requests.get(url)
	while resp.status_code != 200:
		resp = requests.get(url)
		sleep(10)

	respData = json.loads(resp.text)

	articles = respData["articles"]

	output = ["Top 5 Headlines in the US:"]

	for i in range(5):
		article = articles[i]
		title = article["title"]
		output.append(title)
		output.append("\n")

	return output
