import json

settingsJSON = open('settings.json')

settings = json.load(settingsJSON)

calendars = settings["calendars"]
weather = settings["weather"]
news = settings["news"]
modules = settings["modules"]
general = settings["general"]

settingsJSON.close()


