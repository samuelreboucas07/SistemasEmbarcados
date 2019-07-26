from threading import Thread
import sys

class Th2(Thread):
  def __init__ (self):
    Thread.__init__(self)

  def run(self):
      print("y")

class Th(Thread):
  def __init__ (self):
    Thread.__init__(self)

  def run(self):
	  print("x")


while True:
  thread = Th()
  thread.start()
  thread2 = Th2()
  thread2.start()

  # Criando duas threads capazes de paralelizar processamento, logo, é necessário cada função retornar um valor.


# https://www.embarcados.com.br/raspberry-pi-comunicacao-serial-uart/

#https://www.filipeflop.com/blog/comunicacao-serial-arduino-com-raspberry-pi/
