import numpy as np
import Wrapper as w
import time as t
import threading

oks = [0] * 4
ac = w.Arduino_Controler("COM7")

def main() :
    for i in range(100) :
        for j in range(6):
            ac.LED_switch((i % 4) * 6 + j,1)
            oks[i % 4] = 0
            thread = threading.Thread(target=check,args=(i % 4,))
            thread.start()
            t.sleep(0.5);
            thread.alive = False
            ac.LED_switch((i % 4) * 6 + j,0);
            
            if(j == 4 and oks[i % 4]) :
                break

        t.sleep(1)


def check(num): 
    while True :
        if ac.get_state(num) :
            oks[num] = 1
            break
        else:
            t.sleep(0.1)









if __name__ == "__main__" :
    main()

