# The Morning Paper
The Morning Paper is a project that prints out different information to a 
receipt printer in the morning. The project will include template modules for 
today's calendar events, the weather, a quote, top news headlines, and the 
national day.

## Modules
The modules provided are written in python and will use the [adafruit thermal 
printer library](https://github.com/adafruit/Python-Thermal-Printer) to 
interface with the 
[adafruit thermal printer used](https://www.adafruit.com/product/600).

## TODO
- Add comments to all functions for better documentation
- Timer for the main function
- Stock Tracker
- Better error handling
- Test print page with ip address
- Web interface for settings
  ~~- Settings print out with qr code to ip address~~
- Fix the Phantom j

## Parts
- [Adafruit Thermal Printer](https://www.adafruit.com/product/600)
- Microcontroller (I used a raspberry pi 4 but a zero w will work as well)

## APIs used
- [Quotable](https://quotable.io)
- [National Weather Service](https://www.weather.gov/documentation/services-web-api)
- [News API](https://newsapi.org/)
- [National Day API](https://national-api-day.herokuapp.com)

## Setup
Rename Example.settings.json to settings.json and fill in the needed 
information.