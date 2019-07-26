import socket
import sys
import pickle
import numpy as np
import struct ## new
import zlib
from threading import Thread
import cv2

from main import Pessoa
from porta_cor import Porta

class Th(Thread):
  def __init__ (self, image):
    Thread.__init__(self)
    self.image = image

  def run(self):
      Porta.detect(image)

class Th2(Thread):
  def __init__ (self, image):
    Thread.__init__(self)
    self.image = image
  def run(self):
    detect = Pessoa.pessoa(image)
    if(detect):
        conn.send(("pessoa").encode('utf-8'))
    else:
        conn.send(("not").encode('utf-8'))

HOST=''
PORT=8585

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST,PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
#print("payload_size: {}".format(payload_size))

while True:
    while len(data) < payload_size:
     #   print("Recv: {}".format(len(data)))
        data += conn.recv(4096)
    #print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    #print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    image = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    thread = Th(image)
    thread.start()
    thread2 = Th2(image)
    thread2.start()