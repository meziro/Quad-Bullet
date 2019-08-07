int Datas[4][6] = {0};


void setup() {
  
  int inputs[] = {14,15,16,17,18,19};
  for(int i = 0;i < 6;i++) {
    pinMode(inputs[i],INPUT);
  }
  

  int outputs[] = {4,5,6,7,8,9,10,11,12,13};
  for(int i = 0;i < 10;i++) {
    pinMode(outputs[i],OUTPUT);
  }

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  
  int *input = (int*)malloc(sizeof(int) * 5);
  for(int i = 0;i < 5 ;i++) {
    input[i] = digitalRead(i + 14);
  }
  
  int result = Decode(input);
  free(input);

  //digitalWrite(result,HIGH);
  //Serial.println(String(result));
  //Serial.println(String(analogRead(5)));

  //Serial.println(String(digitalRead(19)));
  Datas[result / 6][result % 6] = digitalRead(19);
  
   
  for(int Clock = 0;Clock < 4;Clock++) { //クロック制御
    for(int Counter = 0;Counter < 6;Counter++) {
      digitalWrite(Counter + 8,LOW);
      if(Datas[Clock][Counter]) {
        digitalWrite(Counter + 8,HIGH);
        //Serial.write("TEST");
      } else {
        //digitalWrite(Counter + 8,LOW);
      }
    }

    for(int i = 0;i < 4;i++) {
      digitalWrite(i + 4,HIGH);
    }
    digitalWrite(Clock + 4,LOW);
    delay(3);
  }
}

int Decode(int *data) {
  int result = 0;
  for(int i = 0;i < 5;i++)  {
    result += mpow(2,i) * data[i];
    //\Serial.println(String(i) + ":" + String(data[i]) + ":" + String(result) + ":" + String(mpow(2,i)));
  }
  
  return result;
}

int mpow(int x,int y) {
  int result = 1;
  for(int i = 0;i < y;i++) {
    result *= x;
  }
  return result;
}
  
