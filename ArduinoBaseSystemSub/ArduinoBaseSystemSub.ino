int Datas[4][6] = {0};


void setup() {
  
  int inputs[] = {14,15,16,17,18,19,2};
  for(int i = 0;i < 7;i++) {
    pinMode(inputs[i],INPUT);
  }

  int outputs[] = {4,5,6,7,8,9,10,11,12,13,3};
  for(int i = 0;i < 11;i++) 
    pinMode(outputs[i],OUTPUT);

  digitalWrite(3,LOW);
  
  //Serial.begin(9600); //消すぜ
  
  pinMode(0,OUTPUT);
  pinMode(1,OUTPUT);
}

int count = 0;

void loop() {

  // put your main code here, to run repeatedly:
  count++;
  if(count % 50 == 0) {
    Serial.println("DEBUG");
    count = 0;
  }

  if(digitalRead(2)) {
    int *input = (int*)malloc(sizeof(int) * 5);
    //String tmp = "";
    int parity_one = 0;
    int parity_two = 0;
    for(int i = 0;i < 5 ;i++) {
      input[i] = digitalRead(i + 14);
      //tmp += " " + String(input[i]);
      //tmp += String(num) + " : ";  
      //parity = oxor(parity,input[i]);
    }
  
    int result = Decode(input);
  
    //digitalWrite(result,HIGH);
    //Serial.println(String(result));
    //Serial.println(String(analogRead(5)));
  
    //Serial.println(String(digitalRead(19)));
    int inst = digitalRead(19);
    //parity = oxor(parity,inst);
    for(int i = 0;i < 3;i++)
      parity_one = oxor(parity_one,input[i]);
    for(int i = 3;i < 5;i++)
      parity_two = oxor(parity_two,input[i]);
    parity_two = oxor(parity_two,inst);

    
    Datas[result / 6][result % 6] = inst;
    Serial.println(String(result));
    free(input);
    Serial.println(String(result));

    //digitalWrite(0,parity);
    //Serial.println("parity is " + String(parity_one) + "," + String(parity_two));
    digitalWrite(0,parity_one);
    digitalWrite(1,parity_two);

    digitalWrite(3,HIGH); //終わったよーー
    delay(1);
    digitalWrite(3,LOW); //勝手に進まないでね
  }

  
   
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

int oxor(int a,int b) {
  if(a == b) return 0;
  return 1;
}

int Decode(int *data) {
  int result = 0;
  String tmp = "";
  for(int i = 0;i < 5;i++)  {
    result += mpow(2,i) * data[i];
    tmp += String(data[i]) + ",";
    //Serial.println(String(i) + ":" + String(data[i]) + ":" + String(result) + ":" + String(mpow(2,i)));
  }

  //Serial.println(tmp);
  
  return result;
}

int mpow(int x,int y) {
  int result = 1;
  for(int i = 0;i < y;i++) {
    result *= x;
  }
  return result;
}
  
