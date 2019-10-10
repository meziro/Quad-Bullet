import time
import Wrapper as w

s = w.Arduino_Controler("COM4")

for i in range(200) :
    s.LED_switch(0,i % 2)
    time.sleep(0.01)


s.exit_code = False
