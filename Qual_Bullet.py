from mutagen.mp3 import MP3 as mp3
import pygame
import time
import Wrapper as w
import threading
import json


def main() :
	s = w.Arduino_Controller("COM7")

	fumen = read_json()

	#print(json.dumps(fumen))
	thread = threading.Thread(target = play_music)
	thread.deamon = True
	thread.start()

	Score = 0

	#first

	for i in range(len(fumen)) :
		print(fumen[i],end = " ")
		s.show_state()

		for j in range(4) :
			if(fumen[i][str(i)][j] == 1 and s.switch[j + 10] == fumen[i][str(i)][j]) :
				Score += 1

		for j in range(4) :
			if(fumen[i][str(i)][j] == 1) :
				s.LED_switch(j * 6,True)
			else :
				s.LED_switch(j * 6,False)



		"""
		if(len(fumen) - i < 6) :
			continue

		for _n in range(6) :
			n = i + _n
			for j in range(4) :
				if(fumen[n][str(n)][j] == 1) :
					s.LED_switch((6 - _n) * 6 + j,True)
				else :
					s.LED_switch((6 - _n) * 6 + j,False)
		"""
		
		time.sleep(0.2)
	

	s.exit_code = False

	print(Score)

def play_music() :
    music_filename = "firefly.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music_filename)
    mp3_length = mp3(music_filename).info.length
    pygame.mixer.music.play(1)
    time.sleep(10)
    pygame.mixer.music.stop()
    global Flag
    Flag = False


def read_json() :
	f = open("./SampleFumen.json","r")
	ret = json.load(f)
	f.close()

	return ret



if(__name__ == "__main__") :
    main()

