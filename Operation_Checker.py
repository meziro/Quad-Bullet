import Wrapper as w
import time

s = w.Arduino_Controller("COM3")

for i in range(25) :
    #s.LED_switch(i - 1,False)
    s.LED_switch(i,True)
    time.sleep(0.2)

for i in range(25) :
    s.LED_switch(i,False)
time.sleep(2)
for i in range(25) :
    s.LED_switch(i,True)
time.sleep(2)
for i in range(25) :
    s.LED_switch(i,False)
time.sleep(2)
for i in range(25) :
    s.LED_switch(i,True)

s.exit_code = False
