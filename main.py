from cal import getEventsFromCal
from natDay import getNationalDay
from news import getHeadlines
from quote import getQuote
from weather import getHourlyForecast, getDetailedForecast
import datetime
from settings import modules, general, lineWidth
from time import sleep
from Adafruit_Thermal import *
import textwrap

name = general["name"]
today = datetime.date.today().strftime("%A %m-%d-%Y")
printer = Adafruit_Thermal("/dev/ttyS0", 19200, timeout=5)

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
                printer.println(textwrap.fill(line, lineWidth))
            printer.feed(1)


printer.wake()
printer.setSize('M')
sleep(10)

for line in output:
    printer.println(textwrap.fill(line, lineWidth))
try:
    main()
except:
    sleep(30)
    main()

printer.feed(6)
printer.sleep()
