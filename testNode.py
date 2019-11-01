import threading
import time
from msvcrt import getch

l = [0, 0, 0, 0]
exit_flag = True

get = '0'
k = '0'

n = ['1', '2', '3', '4',]
m = []
o = []

def non_input():
    global exit_flag, get, k
    while exit_flag:
        if get != '0' and k == '0':
            for i in range(4):
                if get == n[i]:
                    o.append(-1)
                    get = '0'
                else:
                    o.append(0)
            print(o)
            o.clear()
        elif get == '0' and k != '0':
            if k != get:
                for i in range(4):
        # print(chr(k), n[i])
                    if k == n[i]:
                        m.append(1)
                    else:
                        m.append(0)
                print(m)
                get = k
                m.clear()

        else:
            print(l)
        time.sleep(0.2)


thread = threading.Thread(target = non_input)
thread.deamon = True
thread.start()

while True:
    k = '0'
    k = chr(ord(getch()))

    time.sleep(0.2)

exit_flag = False
