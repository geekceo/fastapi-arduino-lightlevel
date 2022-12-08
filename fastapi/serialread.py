import serial

def read():
    ser = serial.Serial()
    ser.baudrate = 9600 #read/write speed (must be equal to Arduino Serial speed), 9600 - default
    ser.port = 'COM10' #write your COM-port with Arduino. Check Arduino IDE -> Tools -> Port

    ser.open()

    return ser.readline().decode('utf-8').rstrip() #decode bytes to utf-8 string and remove the '\n'

read()