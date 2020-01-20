import serial
ser = serial.Serial('COM21',9600)

while True:
    '''if(ser.in_waiting >0):
        line = ser.readline().strip().decode('utf-8')
        #line = line.decode('utf-8')
        print(type(line))'''
    s = "1234567890"
    ser.write(s.encode())
    k = ser.readline().decode('utf-8')
    print(k)

    

        
