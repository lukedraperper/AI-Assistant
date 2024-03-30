import speech_recognition as sr
import keyboard
import sys
sys.path.append('../')
from CommandHandler import commandhandler

def AudioRecorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        UserInput = ''
        try:
            UserInput = r.recognize_google(audio)
            UserInput = UserInput.lower()
        except:
            pass
        speaker = '' # getattr(voices.Voices, "LukeDraper")
        speech = UserInput.lower()       
        if speech[:4] in ["what", "who", "where", "when", "why", "how"]:
            speech = f"{speech.capitalize()}?"
        else:
            speech = f"{speech.capitalize()}."

        print(f"{speaker}: {speech}")
        if UserInput != None:
            return UserInput
        
def Listener():
    print("Started.")
    while True:
        if keyboard.is_pressed("f21"):
            print("Detected.")
            UserInput = AudioRecorder()
            commandhandler.Responder(UserInput)