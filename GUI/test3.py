import pandas as pd
import telegram_send
import pyttsx3
def CS(sayMessage):
    telegram_send.send(messages=[sayMessage])
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 130)
    print(f"JARVIS: {sayMessage}")
    engine.say(sayMessage)
    engine.runAndWait()

def Gym():
    
    df = pd.read_csv("gym.csv")

    Squats = str(df.loc[df['exercise'] == "squats"].iloc[0,1])
    BenchPress = str(df.loc[df['exercise'] == "benchpress"].iloc[0,1])
    ShoulderPress = str(df.loc[df['exercise'] == "shoulderpress"].iloc[0,1])
    Deadlifts = str(df.loc[df['exercise'] == "deadlifts"].iloc[0,1])
    BentOverRow = str(df.loc[df['exercise'] == "bentoverrow"].iloc[0,1])

    Day1 = f"Squats {Squats}, Bench Press {BenchPress}, Shoulder Press {ShoulderPress}"
    Day2 = f"Squats {Squats}, Deadlifts {Deadlifts}, Bent Over Row {BentOverRow}"#

    CS(Day1)
Gym()