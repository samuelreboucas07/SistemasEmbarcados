import cv2
import io
import socket
import struct
import time
import pickle
import zlib
from picamera.array import PiRGBArray
from picamera import PiCamera
import RPi.GPIO as GPIO
import serial

ser = serial.Serial("/dev/ttyAMA0", 9600)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.101', 8585))
connection = client_socket.makefile('wb')

camera = PiCamera()
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
img_counter = 0

while True:
    rawCapture = PiRGBArray(camera)
    camera.capture(rawCapture, format="bgr")
    frame = rawCapture.array
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)

    print("{}: {}".format(img_counter, size))
    img_counter+=1
    client_socket.sendall(struct.pack(">L", size) + data)
    info = client_socket.recv(1024)
    if(info.decode() == "pessoa"):
        ser.write("P")
        print("Enviado - L")
        resposta = ser.readline()
        print (resposta)
    else:
        ser.write("X")
        print("Enviado - X")
        resposta = ser.readline()
        print (resposta)



