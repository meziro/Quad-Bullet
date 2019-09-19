int num = 2; //2,3,4,5
int inputs[] = {2,3};
int prev[] = {0,0};

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.setTimeout(0.5);
  
  Serial.println("**Serial Port initialized**");

  for(int i = 0;i < num;i++) {
    pinMode(inputs[i],HIGH);
  }

  Serial.println("**Pins initialized**");

  Serial.println("**Ready**");
  delay(3000);
}

void loop() {
  // put your main code here, to run repeatedly:

  String message = "";
  for(int i = 0;i < num;i++) {
    int tmp = digitalRead(inputs[i]);
    if(tmp != prev[i]) {
      //Serial.println("電圧の変化を検知,Pin = " + String(inputs[i]) + " to " + String(tmp));
      message += "status_update:{" + String(inputs[i]) + "," + String(tmp) + "};";
      prev[i] = tmp;
    }
  }

  if(message.length() != 0) {
    Serial.println(message);
  }
  
  if(Serial.available() == 0) return;


  /*
  String str = Serial.readStringUntil(';');
  delay(1000);
  Serial.println(String(str.toInt()));
  */
}
