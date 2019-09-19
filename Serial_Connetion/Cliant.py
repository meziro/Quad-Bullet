import serial
import time
ser = serial.Serial('COM3',115200,timeout = 0.5)

time.sleep(1)

for i in range(10) :
    ser.write(str(i).encode())
    time.sleep(0.1)
    line = ser.readline()#.decode('utf-8')

    print(line)

ser.close()
