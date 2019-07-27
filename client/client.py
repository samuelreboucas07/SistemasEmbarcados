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
client_socket.connect(('192.168.1.101', 8586))
connection = client_socket.makefile('wb')

camera = PiCamera()
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
img_counter = 0
camera.resolution = (320, 240)
camera.awb_mode = 'off'
# rg, bg = (1.6, 1.6) #ambiente dia
rg, bg = (1.6, 1.7) #ambiente noite
camera.awb_gains = (rg, bg)
camera.sharpness = 50       
while True:
    rawCapture = PiRGBArray(camera)
    camera.capture(rawCapture, format="bgr")
    frame = rawCapture.array
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)

    #print("{}: {}".format(img_counter, size))
    img_counter+=1
    client_socket.sendall(struct.pack(">L", size) + data)
    info = client_socket.recv(1024)
    if(info.decode() == "pc"):
        ser.write('1')
        #resposta = ser.readline()
        #print (resposta)
    elif(info.decode() == "pe"):
        ser.write('2')
        #resposta = ser.readline()
        #print (resposta)
    elif(info.decode() == "pd"):
        ser.write('3')
        #resposta = ser.readline()
        #print (resposta)
    elif(info.decode() == "not_d"):
        ser.write('9')
        #resposta = ser.readline()
        #print (resposta)    
    elif(info.decode() == "dc"):
        ser.write('4')
        #resposta = ser.readline()
        #print (resposta)
    elif(info.decode() == "de"):
        ser.write('5')
        #resposta = ser.readline()
        #print (resposta)
    elif(info.decode() == "dd"):
        ser.write('6')
        #resposta = ser.readline()
        #print (resposta)
    elif(info.decode() == "not_p"):
        ser.write('8')
        #resposta = ser.readline()
        #print (resposta)  
    else:
        ser.write('0')
        #resposta = ser.readline()
        #print (resposta)