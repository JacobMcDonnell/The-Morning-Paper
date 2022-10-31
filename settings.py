import json
from logging import exception

def getSettings(settingSection):
    try:
        settingsJSON = open("settings.json", "r")
    except FileNotFoundError:
       exception("settings.json not found make sure it exists in this folder")

    settings = json.load(settingsJSON)
    settingsJSON.close()

    return settings[settingSection]

