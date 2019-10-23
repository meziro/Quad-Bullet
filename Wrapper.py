import serial
import time
import threading
import re

class Arduino_Controller:
    #TODO: ここにめっちゃわかりやすい説明を書く

    def __init__(self,com_port) :
        #Serial port を初期化
        self.Serial = serial.Serial(com_port,2000000,timeout=0.001)

        #各種変数を初期化
        self.switch = {
                10:0,
                11:0,
                12:0,
                13:0,
                }
        self.LEDdatabase = [0] * 24

        #ユーザがArduinoに送るメッセージ
        self.message = ""

        self.exit_code = True

        thread = threading.Thread(target=self.timer)
        thread.deamon = True

        self.wait_arduino()

        print("Wrapper initialize complated")

        thread.start()

        self.message = "~0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24*"

        time.sleep(1)

    def timer(self) :
        while self.exit_code :
            #Receive data
            s = self.Serial.readline().decode('utf-8')

            if(len(s) != 0) :
                #print(s)
                pass
            result = re.findall("status_update:{([0-9]+),([0-9]+)};",s)

            if result:
                for x in result:
                    self.switch[int(x[0])] = int(x[1])

            #Send data
            if(self.message == "") :
                continue
            
            print(self.message + "*")

            self.Serial.write((self.message + "*").encode())
            self.message = ""
        
        self.Serial.close()

    def wait_arduino(self) :
        for i in range(10000000000) :
            s = 0
            try:
                s = self.Serial.readline().decode('utf-8')
            except:
                continue
            if(len(s) != 0):
                print(s)
            if("Ready" in s) :
                return
        exit()
    
    def show_state(self) :
        msg = ""
        for k,v in self.switch.items():
            msg += "pin:" + str(k) + "=" + str(v) + "," 
        print(msg)

    def LED_switch(self,pin,light) :
        lm = "" if(light == 1) else "~"
        self.message += lm + str(pin) + "," + lm

    def LED_swap(self,epin) :
        self.LED_switch(pin,0 if(self,LEDdatabase[pin] == 1) else 1)
        self,LEDdatabase[pin] = 0 if(self,LEDdatabase[pin] == 1) else 1
   
    def get_state(self,x) :
        return self.switch[x + 10]



#for i in range(24) :
#    x.LED_switch(i,1)
#    time.sleep(1)


#for i in range(24) :
#    x.LED_switch(i,0)
#    time.sleep(1)


