from mutagen.mp3 import MP3 as mp3
import pygame
import time
import threading
import json
import sys
t = 0
note = []
timeout = 10
startTime = time.time()
from msvcrt import getch
def Input():
    zero = [0,0,0,0]
    line = ['1','2','3','4',]
    #note = []


while True:
    if chr(ord(getch()))==1:
        note.insert(0,1)
    elif time.time() - startTime > timeout:
        note.insert(0,0)
    if chr(ord(getch()))==2:
        note.insert(1,1)
    elif time.time() - startTime > timeout:
        note.insert(1,0)
    if chr(ord(getch()))==3:
        note.insert(2,1)
    elif time.time() - startTime > timeout:
        note.insert(2,0)
    if chr(ord(getch()))==4:
        note.insert(3,1)
    elif time.time() - startTime > timeout:
        note.insert(3,0)
    break
print(note)
