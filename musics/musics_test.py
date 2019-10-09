from mutagen.mp3 import MP3 as mp3
import pygame
import time

filename = "firefly.mp3"
pygame.mixer.init()
pygame.mixer.music.load(filename)
mp3_length = mp3(filename).info.length
pygame.mixer.music.play(1)
time.sleep(mp3_length + 0.25)
pygame.mixer.mucis.stop()
