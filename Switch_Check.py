import Wrapper as w
import time
import threading

s = w.Arduino_Controller("COM3")
flag = True

def end() :
    global flag
    time.sleep(20)
    flag = False

thread = threading.Thread(target = end)
thread.start()

while flag:
    for i in range(4):
        if s.switch[i + 10] :
            print(str(i))
            s.LED_switch(i * 6,True)
        else :
            s.LED_switch(i * 6,False)

    time.sleep(0.1)

s.exit_code = False
