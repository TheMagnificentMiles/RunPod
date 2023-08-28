import os, random, time, pygame

os.system("bluetoothctl power on")
os.system("bluetoothctl connect 0C:3B:50:7E:66:B0")
print("Bluetooth connected")

time.sleep(1)
os.system("sudo rfcomm bind 0 0C:3B:50:7E:66:B0")
print("Binded")

time.sleep(1)

musicpath = "/home/runpod/Desktop/RunPod/music/"
music = os.listdir(musicpath)

pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

previous = ["" for x in range(5)]

while True:
    if not pygame.mixer.music.get_busy():
        choice = random.choice(music)
        while choice in previous:
            choice = random.choice(music)
        previous.pop(0)
        previous.append(choice)
        print(f"Playing: {choice[:-4]}")
        pygame.mixer.music.load(musicpath + choice)
        pygame.mixer.music.play(1)
