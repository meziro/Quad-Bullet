import Wrapper as w
import time

s = w.Arduino_Controller("COM7")

for i in range(25) :
    #s.LED_switch(i - 1,False)
    s.LED_switch(i,True)
    time.sleep(0.2)

s.exit_code = False
