
//Code to extract integers from a srtring seperated by "," and whitespaces and store them as seperate elements of an array 
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  char *ptr;
  int i1;

  char yourstring[]="155, 12345, 456, 765, 489";
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
  for(int j=0;j<=i;j++)
  {
  Serial.println(num[j]);
  }
  delay(500);
  }
  
