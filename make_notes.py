from mutagen.mp3 import MP3 as mp3
import pygame
import time
import Wrapper as w
import threading

s = w.Arduino_Controler("COM4")


Flag = True

def play_music():
    music_filename = "hyperspeed.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_filename)
    mp3_length = mp3(music_filename).info.length
    pygame.mixer.music.play(1)
    time.sleep(10)
    pygame.mixer.music.stop()
    global Flag
    Flag = False

thread = threading.Thread(target = play_music)
thread.deamon = True
thread.start()

print("test")

notes = []
while Flag:
    notes.append(s.switch.copy())
    time.sleep(0.1)
    s.show_state()

print("test2")

def print_state(x) :
    for i in range(4) :
        print(str(i + 10) + " : " + str(x[i + 10]),end = " ")
    print()

for i in notes:
    #print_state(i)
    pass

s.exit_code = False 
