import icalendar
import recurring_ical_events
import urllib.request
import datetime
from settings import getSettings

calendars = getSettings("calendars")
today = datetime.date.today()
output = []

'''
    For some reason Icloud calendars seem to be reversed,
    so the must be reversed to put events in the proper order.
'''


def isIcloud(url):
    index = url.find("icloud")
    if index > -1:
        return True
    return False


def getEvents(url, cName):
    ical_string = urllib.request.urlopen(url).read()
    calendar = icalendar.Calendar.from_ical(ical_string)
    events = recurring_ical_events.of(calendar).at(today)
    if len(events) != 0:
        if isIcloud(url):
            events.reverse()
        output.append(f"\nToday's events from {cName} calendar:")
        for event in events:
            name = event["SUMMARY"]
            try:
                start = event["DTSTART"].dt.strftime("%H:%M")
                end = event["DTEND"].dt.strftime("%H:%M")
                output.append(f"{name} from {start} to {end}")
            except:
                output.append(f"{name} All Day")


def getEventsFromCal():
    for calendar in calendars:
        url = calendars[calendar]
        getEvents(url, calendar)
    output[-1] = output[-1] + "\n"
    return output
