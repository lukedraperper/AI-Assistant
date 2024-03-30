from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import time
import contextlib
import webbrowser
import requests
import re, requests, subprocess, urllib.parse, urllib.request
 

def GetWeather(type):
    now = time.localtime()
    # Requests.
    url = requests.get("http://api.openweathermap.org/data/2.5/weather?q=cheltenham&appid=c06dbe3e3325ac75be698f7677847928").json()
    my_url = "https://www.bbc.co.uk/weather/2653261"
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    page = soup(page_html, "html.parser")

    # Today

    # Temeperature
    currentTemp = round(((url["main"]["temp"])- 273.15))
    currentTemp = str(currentTemp).replace("-", "Minus ")
    maxTemp = round(((url["main"]["temp_max"])- 273.15))
    maxTemp = str(maxTemp).replace("-", "Minus ")
    minTemp = round(((url["main"]["temp_min"])- 273.15))
    minTemp = str(minTemp).replace("-", "Minus ")

    # Sunrise
    sunrise = page.find("span", {"class":"wr-c-astro-data__time"}).text
    sunrise = sunrise.replace("0","",1).replace(":"," ")

    # Forecast
    forecast = page.find("p",{"class":"wr-c-text-forecast__summary-text gel-long-primer gs-u-mt-"}).text

    # Tomorrow


    # Return
    if type == "temperature":
        return str(currentTemp)
    if type == "maxtemperature":
        return maxTemp
    if type == "mintemperature":
        return minTemp
    if type == "maxmintemperature":
        return maxTemp, minTemp
    if type == "tomorrowtemperature":
        return tomorrowtemperature
    
    if type == "sunrise":
        return sunrise
    if type == "forecast":
        return str(forecast)
    else:
        return "That is not a type."