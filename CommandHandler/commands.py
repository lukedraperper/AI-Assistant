import bs4
from urllib.request import urlopen as uReq
from urllib.request import Request
from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition as sr
import os, glob, sys
import time
from pynput.keyboard import Key, Controller
import webbrowser
import random
import contextlib
import string
import yt_dlp
with contextlib.redirect_stdout(None):
    import pygame
from datetime import datetime
from multiprocessing import Process
import threading
import main
import webbrowser
import requests
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import re, requests, subprocess, urllib.parse, urllib.request
from yt_dlp import YoutubeDL
import pytz
import pandas as pd
import telegram_send

def Exercise(command):
    try:

        df = pd.read_csv("gym.csv")

        Squats = str(df.loc[df['exercise'] == "squats"].iloc[0,1])
        BenchPress = str(df.loc[df['exercise'] == "benchpress"].iloc[0,1])
        ShoulderPress = str(df.loc[df['exercise'] == "shoulderpress"].iloc[0,1])
        Deadlifts = str(df.loc[df['exercise'] == "deadlifts"].iloc[0,1])
        BentOverRow = str(df.loc[df['exercise'] == "bentoverrow"].iloc[0,1])
        Day = str(df.loc[df['exercise'] == "day"].iloc[0,1])

        Day1 = f"Squats {Squats}, Bench Press {BenchPress}, Shoulder Press {ShoulderPress}"
        Day2 = f"Squats {Squats}, Deadlifts {Deadlifts}, Bent Over Row {BentOverRow}"

        if command == "Finished":
            if Day == "1":
                df.loc["squats","weight"] = 1
                # df.loc["benchpress","weight"] += 2.5
                # df.loc["shoulderpress","weight"] += 2.5
                # df.loc["day","weight"] += 1
                df.to_csv('gym.csv')
                print("Done.")
            else:
                df.loc["squats","weight"] += 2.5
                df.loc["deadlifts","weight"] += 2.5
                df.loc["bentoverrow","weight"] += 2.5
                df.loc["day","weight"] -= 1
                df.to_csv('gym.csv')
                print("Done.")
        elif command == "Weight":
            CS(f"Squats {Squats}, Bench Press {BenchPress}, Shoulder Press {ShoulderPress}, Deadlifts {Deadlifts}, Bent Over Row {BentOverRow}")



    except Exception as e:
        print(e)
def Time(voice_data):
    if voice_data.endswith("time") or voice_data.endswith("is it"):
        now = datetime.now()
        time = now.strftime("%I:%M %p")
    else:
        zone = voice_data.split("in", 1)[1].strip().lower()
        zones = []
        for z in pytz.all_timezones:
            zones.append(z.split("/",1)[1].lower())
        for z in zones:
            if zone in z:
                print("yes")
                time = datetime.now(pytz.timezone(z))
                time = time.strftime("%I:%M %p")
        else:
            pass
    time = str(time)
    return time
def CS(sayMessage):
    # telegram_send.send(messages=[sayMessage])
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    print(f"JARVIS: {sayMessage}")
    engine.say(sayMessage)
    engine.runAndWait()
def GetTable():
    my_url = "https://www.premierleague.com/tables"
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    top = page_soup.find("span", {"class":"long"}).text
    tottenham = page_soup.find("tr", {"data-filtered-table-row-name":"Tottenham Hotspur"})
    tottenhamplace = tottenham.span.text
    if top == "Tottenham Hotspur":
        sayMessage = "Currently, " + top + " are at the top of the Premier League Table."
    else:
        sayMessage = "Currently, " + top + " are at the top of the Premier League Table whilst Tottenham are at Position", tottenhamplace
    return sayMessage
def NextFixture():
    my_url = "https://www.tottenhamhotspur.com/fixtures/men/"
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    uClient = uReq(req)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    dayname = page_soup.find("div",{"class":"FixtureHero__kickoff"})

    return dayname
class OpenWebsite():
    youtube = "https://www.youtube.com/"
    instagram = "https://www.instagram.com/"
    reddit = "https://www.reddit.com/"
    twitch = "https://www.twitch.tv/"
    guitar = "https://www.ultimate-guitar.com/explore"
def Joke():
    global CS
    url = requests.get("https://v2.jokeapi.dev/joke/any").json()
    response = ""
    if url["type"] == "twopart":
        response = url["setup"]
        time.sleep(1)
        response = url["delivery"]
    else:
        response = url["joke"]
    
    return response
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
def Alarm(num1, num2, amorpm, type):
    global StartUp
    if amorpm == "p.m.":
        amorpm = "PM."
    else:
        amorpm = "AM."
    CS(f"Alarm set for {num1}:{num2} {amorpm}")
    num1 = int(num1)
    num2 = int(num2)
    if amorpm == "PM.":
        num1 += 12
    elif num1 == 12 and amorpm == "AM.":
        num1 -= 12
    while True:
        if num1 == datetime.datetime.now().hour and num2 == datetime.datetime.now().minute:
            break
    if type == "bed":
        StartUp()
    elif type == "Normal":
        main.Play("alarm")
def SimonSays(message):
    message = message.replace("simon says","").strip()
    message = str(message)
    return message
def ChangeAudioOutput(device, pos):
    pygame.mixer.quit()
    pygame.mixer.pre_init(devicename="HDA Intel PCH, 92HD87B2/4 Analog")
def ShutDown():
    os.system("shutdown /s /y")