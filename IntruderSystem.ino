#define trig 7
#define echo 8
#define Buzz 11
#define BoltDigital 4
#define boltWrite 3
int d1, d2, distance, i;
long duration;

void setup() {
  // put your setup code here, to run once:
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(Buzz, OUTPUT);
  pinMode(BoltDigital, OUTPUT);
  pinMode(boltWrite, INPUT);


}


void loop() {
  // put your main code here, to run repeatedly:
  Ultrasonic(trig, echo);
  d2 = distance;
  if(digitalRead(boltWrite) == 1)
  {
    if(d2 <= 20)//if distance is less than 40
    {
      digitalWrite(Buzz, HIGH);//turn the buzzer on
      digitalWrite(BoltDigital, HIGH);
      for(int i=0; i<100; i++) 
      { //do this 255 times
        analogWrite(Buzz, i); //raise the voltage sent out of the pin by 1
        delay(150); //wait 10 milliseconds to repeat 
      }

      for(int i=100; i>0; i--)
      { // do this 255 times
          analogWrite(Buzz, i); //lower the voltage sent out of the pin by 1
          delay(150); //wait 10 milliseconds to repeat
        
      }
    }
    else
    {
      digitalWrite(Buzz, LOW);//turn the buzzer off
      digitalWrite(BoltDigital, LOW);
    }
  }

}

void Ultrasonic(int Trig, int Echo)
{
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);
  duration = pulseIn(Echo, HIGH);
  distance = 0.034 * duration/2;
}
