#include <string.h>
int my_led = 12;
char var;
String temp = "";
String data = "";

#include <Servo.h>
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(my_led,OUTPUT);
  pinMode(LED_BUILTIN,OUTPUT);
}

void loop() {
   
  data = "";
  while(Serial.available()){
    var = Serial.read();
    temp = String(var);
    data+=temp;
  }
  //Serial.println(data);
  double LAX = (data.substring(0,3)).toDouble();
  double LAY = (data.substring(4,8)).toDouble();
  double LTpveRTnve = (data.substring(9,13)).toDouble();
  double RAY = (data.substring(14,18)).toDouble();
  double RAX = (data.substring(19,24)).toDouble();
  int A = (data.substring(25,27)).toInt();
  int B = (data.substring(28,30)).toInt();
  int X = (data.substring(31,33)).toInt();
  int Y = (data.substring(34,36)).toInt();
  int LB = (data.substring(37,39)).toInt();
  int RB = (data.substring(40,42)).toInt();
  int Back = (data.substring(43,45)).toInt();
  int Start = (data.substring(46,48)).toInt();
  Serial.println(LAX);
  Serial.println(LAY);
  Serial.println(LTpveRTnve);
  Serial.println(RAY);
  Serial.println(RAX);
  Serial.println(A);
  Serial.println(B);
  Serial.println(X);
  Serial.println(Y);
  Serial.println(LB);
  Serial.println(RB);
  Serial.println(Back);
  Serial.println(Start);
  /*if(LAY>0){
    digitalWrite(my_led,HIGH);
  }
  else{
    digitalWrite(my_led,LOW);
  }*/
  delay(500);
}
