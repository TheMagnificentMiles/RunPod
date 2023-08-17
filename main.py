import os, random, time, pygame

from mutagen.mp3 import MP3

musicpath = os.path.dirname(os.path.realpath(__file__)) + "\\music\\"
music = os.listdir(musicpath)

pygame.init()
pygame.mixer.music.set_volume(1.0)

previous = ""
endTime = 0

while True:
    if endTime < int(time.time()):
        pygame.mixer.music.unload()
        choice = random.choice(music)
        while choice == previous:
            choice = random.choice(music)
        previous = choice
        audio = MP3(str(musicpath + choice))
        print(f"Playing: {choice[:-4]} ({int(audio.info.length / 60)}:{int(audio.info.length % 60)})")
        endTime = int(time.time()) + audio.info.length
        pygame.mixer.music.load(musicpath + choice)
        pygame.mixer.music.play(1)
