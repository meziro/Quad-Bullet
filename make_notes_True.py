from mutagen.mp3 import MP3 as mp3
import pygame
import time
#import Wrapper as w
import threading
import json
from msvcrt import getch

#s = w.Arduino_Controler("COM4")

exit_flag = True

Max = 1000
get = '0'
k = '0'
t = 0

json_data = []

Flag = True

def non_input():
    l = [0, 0, 0, 0]
    n = ['1', '2', '3', '4',]
    m = []
    o = []
    global exit_flag, get, k, t, json_data
    while exit_flag:
        if get != '0' and k == '0':
            for i in range(4):
                if get == n[i]:
                    o.append(-1)
                    get = '0'
                else:
                    o.append(0)
            json_data.append({t : o})
            print(json_data[t])
        elif get == '0' and k != '0':
            if k != get:
                for i in range(4):
                    if k == n[i]:
                        m.append(1)
                    else:
                        m.append(0)
                json_data.append({t : m})
                print(json_data[t])
                get = k

        else:
            json_data.append({t : l})
            print(json_data[t])
        t += 1
        if t == Max:
            break
        o = []
        m = []
        time.sleep(0.2)

def play_music():
    music_filename = "firefly.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_filename)
    mp3_length = mp3(music_filename).info.length
    print(mp3_length)
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()
    global Flag
    Flag = False

thread = threading.Thread(target = play_music)
thread.deamon = True
thread.start()

thread2 = threading.Thread(target = non_input)
thread2.deamon = True
thread2.start()

while Flag:
    if t == Max:
        break
    k = '0'
    k = chr(ord(getch()))
    time.sleep(0.2)


    #notes = input_node()
    #notes.append([i for i in s.switch.values()])
    #time.sleep(0.2)
    #json_data.append({t : notes})
    #s.show_state()
print(json_data)
exit_flag = False

# f = open("testJson.json", 'w')
json.dump(json_data,open("SampleFumen.json","w"))


#s.exit_code = False
