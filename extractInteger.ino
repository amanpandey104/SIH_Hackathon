void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  char *ptr;
  int i1;
  int i2;

  char yourstring[]=" 155, 12345, 456, 765,4.56";
  int num[10];
  int i=0;
  num[i]=atoi(yourstring);
  ptr=strchr(yourstring,',');  
  //Serial.println(ptr);
  while(ptr!=NULL)
  {
     i++;
     ptr=ptr+1;
    i1=atoi(ptr);
    num[i]=i1;
    ptr=strchr(ptr,',');
  }
  Serial.println(num[4]);
  delay(500);
  }
  
