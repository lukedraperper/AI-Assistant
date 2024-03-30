from __future__ import unicode_literals
import sys
from pynput.keyboard import Key, Controller
import webbrowser
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import threading
import webbrowser
import commands
import time
pygame.mixer.init()


def CS(sayMessage):
    # telegram_send.send(messages=[sayMessage])
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    print(f"JARVIS: {sayMessage}")
    engine.say(sayMessage)
    engine.runAndWait()
    
def Responder(UserInput):
    global AudioRecorder
    try:
        if 'alarm' in UserInput:
            if 'bed' in UserInput:
                type = "bed"
            else:
                type = "Normal"
            try:
                nums = ""
                if 'for' in UserInput:
                    times = UserInput.split("for ",1)[1]
                else:
                    commands.CS("For what time?")
                    times = AudioRecorder()
                if times.count("a.m.") >= 1:
                    nums = times.split(" a.m.",1)[0]
                    amorpm = "a.m."
                elif times.count("p.m") >= 1:
                    nums = times.split( "p.m.",1)[0]
                    amorpm = "p.m."
                else:
                    while True:
                        commands.CS("a.m. or p.m.")
                        amorpmtest = AudioRecorder()
                        amorpmtest = amorpmtest.lower()
                        print(amorpmtest)
                        if amorpmtest.count("a.m.") >= 1:
                            amorpm = "a.m."
                            nums = times.split(" a.m.",1)[0]
                            break
                        elif amorpmtest.count("p.m.") >= 1:
                            amorpm = "p.m."
                            nums = times.split(" p.m.",1)[0]
                            break
                        else:
                            print("Failed to retrieve AM or PM.")
                            pass
                nums = nums.replace(":","").strip()
                if len(nums) == 1:
                    num1 = nums
                    num2 = 00
                    alarm = threading.Thread(target=commands.Alarm,args=[num1,num2,amorpm,type])
                    alarm.start()
                if len(nums) == 3:
                    num1 = str(nums[0])
                    num2 = str(nums[1:3])
                    alarm = threading.Thread(target=commands.Alarm,args=[num1,num2,amorpm,type])
                    alarm.start()
                elif len(nums) == 4: 
                    num1 = str(nums[0:2])
                    num2 = str(nums[2:4])
                    alarm = threading.Thread(target=commands.Alarm,args=[num1,num2,amorpm,type])
                    alarm.start()
                else:
                    print("Failed to start alarm.")
            except:
                pass
        # Weather
        elif 'weather' in UserInput:
            commands.CS(commands.GetWeather("forecast"))
        elif 'temperature' in UserInput and 'tomorrow' not in UserInput and 'high' not in UserInput and 'low' not in UserInput:
            commands.CS(commands.GetWeather("temperature") + " degrees.")
        elif 'temperature' in UserInput and 'mininmum' in UserInput and 'tomorrow' not in UserInput and 'maxmimum' not in UserInput:
            commands.CS(commands.GetWeather('mintemperature') + " degrees.")
        elif 'temperature' in UserInput and 'maximum' in UserInput and 'tomorrow' not in UserInput and 'minimum' not in UserInput:
            commands.CS(commands.GetWeather("maxtemperature") + " degrees.")
        elif 'temperature' in UserInput and 'maximum' in UserInput and 'minimum' in UserInput and 'tomorrow' not in UserInput:
            commands.CS(commands.GetWeather("maxmintemperature") + " degrees.")
        elif 'joke' in UserInput:
            commands.Joke(UserInput)
        elif 'open' in UserInput:
            try:
                website = getattr(commands.OpenWebsite, str(UserInput.split("open ",1)[1]))
                webbrowser.get().open(website)
            except:
                website = "https://www." + str(UserInput.split("open ",1)[1]) + ".com/"
                webbrowser.get().open(website)
        elif 'add' in UserInput and 'note' in UserInput:
            with open("ideas.txt", "a") as text_file:
                text = UserInput.split("note",1)[1] + "\n"
                text_file.write(text)
        elif 'search' in UserInput:
            url = 'https://google.co.uk/search?q=' + UserInput.split("search for",1)[1]
            webbrowser.get().open(url)
        elif 'what is your name' in UserInput:
            return "My name is JARVIS"
        elif 'time' in UserInput:
            response = commands.Time(UserInput)
            return response
        elif "simon" in UserInput and "says" in UserInput:
            commands.SimonSays(UserInput)
        elif "run" in UserInput:
            wantedfunction = UserInput.split("run",1)[1].strip()
            wantedfunction = wantedfunction.lower()
            functions = dir(commands)
            for i in range(0,len(functions)):
                function = str(functions[i]).lower()
                if wantedfunction in function:
                    response = "Okay."
                    getattr(commands, functions[i])()
                    break
                else:
                    pass
            else:
                response = "That is not a function."
            return response

        # Media.
        elif "play" in UserInput:
            if 'my playlist' in UserInput:
                commands.Playlist(UserInput)
            else:
                commands.PlayMusic(UserInput)
            return "As you wish sir"
        
        elif 'next' in UserInput or 'next song' in UserInput:
            pygame.mixer.music.stop()
        # if 'previous' in UserInput or 'previous song' in UserInput:
        #     PreviousSong()
        # elif 'gym' in UserInput:
        #     if "finished" in UserInput:
        #         commands.Exercise("Finished")
        #     elif "weight" in UserInput:
        #         commands.Exercise("Weight")
        #     else:
        #         pass
        elif "pause" in UserInput:
            try:
                pygame.mixer.music.pause()
            except:
                keyboard = Controller()
                keyboard.press(Key.media_play_pause)
        elif "unpause" in UserInput or 'resume' in UserInput:
            try:
                pygame.mixer.music.unpause()
            except:
                keyboard = Controller()
                keyboard.press(Key.media_play_pause)
        elif "stop" in UserInput:
            pygame.mixer.quit()
        elif 'mute' in UserInput:
            keyboard = Controller()
            keyboard.press(Key.media_volume_mute)
        elif 'unmute' in UserInput:
            keyboard = Controller()
            keyboard.press(Key.media_volume_up)
            time.sleep(1)
            keyboard.press(Key.media_volume_down)
        elif 'volume' in UserInput:
            if 'to' in UserInput:
                volume = UserInput.split("to",1)[1].replace("%","").strip()
                commands.Volume(volume)
            else:
                volume = UserInput.split("volume",1)[1].replace("%","").strip()
                commands.Volume(volume)
            
        elif 'power down' in UserInput:
            sys.exit()
        elif 'shut down computer' in UserInput:
            commands.ShutDown()
    except Exception as Error:
        print(Error)
    except SystemExit:
        sys.exit()