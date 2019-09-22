import serial
import time
import threading
import re

class Arduino_Controler:
    #TODO: ここにめっちゃわかりやすい説明を書く

    def __init__(self,com_port) :
        #Serial port を初期化
        self.Serial = serial.Serial(com_port,115200,timeout=0.5)

        #各種変数を初期化
        self.swtich = {
                6:0,
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

    def timer(self) :
        while self.exit_code :
            #Receive data
            s = self.Serial.readline().decode('utf-8')

            result = re.findadd("status_update:{([0-9]+),([0-9]+)};",s)

            if result:
                for x in result:
                    self.switch[int(x[0])] = int(x[1])
            
            #Send data
            if(self.message == "") :
                continue

            self.Serial.write(self.message.encode())
            self.message = "#0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24"

    def wait_arduino(self) :
        for i in range(10000000000) :
            s = self.Serial.readline().decode('utf-8')
        print(s)
        if("Ready" in s) :
            return
        exit()
    
    def show_state(self) :
        msg = ""
        for k,v in self.switch().items():
            msg += "pin:" + str(k) + "=" + str(v) + "," 
        print(msg)

    def LED_switch(self,pin,light) :
        lm = "" if(light == 1) else "#"
        self.message += lm + str(pin) + "," + lm

    def LED_swap(self,epin) :
        self.LED_switch(pin,0 if(self,LEDdatabase[pin] == 1) else 1)
        self,LEDdatabase[pin] = 0 if(self,LEDdatabase[pin] == 1) else 1
   

x = Arduino_Controler("COM3")




