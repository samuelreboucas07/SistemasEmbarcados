#include <NewPing.h> //https://cluberobotica.wordpress.com/2017/11/29/newping/
//A biblioteca “NewPing” permite a utilização até 15 sensores ultrasónicos e adiciona novos recursos para utilização destes sensores.

int IN1 = 9;
int IN2 = 10;
int velocidadeA = 8;

//Motor B
int IN3 = 11;
int IN4 = 12;
int velocidadeB = 13;

char buf;

//Sensores Ultrassonicos
//sensor A1 - amarelo
#define TRIGGER_PIN1 16
#define ECHO_PIN1 17

//sensor A2 -verde
#define TRIGGER_PIN2 18
#define ECHO_PIN2 19

//sensor F1 - azul
#define TRIGGER_PIN3 20 
#define ECHO_PIN3 21

//sensor F2 - roxo
#define TRIGGER_PIN4 14
#define ECHO_PIN4 15

NewPing sonar1(TRIGGER_PIN1, ECHO_PIN1);

NewPing sonar2(TRIGGER_PIN2, ECHO_PIN2);

NewPing sonar3(TRIGGER_PIN3, ECHO_PIN3);

NewPing sonar4(TRIGGER_PIN4, ECHO_PIN4);

float sA1, sA2, sF1, sF2, sf, sa;

//Sensores Infravermelhos
const int sensor1 = 4; //PINO DIGITAL UTILIZADO PELO MÓDULO
const int sensor2 = 3; //PINO DIGITAL UTILIZADO PELO MÓDULO

void setup(){
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT); //DEFINE O PINO COMO ENTRADA
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(velocidadeA,OUTPUT);
  pinMode(velocidadeB,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  
  delay(1000);

  buf = Serial.read();
    // Caso seja recebido o caracter L, acende o led
    if (buf == 'P')
    {
      // Liga ou desliga o led da porta 13
      digitalWrite(5, 1);
      // Envia a resposta para o Raspberry
      Serial.println("Recebido! - Estado Led: LIGADO");
    }

        // Caso seja recebido o caracter L, acende o led
    if (buf == 'X')
    {
      // Liga ou desliga o led da porta 13
      digitalWrite(5, 0);
      // Envia a resposta para o Raspberry
      Serial.println("Recebido! - Estado Led: DESLIGADO");
    }
  
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(velocidadeA,80);
  
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(velocidadeB,123.8);
  
  //Logica Sensores Ultrassonicos
  sA1=sonar1.ping_cm();
  sA2=sonar2.ping_cm();
  sa=(sA1+sA2)/2;
  //Serial.print(" / Ping aereo: ");
  //Serial.print(sa);
  //Serial.println(sA1);
  //Serial.println(sA2);
  
  sF1=sonar3.ping_cm();
  sF2=sonar4.ping_cm();
  sf=(sF1+sF2)/2; 
  //Serial.println(sF1);
  //Serial.println(sF2);
  
  //Serial.print(" / Ping frontal: ");
  //Serial.print(sf);
  //Serial.println("cm"); 

  if(sf<=45){
    Serial.print("Obstculo frontal a: ");
    Serial.print(sf);
    Serial.println("cm");
    analogWrite(velocidadeA,0);
    analogWrite(velocidadeB,0);
    
  }  
  
  if(sa>=100 && sa<=190){
    Serial.print("Obstculo aereo a:");
    Serial.print(sa);
    Serial.println("cm");
    analogWrite(velocidadeA,0);
    analogWrite(velocidadeB,0);
  }
  
  //Logica Sensores Infravermelhos
  if(digitalRead(sensor1)!=LOW || digitalRead(sensor2)!=LOW){
    Serial.println ("Buraco detectado");
    analogWrite(velocidadeA,0);
    analogWrite(velocidadeB,0);
    
    }else{
    Serial.println ("Buraco NAO detectado");
  }
  
  //OBS: o sensor de infravermelho esta detectando apenas descida de meio fio e buracos com proporçoes semelhantes a meio fio ou maiores
}
