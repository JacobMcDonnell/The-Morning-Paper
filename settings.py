import json
from main import printer
from ipqr import getQrCode
from PIL import Image
from textwrap import fill

settingsJSON = open('settings.json')

settings = json.load(settingsJSON)

calendars = settings["calendars"]
weather = settings["weather"]
news = settings["news"]
modules = settings["modules"]
general = settings["general"]
lineWidth = settings["general"]["Line Width"]

settingsJSON.close()


def printSettingsPage():
    printer.println("Settings")
    try:
        getQrCode()
        qr = Image.open(r"ipqr.png")
        printer.println(fill("Scan the QR Code below to access settings", lineWidth))
        printer.printImage(qr)
    except:
        printer.println("No Network Connection")
