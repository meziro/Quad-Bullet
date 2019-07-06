#include<string>
#include<stdio.h>
#include<windows.h>
#include<tchar.h>

HANDLE hComPort;

int main(void) {
  hComPort = CreateFile(
    _T("COM3"),
    GENERIC_WRITE,
    0,
    NULL,
    OPEN_EXISTING,
    FILE_FLAG_OVERLAPPED,
    NULL);

  if(hComPort == INVALID_HANDLE_VALUE) {
    printf("Error Occured");
    CloseHandle(hComPort);
    return 0;
  } else {
    printf("Seccuss");
  }

  int check = SetupComm(
    hComPort,
    1024,
    1024
  );

  if(check == FALSE) {
    printf("Error eccured in setup");
    CloseHandle(hComPort);
    return 0;
  } else {
    printf("Seccuss");
  }

  check = PurgeComm(
       hComPort,//COMポートのハンドラ
       PURGE_TXABORT | PURGE_RXABORT | PURGE_TXCLEAR | PURGE_RXCLEAR//出入力バッファをすべてクリア
  );
  
  if (check == FALSE){
    printf("送受信バッファの初期化ができません.\r\n");
    (hComPort);
    return 0;
  } else {
    printf("送受信バッファの初期化が完了しました.\r\n");
  }

  DCB dcb;//構成情報を記録する構造体の生成
  GetCommState(hComPort, &dcb);//現在の設定値を読み込み
  dcb.DCBlength = sizeof(DCB);//DCBのサイズ
  dcb.BaudRate = 9600;//ボーレート:9600bps
  dcb.ByteSize = 8;//データサイズ:8bit
  dcb.fBinary = TRUE;//バイナリモード:通常TRUE
  dcb.fParity = NOPARITY;//パリティビット:パリティビットなし
  dcb.StopBits = ONESTOPBIT;//ストップビット:1bit
  dcb.fOutxCtsFlow = FALSE;//CTSフロー制御:フロー制御なし
  dcb.fOutxDsrFlow = FALSE;//DSRハードウェアフロー制御：使用しない
  dcb.fDtrControl = DTR_CONTROL_DISABLE;//DTR有効/無効:DTR無効
  dcb.fRtsControl = RTS_CONTROL_DISABLE;//RTSフロー制御:RTS制御なし

  dcb.fOutX = FALSE;//送信時XON/XOFF制御の有無:なし
  dcb.fInX = FALSE;//受信時XON/XOFF制御の有無:なし
  dcb.fTXContinueOnXoff = TRUE;// 受信バッファー満杯＆XOFF受信後の継続送信可否:送信可
  dcb.XonLim = 512;//XONが送られるまでに格納できる最小バイト数:512
  dcb.XoffLim = 512;//XOFFが送られるまでに格納できる最小バイト数:512
  dcb.XonChar = 0x11;//送信時XON文字 ( 送信可：ビジィ解除 ) の指定:XON文字として11H ( デバイス制御１：DC1 )
  dcb.XoffChar = 0x13;//XOFF文字（送信不可：ビジー通告）の指定:XOFF文字として13H ( デバイス制御3：DC3 )

  dcb.fNull = TRUE;// NULLバイトの破棄:破棄する
  dcb.fAbortOnError = TRUE;//エラー時の読み書き操作終了:終了する
  dcb.fErrorChar = FALSE;// パリティエラー発生時のキャラクタ（ErrorChar）置換:なし
  dcb.ErrorChar = 0x00;// パリティエラー発生時の置換キャラクタ
  dcb.EofChar = 0x03;// データ終了通知キャラクタ:一般に0x03(ETX)がよく使われます。
  dcb.EvtChar = 0x02;// イベント通知キャラクタ:一般に0x02(STX)がよく使われます

  check = SetCommState(hComPort, &dcb);  //設定値の書き込み
  if (check == FALSE){//エラーチェック
      printf("COMポート構成情報の変更に失敗しました.\r\n");
      CloseHandle(hComPort);
      return 0;
  }
  else{
        printf("COMポート構成情報を変更しました.\r\n");
  }

  COMMTIMEOUTS TimeOut; // COMMTIMEOUTS構造体の変数を宣言
  GetCommTimeouts(hComPort, &TimeOut); // タイムアウトの設定状態を取得

  TimeOut.ReadTotalTimeoutMultiplier = 0;//読込の１文字あたりの時間:タイムアウトなし
  TimeOut.ReadTotalTimeoutConstant = 1000;//読込エラー検出用のタイムアウト時間
  //(受信トータルタイムアウト) = ReadTotalTimeoutMultiplier × (受信予定バイト数) + ReadTotalTimeoutConstant 
  TimeOut.WriteTotalTimeoutMultiplier = 0;//書き込み１文字あたりの待ち時間:タイムアウトなし
  TimeOut.WriteTotalTimeoutConstant = 1000;//書き込みエラー検出用のタイムアウト時間
  //(送信トータルタイムアウト) = WriteTotalTimeoutMultiplier ×(送信予定バイト数) + WriteTotalTimeoutConstant

  check = SetCommTimeouts(hComPort, &TimeOut);//タイムアウト設定の書き換え
  if (check == FALSE){//エラーチェック
      printf("タイムアウトの設定に失敗しました.\r\n");
      CloseHandle(hComPort);
      return 0;
  }
  else{
        printf("タイムアウトの設定に成功しました.\r\n");
  }
  
  char SendData[] = "1,";//送信データの用意
  int SendSize = strlen(SendData)+1;//送信データサイズを取得
  DWORD writeSize;//実際に送信したデータサイズ
  WriteFile(hComPort,SendData,SendSize,&writeSize,NULL);


}
