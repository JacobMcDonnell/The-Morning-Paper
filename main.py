from cal import getEventsFromCal
from natDay import getNationalDay
from news import getHeadlines
from quote import getQuote
from weather import getHourlyForecast, getDetailedForecast
import datetime
from settings import modules, general, lineWidth
from time import sleep
from Adafruit_Thermal import *
from textwrap import fill
from ipqr import getQrCode

name = general["name"]
today = datetime.date.today().strftime("%A %m-%d-%Y")
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

output = ["The Morning Paper:", f"Good Morning {name}, Today is {today}"]

mods = {
    "quote": getQuote(),
    "national day": getNationalDay(),
    "Detailed": getDetailedForecast(),
    "Hourly": getHourlyForecast(),
    "calendar": getEventsFromCal(),
    "news": getHeadlines()
}


def main():
    for module in modules:
        if modules[module]:
            for line in mods[module]:
                line = line.replace("\n", "")
                printer.println(fill(line, lineWidth))
            printer.feed(1)


def printSettingsPage():
    printer.println("Settings")
    try:
        getQrCode()
        printer.println(fill("Scan the QR Code below to access settings", lineWidth))
        printer.printImage("ipqr.png")
    except:
        printer.println("No Network Connection")


printer.wake()
printer.setSize('M')
sleep(10)

for line in output:
    printer.println(fill(line, lineWidth))
try:
    main()
except:
    sleep(30)
    main()

printSettingsPage()

printer.feed(6)
printer.sleep()
