int outputs[] = {2,3,4,5,14,15,16,17,18,19};
int output_num = 10;
int inputs[] = {10,11,12,13};
int input_num = 4;
int *switch_state_prev;

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
  Serial.setTimeout(1);

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
  switch_state_prev = (int*)calloc(sizeof(int),input_num);
  //Full with 0(by using calloc)

  digitalWrite(19,LOW);

  delay(1000);
  Serial.println("[DEBUG]Ready!");
}

String Onetime_Control_Message = ""; //1つのシリアル通信で送られるメッセージの置き場
String Complate_Control_Message = ""; //1つの命令っメッセージ

void loop() {
  //Send data

  String message = "";
  for(int i = 0;i < input_num;i++) {
    int tmp = digitalRead(inputs[i]);
    if(tmp != switch_state_prev[i]) {
      message += "status_updata:{" + String(inputs[i]) + "," + String(tmp) + "};";
    }
    switch_state_prev[i] = tmp;
  }

  if(message.length() != 0) {
    Serial.println(message);
  }

  //Receive data
  
  if (Serial.available() <= 0) return; //no data that we should receive

  //string_buf = Serial.readString(); //receive data
  Onetime_Control_Message = Serial.readString();
  int s_len = Onetime_Control_Message.length();

  int read_count = 0;
  int prev = 0;
  for(auto it = Onetime_Control_Message.begin();it != Onetime_Control_Message.end();it++) {
     if(*it == '*') { //命令が終わった
      Complate_Control_Message += Onetime_Control_Message.substring(prev,read_count + 1);

      Tokenize_Control_Message(Complate_Control_Message);
      
      Complate_Control_Message = "";
      prev = read_count + 1;
    } else if(read_count == s_len - 1) { //終端文字なしで1つのシリアル通信が終了
      String tmp = Onetime_Control_Message.substring(prev,read_count + 1);
      if(tmp != "\n") {
        Complate_Control_Message += Onetime_Control_Message.substring(prev,read_count + 1);
      }
    }
    read_count++;
  }
  
}

int light_state = HIGH; //ライトの状態

void Tokenize_Control_Message(String mes) {
  int len = mes.length(); //文字列の長さ(Stringはリンクリストなので、lengthがO(N)のため)

  int last = 0,now = 0;//csvを読むやつ
  //Read as csv

  for(auto it = mes.begin();it != mes.end();it++) {
    //swtich文を使いたかったけど、可能な実装方法が汚かったので残念ながらif
    char c = *it;
    if((c == ',' || c == '*' || c == '~') && (1 <= now - last)) { //直前までの文字が数値なので解析するやつ
      int num = mes.substring(last,now).toInt();
      last = now + 1;

      Control(num); //ピンの状態をもとになにかいいことしてくれるはずだと思う。多分。おそらく(予定)。
      Serial.println(String(num) + " to " + (light_state ? "HIGH" : "LOW"));
    }
    if(c == '~') {
      light_state = light_state ? LOW : HIGH;
      last = now + 1;
    }
    
    now++; //index
  }
  light_state = HIGH; //初期化
}


void Control(int x) {
  if(!(0 <= x && x <= 23)) //範囲外だったら
    return;
  
  digitalWrite(19,light_state); //指示しているライトの状態を指定
  digitalWrite(2,HIGH); //Enable
  
  int *ptr = Encode(x); //二進数列に変換
  String tmp = ""; //デバック用メッセージリスト
  for(int i = 0;i < 5;i++) {
    digitalWrite(i + 14,ptr[i]); //Analog pinにbinaryを出力
    //Serial.println(String(ptr[i]));
    tmp += " " + String(ptr[i]);
  }

  //Serial.println(tmp);
  
  free(ptr);
  delay(12); //サブがメッセージを理解する猶予
  digitalWrite(2,LOW);
}



int* Encode(int x) {
  int *result = (int*)calloc(sizeof(int),5);

  for(int i = 0;x != 0;i++) {
    result[i] = x % 2;
    x /= 2;
  }

  return result;
}
