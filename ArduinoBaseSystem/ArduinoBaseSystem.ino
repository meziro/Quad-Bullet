String string_buf;
//char *char_buf;

int outputs[] = {2,3,4,5,14,15,16,17,18,19,0};
int output_num = 11;
int inputs[] = {6};
int input_num = 1;
int *prev;

/*  Output pin details
 *  
 *  0                 : Main LED voltage instruction pin
 *  2,3,4,5           : Center LED control pin
 *  14,15,16,17,18    : Main LED control pin
 *  19                : Main LED enable pin
 *  
 *  Input pin details
 *  
 *  6                 : Center swtich voltage pin
 *  
 */ 

void setup() {
  //serial init
  Serial.begin(115200);
  Serial.setTimeout(0.5);

  Serial.println("[DEBUG]Serial port had beed initialized");
  
  //pin init

  for(int i = 0;i < output_num;i++) {
    pinMode(outputs[i],OUTPUT);
  }

  for(int i = 0;i < input_num;i++) {
    pinMode(inputs[i],INPUT);
  }

  Serial.println("[DEBUG]Pins had been initialized");

  //data init
  //char_buf = (char*)malloc(sizeof(char) * 256);
  prev = (int*)calloc(sizeof(int),input_num);
  //Full with 0(by using calloc)

  digitalWrite(19,LOW);

  delay(2000);
  Serial.println("[DEBUG]Ready!");
}

int selector = 0;

void loop() {
  //Send data

  String message = "";
  for(int i = 0;i < input_num;i++) {
    int tmp = digitalRead(inputs[i]);
    if(tmp != prev[i]) {
      message += "status_updata:{" + String(inputs[i]) + "," + String(tmp) + "};";
    }
    prev[i] = tmp;
  }

  if(message.length() != 0) {
    Serial.println(message);
  }


  //Receive data
  
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
    digitalWrite(0,LOW);
    
    //Serial.println(String(x));
    int *ptr = Encode(x);
    String tmp = "";
    for(int i = 0;i < 5;i++) {
      digitalWrite(i + 14,ptr[i]);
      //Serial.println(String(ptr[i]));
      tmp += " " + String(ptr[i]);
    }

    Serial.println(tmp);
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
