import requests
import json
import time
import random

url = "https://national-api-day.herokuapp.com/api/today"


def getNationalDay():
    resp = requests.get(url)

    while resp.status_code != 200:
        resp = requests.get(url)
        time.sleep(10)

    data = json.loads(resp.text)
    holidays = data["holidays"]
    index = random.randint(0, len(holidays) - 1)

    return [f"Today's National Day:\n{holidays[index]}\n"]
