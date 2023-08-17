import os, random
import time

from playsound import playsound
from mutagen.mp3 import MP3

musicpath = os.path.dirname(os.path.realpath(__file__)) + "\\music\\"
music = os.listdir(musicpath)

previous = ""
endTime = 0

while True:
    if endTime < int(time.time()):
        choice = random.choice(music)
        while choice == previous:
            choice = random.choice(music)
        previous = choice
        audio = MP3(str(musicpath + choice))
        print(f"{choice} ({int(audio.info.length)}s)")
        playsound(str(musicpath + choice), False)
        endTime = int(time.time()) + audio.info.length
