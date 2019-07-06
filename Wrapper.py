import serial

ser = serial.Serial('COM3',9600,timeout=None)




ser.write(b"1,2,3,4,5,6")



ser.close()
