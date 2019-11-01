from mutagen.mp3 import MP3 as mp3
import pygame
import time
import Wrapper as w
import threading
import json
from msvcrt import getch

#s = w.Arduino_Controler("COM4")


Flag = True

def input_node():
    l = [0, 0, 0, 0]
    exit_flag = True

    get = '0'
    k = '0'

    n = ['1', '2', '3', '4',]
    m = []
    o = []

    def non_input():
        global exit_flag, get, k
        while exit_flag:
            if get != '0' and k == '0':
                for i in range(4):
                    if get == n[i]:
                        o.append(-1)
                        get = '0'
                    else:
                        o.append(0)
                print(o)
                return o
                #o.clear()
            elif get == '0' and k != '0':
                if k != get:
                    for i in range(4):
            # print(chr(k), n[i])
                        if k == n[i]:
                            m.append(1)
                        else:
                            m.append(0)
                    print(m)
                    get = k
                    return m
                 #   m.clear()

            else:
                print(l)
                return l
            time.sleep(0.2)


    Thread = threading.Thread(target = non_input)
    Thread.deamon = True
    Thread.start()

    while True:
        k = '0'
        k = chr(ord(getch()))
        #print(json_data)

        time.sleep(0.2)

  #  exit_flag = False

exit_flag = False


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

t = 0
json_data = []
notes = []
while Flag:
    notes = input_node()
    #notes.append([i for i in s.switch.values()])
    #time.sleep(0.2)
    json_data.append({t : nodes})
    #s.show_state()
"""
t = 0
json_data = []
for data in notes:
    json_data.append({t : data})
    t += 1
"""
json.dump(json_data,open("SampleFumen.json","w"))


s.exit_code = False


