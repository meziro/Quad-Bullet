import serial 
#import sys
#import json
import Wrapper as w
import time


LED=w.Arduino_Controler("COM4")

#if __name__=='__main__':
  #main()

#def Input():
  #return inputinfo


def Light1(self):#1~6LEDを光らしてくれる関数
  for i in range(6):
    LED.LED_switch(i + 6,1)
    time.sleep(1)
    LED.LED_switch(i + 6,0)
    hit=isHit(1,i)
    if hit == 1:
      break

def Light2(self):#7~12LEDを光らしてくれる関数
  i=7
  for i in range(6):
    LED.LED_switch(i,1)
    sleep(1)
    LED.LED_switch(i,0)
    hit=isHit(i)
    if hit==1:
      break
    i+=1


def Light3(self):#13~18LEDを光らしてくれる関数
  i=13
  for i in range(6):
    LED.LED_switch(i,1)
    sleep(1)
    LED.LED_swap(i,0)
    hit=isHit(i)
    if hit==1:
      break
    i+=1


def Light4(self):#19~24EDを光らしてくれる関数
  i=19
  for i in range(6):
    LED.LED_switch(i,1)
    sleep(1)
    LED.LED_switch(i,0)
    hit=isHit(i)
    if hit==1:
      break
    i+=1

inputInfo1=0
def isHit(self,i):#当たり判定
  inputInfo1=LED.get_state(1)
  inputInfo2=LED.get_state(2)
  inputInfo3=LED.get_state(3)
  inputInfo4=LED.get_state(4)

  hit = 0

  if inputInfo1==1:
    if i==5:
      hit=1

  elif inputInfo2==1:
    if i==11:
      hit=1

  elif inputInfo3==1:
    if i==17:
      hit=1

  elif inputInfo4==1:
    if i==23:
      hit=1
    
  return hit

def Score(hit):
  if hit==1:
    score+=1

while True: 
  inputInfo1=LED.get_state(1)
  if inputInfo1==1:
    Light1(1)
#for i in range(24):
 # LED_switch(i,0)
 # sleep(1000)

#Light1()
#while 1:
    #Light1()
    #Light2()
    #Light3()
    #Light4()
