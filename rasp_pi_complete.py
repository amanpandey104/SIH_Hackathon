import cv2
import io
import socket
import struct
import time
import pickle
import threading
import serial

ser = serial.Serial('COM7',9600)
msg = ""

server_address = ('192.168.1.167',5002)

cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

def recv():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(server_address)
    sock1.listen(5)
    conn,addr = sock1.accept()
    while True:
        data = conn.recv(1024)
        try:
            msg = pickle.loads(data)
        except:
            continue
        ser.write(msg.encode())
        k = ser.readline().decode('utf-8')
        k1 = ser.readline().decode('utf-8')
        k2 = ser.readline().decode('utf-8')
        k3 = ser.readline().decode('utf-8')
        k4 = ser.readline().decode('utf-8')
        k5 = ser.readline().decode('utf-8')
        k6 = ser.readline().decode('utf-8')
        k7 = ser.readline().decode('utf-8')
        k8 = ser.readline().decode('utf-8')
        k9 = ser.readline().decode('utf-8')
        k10 = ser.readline().decode('utf-8')
        k11 = ser.readline().decode('utf-8')
        k12 = ser.readline().decode('utf-8')
        print(k,k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12)
        #print("Received:",msg)
        #ardToPi(msg)

def send():
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.connect(('192.168.1.168',5001))
    connection = sock2.makefile('wb')
    while True:
        ret, frame = cam.read()
        result, frame = cv2.imencode('.jpg', frame, encode_param)
        data = pickle.dumps(frame, 1)
        size = len(data)

        sock2.sendall(struct.pack(">L", size) + data)

    cam.release()

sending = threading.Thread(target=send)
receiving = threading.Thread(target = recv)

sending.start()
receiving.start()

sending.join()
receiving.join()
