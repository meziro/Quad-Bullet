String string_buf;
char *char_buf;

void setup() {
  //pin init
  //pinMode(7, OUTPUT);

  int outputs[] = {2,3,4};
  for(int i = 0;i < sizeof(outputs) / sizeof(int);i++) {
    pinMode(outputs[i],OUTPUT);
  }

  

  //digitalWrite(7, HIGH);

  //serial init
  Serial.begin(9600);
  Serial.setTimeout(10);

  //data init
  char_buf = (char*)malloc(sizeof(char) * 256);
}



void loop() {
  //send data

  // ...



  if (Serial.available() <= 0) return; //no data that we should receive

  string_buf = Serial.readString(); //receive data

  int lastest = 0;
  int light_status = HIGH;

  for (int read_count = 0; read_count < string_buf.length() - 1; read_count++) {
    switch (string_buf[read_count]) {
      case ',': {
        String ss = string_buf.substring(lastest,read_count + 1); 
        lastest = read_count + 1;

        Serial.print(String(ss.toInt(),10)[0]);
        Serial.print("を、状態");
        Serial.print(String(light_status,10)[0]);
        Serial.println("にします");

        digitalWrite(ss.toInt(),light_status);

        break;
      }
      case '#': {
        light_status = !light_status;
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
