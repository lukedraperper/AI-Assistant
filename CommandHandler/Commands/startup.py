import time
from weather import GetWeather
import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

def StartUp():
    # Time
    now = time.localtime()
    if now[4] > 0 and now[4] < 30:
        seconddigit = str(f"{now[4]} past")
        firstdigit = now[3]-12
    elif now[4] > 30:
        seconddigit = str(f"{60 - now[4]} to")
        firstdigit = now[3]-11
    elif now[4] == 30:
        seconddigit = "Half past"
        firstdigit = now[3]-12
    if now[3] < 12:
        if now[4] == 00:
            greeting = f"Good morning, it's {now[3]} AM, "
        else:
            greeting = f"Good morning, it's {seconddigit} {now[3]} AM, "
    elif now[3] > 11 and now[3] < 17:
        if now[4] == 00:
            greeting = f"Good afternoon, it's {now[3]-12} PM, "
        else:
            greeting = f"Good afternoon, it's {seconddigit} {firstdigit} PM, "
    elif now[3] > 16 and now[3] < 24:
        if now[4] == 00:
            greeting = f"Good evening, it's {now[3]-12} PM, "
        else:
            greeting = f"Good evening, it's {seconddigit} {firstdigit} PM, "
    sunrise = str(GetWeather("sunrise"))
    if now[3] < int(sunrise[0:1].strip()) and now[4] < int(sunrise[3:4]):
        sunrisemessage = f"Sunrise is at {sunrise}, "
    elif now[3] == int(sunrise[0:1].strip()) and now[4] == int(sunrise[3:4]):
        sunrisemessage = f"Sunrise is at {sunrise}, "
    else:
        sunrisemessage = ""

    # tomorrow = page.find("li", {"id":"tabDay1"})
    # tomorrow_high = tomorrow.find("span", {"class":"tab-temp-high"}).text
    # tomorrow_low = tomorrow.find("span", {"class":"tab-temp-low"}).text
    # tomorrow_high = tomorrow_high.replace("°", " Degrees")
    # tomorrow_low = tomorrow_low.replace("°", " Degrees")    
    weathermessage = f'The weather in Cheltenham is {GetWeather("temperature")} degrees. {GetWeather("forecast")}'
    sayMessage = f"{greeting}{sunrisemessage}{weathermessage}"
    pygame.mixer.init()
    pygame.mixer.music.load(os.path.dirname(os.path.realpath(__file__)) + "\Sounds\\startsound.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.load(os.path.dirname(os.path.realpath(__file__))+ "\Sounds\\endsound.mp3")
    pygame.mixer.music.play()
    pygame.mixer.quit()