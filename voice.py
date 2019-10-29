import subprocess
import sys
import Quat_Bullet as QB

def main():
    Voice()
#print(score)
#voice="start C:\stn019337\softalk\softalk.exe /R: /W:"+"スコアは"+score+"です"
#subprocess.call(voice,shell=True)
def Voice():
    score = str(QB.Score)
    voice="start C:\stn019337\softalk\softalk.exe /R: /W:"+"スコアは"+score+"です"
    subprocess.call(voice,shell=True)


main()
