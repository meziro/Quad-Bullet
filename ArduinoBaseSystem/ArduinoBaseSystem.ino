String string_buf;
char *char_buf;

void setup() {
  //pin init
  //pinMode(7, OUTPUT);

  int outputs[] = {2,3,4,5,14,15,16,17,18,19};
  for(int i = 0;i < 10;i++) {
    pinMode(outputs[i],OUTPUT);
  }

  

  //digitalWrite(7, HIGH);

  //serial init
  Serial.begin(9600);
  Serial.setTimeout(10);

  //data init
  char_buf = (char*)malloc(sizeof(char) * 256);

  digitalWrite(19,LOW);
}

int selector = 0;


void loop() {
  //init

  
  //send data

  /*
  digitalWrite(14,HIGH);
  digitalWrite(15,HIGH);
  digitalWrite(16,LOW);
  digitalWrite(17,LOW);
  digitalWrite(18,LOW);
  digitalWrite(19,HIGH);
  */
  
  // ...
  
  

  if (Serial.available() <= 0) return; //no data that we should receive

  string_buf = Serial.readString(); //receive data

  int lastest = 0;
  int light_status = HIGH;
  
  for (int read_count = 0; read_count < string_buf.length(); read_count++) {
    switch (string_buf[read_count]) {
      case ',': {
        String ss = string_buf.substring(lastest,read_count + 1); 
        lastest = read_count + 1;

        digitalWrite(19,light_status);
        Serial.println(String(light_status));
        control(ss.toInt());

        delay(15);
        
        /*
        Serial.print(String(ss.toInt(),10)[0]);
        Serial.print("を、状態");
        Serial.print(String(light_status,10)[0]);
        Serial.println("にします");

        digitalWrite(ss.toInt(),light_status);
        */
        
        break;
      }
      case '#': {
        light_status = light_status ? LOW : HIGH;
        lastest = read_count + 1;
        break;
      }
      default :{
        //Serial.write("error");
        
        break;
      }
    }
  }
}




void control(int x) {
  if(0 <= x && x <= 23) {
    //Serial.println(String(x));
    int *ptr = Encode(x);
    for(int i = 0;i < 5;i++) {
      digitalWrite(i + 14,ptr[i]);
      //Serial.println(String(ptr[i]));
    }
    //Serial.println("");
    free(ptr);
  } else {
  }
}



int* Encode(int x) {
  int *result = (int*)calloc(sizeof(int),5);

  for(int i = 0;x != 0;i++) {
    result[i] = x % 2;
    x /= 2;
  }

  return result;
}
