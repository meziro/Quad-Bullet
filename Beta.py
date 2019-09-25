import Wrapper as w
import time
import threading

s = w.Arduino_Controler("COM7")

num = 0

ar = [0] * 4;

def light() :
  x = num
  for j in range(6):
    s.LED_switch(x * 6 + j,1)
    time.sleep(0.5)
    s.LED_switch(x * 6 + j,0)
  ar[x] = 0

while True :
  for i in range(4):
    if(ar[i] == 0 and s.get_state(i + 1)):
      ar[i] = 1
      num = i
      thread = threading.Thread(target = light)
      thread.deamon = True
      thread.start()
      

