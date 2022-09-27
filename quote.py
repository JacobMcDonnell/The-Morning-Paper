import requests
import json
import time

quoteUrl = "https://quotable.io/random"


def getQuote():
    resp = requests.get(quoteUrl)

    while resp.status_code != 200:
        resp = requests.get(quoteUrl)
        time.sleep(10)

    quoteData = json.loads(resp.text)
    content = quoteData["content"]
    author = quoteData["author"]

    return [f"Here is today's quote:\n\"{content}\" - {author}\n"]
