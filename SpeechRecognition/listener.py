import speech_recognition as sr
import keyboard
import sys
sys.path.append('../')
from CommandHandler import commandhandler
from recognition import AudioRecorder
import telegram
import pvporcupine
import pyaudio
import struct

api_id = 23064059
api_hash = 'ef3f3e3245284948f45368457d7e38cb'

def KeyboardListener():
    hotkey = "f21"
    print(f"KeyboardListener started. Waiting for {hotkey}.")
    while True:
        if keyboard.is_pressed(hotkey):
            print("Detected.")
            UserInput = AudioRecorder()
            commandhandler.Responder(UserInput)

def TelegramListener():
    with TelegramClient('Session', api_id, api_hash) as client:
        def SendMessage(message):
            client.send_message('lukedraper', message)
        @client.on(events.NewMessage())
        async def handler(event):
            print(event.raw_text)
            commandhandler.Responder(event.raw_text)
        client.run_until_disconnected()

def Listener():
    porcupine = None
    pa = None
    audio_stream = None

    try:
        porcupine = pvporcupine.create(access_key="I1SyAIJf3kkTX5pqwnkSUp+ZQufZTjwaS1lArKNam7cXqStLvscNCQ==",keywords=["computer", "jarvis"],sensitivities=[0.75,1])

        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
                        rate=porcupine.sample_rate,
                        channels=1,
                        format=pyaudio.paInt16,
                        input=True,
                        frames_per_buffer=porcupine.frame_length)
        n = 0
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if n == 0:
                print("Keyword listener started.")
                n += 1
            if keyword_index >= 0:
                print("Detected.")
                UserInput = AudioRecorder()
                commandhandler.Responder(UserInput)
            if keyboard.is_pressed("`"):
                sys.exit()
    except KeyboardInterrupt:
        pass
    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
                pa.terminate()
