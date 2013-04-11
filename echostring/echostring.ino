String str;
int d;

int pins[] = {8,9,10,11,12};

int SETUP_TIME = 100;
int WAIT_TIME = 100;

void pinsOn(int level) {
  for (int i=0; i<5; i++) {
    if (i < level) {
      digitalWrite(pins[i], HIGH);
    } else {
      digitalWrite(pins[i], LOW); 
    }
  }
}

void flashReady(int times) {
  for(int i=0; i<times; i++) {
    pinsOn(5);  
    delay(SETUP_TIME);
    pinsOn(0);
  }
}

void setup() {
    for (int i; i<5; i++) {
      pinMode(pins[i], OUTPUT);
    }
    Serial.begin(9600);
    flashReady(3);
}

void loop(){
  if (Serial.available() > 1){
    d = Serial.read();
    delay(WAIT_TIME);
    if (d > 0) {
      pinsOn(d - 48);
      Serial.println(d);
    }
  }
}
