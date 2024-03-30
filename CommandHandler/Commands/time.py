from datetime import datetime
import pytz

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