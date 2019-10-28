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

	
	Sums = [0,0,0,0]
	Pushed = [0,0,0,0]

	for i in range(len(fumen)) :

		for j in range(4) :
			Sums[j] += fumen[i][str(i)][j]

		print(Sums)
		#s.show_state()

		#Print
		for offset in range(6) :
			print_place = i + offset - 1
			if(print_place <= 0 or len(fumen) <= print_place) :
				continue
			for j in range(4) :
				print_data = fumen[print_place][str(print_place)][j]
				print_led = (5 - offset) + 6 * j
				if(print_data == 1 and not Pushed[j] == 1) :
					s.LED_switch(print_led,True)
				if(print_data == -1)  :
					s.LED_switch(print_led,False)

		#Score
		Pushed = [0,0,0,0]
		for j in range(4) :
			if(s.switch[j + 10] == 1) :
				if(Sums[j] == 1) :

					print("OK")

					Score += 2
					#押したらLED消す処理(手抜きなのでLEDどころか譜面が消し飛ぶが)
					#fumen[i][j] = 0 #悪魔の力
					#それはさすがにないわ。修正
					Pushed[j] = 1
					
				else :
					Score -= 1

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

