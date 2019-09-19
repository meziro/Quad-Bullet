import serial
import time
import threading
import re

class Arduino_Controler:
    #TODO:ここにめっちゃわかりやすい説明を書く

    def __init__(self,com_port) :
        #Serialポートを初期化
        self.Serial = serial.Serial(com_port,115200,timeout=0.5)
        
        #各種変数を初期化
        self.switch = {
                2 : 0,
                3 : 0,
        }
        
        #ユーザがArduinoに送るメッセージ
        self.message = ""

        self.exit_code = True

        thread = threading.Thread(target=self.timer)
        thread.daemon = True

        self.wait_arduino()

        print("Wrapper initialize complated")

        thread.start()

    def timer(self) :
        while self.exit_code :
            s = self.Serial.readline().decode('utf-8')

            result = re.findall("status_update:{([0-9]+),([0-9]+)};",s) 
            if result:
                
                for x in result:
                    self.switch[int(x[0])] = int(x[1])


    def wait_arduino(self) :

        for i in range(10000000000):
            s = self.Serial.readline().decode('utf-8')
            print(s)
            if("Ready" in s):
                return
        exit();

    def show_state(self) :
        msg = ""
        for k,v in self.switch.items() :
            msg += ",pin:" + str(k) + "=" + str(v)
        print(msg)

x = Arduino_Controler("COM3")


for i in range(10000) :
    x.show_state()
    time.sleep(0.01)



