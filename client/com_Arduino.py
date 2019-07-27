import RPi.GPIO as GPIO
import time
import serial
 
#Configura a serial e a velocidade de transmissao
ser = serial.Serial("/dev/ttyAMA0", 9600)
 
GPIO.setmode(GPIO.BOARD)
 
#Define o pino do botao como entrada
GPIO.setup(18, GPIO.IN)
 
con = 0
while(1):
    #Verifica se o botao foi pressionado
    # if GPIO.input(18) == True:
    #Envia o caracter L pela serial
    ser.write('0')
    print("Enviado - L")
    #Aguarda reposta
    #resposta = ser.readline()
    #Mostra na tela a resposta enviada
    #pelo Arduino
    #print (resposta)
    #Aguarda 0,5 segundos e reinicia o processo
    time.sleep(5)
    ser.write('1')
    print("Enviado - X")
    #Aguarda reposta
    resposta = ser.readline()
    #Mostra na tela a resposta enviada
    #pelo Arduino
    print (resposta)
    #Aguarda 0,5 segundos e reinicia o processo
    time.sleep(5)
