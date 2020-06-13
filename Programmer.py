from pygame import mixer
from datetime import datetime
from time import time

def playmusic(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def logs(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    name = input("Enter your name :")
    print(f"Welcome Mr.{name}, Have a good day!")
    init_water = time()
    init_exec = time()
    init_eyes = time()
    water_interval = 20*60
    exec_interval = 40*60
    eyes_interval = 30*60

    while True:
        if time() - init_water > water_interval:
            print("Drinking water, Enter 'done' to stop music")
            playmusic('water.mp3', 'done')
            init_water = time()
            logs("Drank water at = ")
        if time() - init_eyes > eyes_interval:
            print("Relexing eyes, Enter 'done' to stop music")
            playmusic('eye.mp3', 'done')
            init_eyes = time()
            logs("Eyes relexed at = ")
        if time() - init_exec > exec_interval:
            print("Exercising, Enter 'done' to stop music")
            playmusic('audio.mp3', 'done')
            init_exec = time()
            logs(f"Physical exercise done at = ")
