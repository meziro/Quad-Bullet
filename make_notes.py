from mutagen.mp3 import MP3 as mp3
import pygame
import time
import Wrapper as w
import threading

s = w.Arduino_Controler("COM4")



def play_music():
    music_filename = "hyperspeed.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_filename)
    mp3_length = mp3(music_filename).info.length
    pygame.mixer.music.play(1)
    time.sleep(mp3_length + 0.25)
    pygame.mixer.music.stop()

thread = threading.Thread(target = play_music)
thread.deamon = True
thread.start()


:q

