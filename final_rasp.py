import cv2
import io
import socket
import struct
import time
import pickle
import threading

server_address = ('192.168.1.167',5002)

cam = cv2.VideoCapture(0)

cam.set(3, 320);
cam.set(4, 240);

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

def send():
    sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock1.bind(server_address)
    sock1.listen(5)
    conn,addr = sock1.accept()
    while True:
        data = conn.recv(1024)
        msg = pickle.loads(data)
        print("Received:",msg)
        time.sleep(.01)

def recv():
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
