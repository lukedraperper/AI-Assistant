from datetime import datetime
import pytz
import time

def Time(query):
    now = time.localtime()
    hour = now[3]
    minute = now[4]
    if query.endswith("time") or query.endswith("is it"):
        now = datetime.now()
        time = now.strftime("%I:%M %p")
    else:
        zone = query.split("in", 1)[1].strip().lower()
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
print(hour, minute)