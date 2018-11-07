int ledPin = 13;
int lockPin=12; 
int state = 0;
int flag = 0; 
int lockEvent;

int lockResetTimer = 3000;
long lockTime = 0;

void setup() {
 pinMode(ledPin, OUTPUT);
 digitalWrite(ledPin, LOW);
 pinMode(lockPin, OUTPUT);
 digitalWrite(lockPin,LOW);
 Serial.begin(9600); // Default connection rate for my BT module
 
 Serial.println("Starting Arduino....");
}
 
void loop() {  
 if(millis() - lockTime >= lockResetTimer){
   Serial.println("Locking");
   flag = 0;
   lock();
 }
  
  if(Serial.available() > 0){
   state = Serial.read();
   flag=0;
 }


 if (state == '0') {
  ledOff();
 }

 else if (state == '1') {
  ledOn();
 }

//Unlock the lock
else if(state=='2'){
   unlock();  
}

//Lock the lock
else if(state=='3'){
  lock();
 }
 
 state = -1;
}


//Turn led on
void ledOn(){
 digitalWrite(ledPin, HIGH);
 
 if(flag == 0){
   Serial.println("LED: on");
   flag = 1;
 }
}

//Turn led off
void ledOff(){
   digitalWrite(ledPin, LOW);
   
   if(flag == 0){
   Serial.println("LED: off");
   flag = 1;
   }
}


//Unlock the lock
void unlock(){
  digitalWrite(lockPin,HIGH);
  
  if(flag==0){
    Serial.println("Unlocked");
    flag=1;
    
    lockTime = millis();
  }
}

//Function to lock the lock
void lock(){
  digitalWrite(lockPin,LOW);
  
  if(flag==0){
    Serial.println("Locked");
    flag=1;
  }
}
