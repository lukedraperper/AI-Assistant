from datetime import datetime
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

# import time
# now = datetime.now()
# Minute = int(now.strftime("%M"))
# if Minute > 30:
#     if Minute > 45:
#         Minute = 45
#     else:
#         Minute = 30
# elif Minute < 30:
#     if Minute < 15:
#         Minute = 00
#     else:
#         Minute = 15
# Time1 = str(now.strftime("%H"))+"%3A"+ str(Minute)
# Second = str(int(now.strftime("%H")) + 1)
# Time2 = "&f="+Second+"%3A"+str(Minute)

# url = f"https://www.stagecoachbus.com/timetable-result?a[Category]=postcode&a[Geocode][Grid][value]=WGS84&a[Geocode][Longitude]=-2.1901536445557435&a[Geocode][Latitude]=51.89590838795034&a[FullText]=GL29QQ&a[id]=GL29QQ&b[Category]=locality&b[Geocode][Grid][value]=WGS84&b[Geocode][Longitude]=-2.0759655148644582&b[Geocode][Latitude]=51.900443260367155&b[FullText]=Cheltenham+Town+Centre%2C+Gloucestershire&b[LocalityData][LocalityId]=ZYX3548&b[id]=Cheltenham+Town+Centre%2C+Gloucestershire&c=GL29QQ&d=Cheltenham+Town+Centre%2C+Gloucestershire&e={Time1}{Time2}"
# # print(url)
# # page = requests.get(url)

# # soup = BeautifulSoup(page.content, "html.parser")
# # table = soup.find('table',{'id':'timetable-item-1'})
# # depart = table.find('td',{'class':'print-head'})

# options = Options()
# options.add_argument('--disable-gpu')
# options.add_argument("--log-level=OFF")
# options.add_argument("--disable-web-security")
# options.add_argument("--disable-site-isolation-trials")
# options.add_argument('--headless')
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get(url)
# time.sleep(5)
# Depart = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[7]/div/div[2]/div/div/ul/li/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/div/p").text
# print(Depart)

def thing(command):
    df = pd.read_csv("gym.csv")

    Squats = str(df.loc[df['exercise'] == "squats"].iloc[0,1])
    BenchPress = str(df.loc[df['exercise'] == "benchpress"].iloc[0,1])
    ShoulderPress = str(df.loc[df['exercise'] == "shoulderpress"].iloc[0,1])
    Deadlifts = str(df.loc[df['exercise'] == "deadlifts"].iloc[0,1])
    BentOverRow = str(df.loc[df['exercise'] == "bentoverrow"].iloc[0,1])
    Day = str(df.loc[df['exercise'] == "day"].iloc[0,1])
    print(Day)

    Day1 = f"Squats {Squats}, Bench Press {BenchPress}, Shoulder Press {ShoulderPress}"
    Day2 = f"Squats {Squats}, Deadlifts {Deadlifts}, Bent Over Row {BentOverRow}"

    if command == "Finished":
        if Day == "1.0":
            Squats = 1
            # df.loc["benchpress","weight"] += 2.5
            # df.loc["benchpress","weight"] += 2.5
            # df.loc["shoulderpress","weight"] += 2.5
            # df.loc["day","weight"] += 1
            df.to_csv('gym.csv')
            print("Done.")
        else:
            # df.loc["squats","weight"] += 2.5
            # df.loc["deadlifts","weight"] += 2.5
            # df.loc["bentoverrow","weight"] += 2.5
            # df.loc["day","weight"] -= 1
            # df.to_csv('gym.csv')
            # print("Done.")
            pass
    elif command == "Weight":
        print(f"Squats {Squats}, Bench Press {BenchPress}, Shoulder Press {ShoulderPress}, Deadlifts {Deadlifts}, Bent Over Row {BentOverRow}")
thing("Finished")