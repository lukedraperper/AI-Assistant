from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
import time
import requests
import requests
 
# def Sunrise():
#     global sunrise
#     time = str(GetWeather("sunrise"))
#     if now[3] < int(time[0:1].strip()) and now[4] < int(time[3:4]):
#         sunrise = f"time is at {time}, "
#     elif now[3] == int(time[0:1].strip()) and now[4] == int(time[3:4]):
#         sunrise = f"time is at {time}, "
#     else:
#         sunrise = ""
#     # tomorrow = page.find("li", {"id":"tabDay1"})
#     # tomorrow_high = tomorrow.find("span", {"class":"tab-temp-high"}).text
#     # tomorrow_low = tomorrow.find("span", {"class":"tab-temp-low"}).text
#     # tomorrow_high = tomorrow_high.replace("°", " Degrees")
#     # tomorrow_low = tomorrow_low.replace("°", " Degrees")    
#     weather = f'The weather in Cheltenham is {GetWeather("temperature")} degrees. {GetWeather("forecast")}'
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

    # Temperature
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
    forecast = page.find("div",{"class":"ssrcss-7uxr49-RichTextContainer e5tfeyi1"})
    text = forecast.findAll("p",{"class":"ssrcss-1q0x1qg-Paragraph e1jhz7w10"})[1]
    text = text.text
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
        pass
    
    if type == "sunrise":
        return sunrise
    if type == "forecast":
        return str(forecast)
    else:
        return "That is not a type."
    
print(GetWeather("forecast"))