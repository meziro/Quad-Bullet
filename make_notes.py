from mutagen.mp3 import MP3 as mp3
import pygame
import time
import Wrapper as w
import threading
import json

s = w.Arduino_Controler("COM4")


Flag = True

def play_music():
    music_filename = "firefly.mp3"
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

notes = []
while Flag:
    notes.append([i for i in s.switch.values()])
    time.sleep(0.2)
    s.show_state()

t = 0
json_data = []
for data in notes:
    json_data.append({t : data})
    t += 1

json.dump(json_data,open("SampleFumen.json","w"))


s.exit_code = False 
