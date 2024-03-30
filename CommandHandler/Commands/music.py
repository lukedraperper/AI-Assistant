import os, glob
import time
import random
import contextlib
import string
import yt_dlp
with contextlib.redirect_stdout(None):
    import pygame
import threading
import re, requests, subprocess, urllib.parse, urllib.request
from yt_dlp import YoutubeDL
playlist = []

def IfEnded():
    global playlist
    song = pygame.mixer.Sound(playlist[0])
    while len(playlist) != 0:
        if pygame.mixer.music.get_busy() != 1:
            if pygame.mixer.music.get_pos() != -1:
                pass
            else:
                playlist.pop(0)
                time.sleep(1)
                pygame.mixer.music.load(playlist[0])
                pygame.mixer.music.play()
        else:
            pass
    return "That's the end of your playlist sir."
def Playlist(voice_data):
    global playlist
    os.chdir(os.path.dirname(os.path.realpath(__file__))+ "\songs")
    for musicfile in glob.glob("*.mp3"):
        playlist.append(musicfile)
    for i in range(random.randint(0,25)):
        random.shuffle(playlist)
    if voice_data == "alarm":
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.dirname(os.path.realpath(__file__))+ "\Sounds\\alarmsound.mp3")
        pygame.mixer.music.play()
    else:
        pygame.mixer.init()
        pygame.mixer.music.load(playlist[0])
        pygame.mixer.music.play()

        ifended = threading.Thread(target=IfEnded)
        ifended.start()
def PlayMusic(voice_data):
    voice_data = voice_data.split("play",1)[1].strip()
    if len(voice_data) < 1:
        pass
    else:
        os.chdir(os.path.dirname(os.path.realpath(__file__))+ "\ytsongs")
        query_string = urllib.parse.urlencode({"search_query": voice_data})
        formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string + "+offical+audio")
        search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

        ydl_opts = {
            'format': 'bestaudio',
            'ffmpeg_location':'C:\\ffmpeg\\bin\\ffmpeg.exe',
            'quiet':True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(clip2, download=False)
            video_title = info_dict.get('title', None)
            title = video_title
            for char in string.punctuation:
                title = title.replace(char, '')
                
        print(title)
        n = 0
        for song in glob.glob("*.mp3"):
            if f"{title}" in song[0:-17]:
                n += 1
                pygame.mixer.init()
                pygame.mixer.music.load(song)
                pygame.mixer.music.play()
        if n == 0:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([clip2])
            for file in os.listdir("./"):
                print(file[0:-17])
                if f"{title}" in file[0:-17]:
                    filename = file
            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
