import serial

ser = serial.Serial('COM7',9600,timeout=None)

ser.write(b"0,1,2,3,4,5,6,7,")


ser.close()
