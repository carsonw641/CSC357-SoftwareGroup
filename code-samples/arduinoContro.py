import serial
arduino = serial.Serial('COM5', 9600, timeout=.1)
g=0
while True:
    g=g+1
    data= arduino.readline()[:-2]
    if g==20:
        arduino.write(b'2')
    elif g==40:
        arduino.write(b'3')
    elif g==60:
        arduino.write(b'1')
    elif g==80:
        arduino.write(b'0')
    elif g==81:
        g=0
    if data:
        print(data)