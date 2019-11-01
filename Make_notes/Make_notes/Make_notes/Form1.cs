using NAudio.Wave;
using System;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Drawing;

namespace Make_notes {
    public partial class Form1 : Form {
        public Form1() {
            InitializeComponent();

            bitmap = new Bitmap(this.Width, this.Height);
            g = Graphics.FromImage(bitmap);

            timer.Interval = 200;
            timer.Tick += TickEvent;
        }

        WaveOutEvent device;
        AudioFileReader audio;
        Timer timer = new Timer();
        int[] KeyState = new int[4];
        int[] KeyFlag = new int[4];
        int[] Sum = new int[4];
        List<int[]> Data = new List<int[]>();
        List<int[]> Sums = new List<int[]>();
        Bitmap bitmap;
        Graphics g;
        bool FinishFlag = false;

        private void Button1_Click(object sender, EventArgs e) {
            if (device == null) {
                device = new WaveOutEvent();
                device.PlaybackStopped += OnPlaybackStopped;
            }

            if (audio == null) {
                audio = new AudioFileReader(@"C:\Users\meziro\Quad-Bullet\firefly.mp3");
                device.Init(audio);
            }

            //Limit = (int)(length / timer.Interval * 1000);

            device.Play();
            timer.Enabled = true;
            timer.Start();

            KeyFlag = new int[4] { 0, 0, 0, 0 };
        }


        /* Sounds */


        private void OnPlaybackStopped(object sender, StoppedEventArgs args) {
            device.Dispose();
            device = null;
            audio.Dispose();
            audio = null;

            FinishFlag = true;
        }


        private void TickEvent(object _,EventArgs e) {
            Data.Add(KeyState);
            for (int i = 0; i < 4; i++)
                ;// Console.Write(KeyState[i] + " ");

            Console.WriteLine();

            for (int i = 0; i < 4; i++)
                Sum[i] += KeyState[i];

            for (int i = 0; i < 4; i++)
                Console.Write(Sum[i] + " ");


            Sums.Add(Sum);

            KeyState = new int[4] { 0,0,0,0};

            if(FinishFlag) {
                timer.Stop();

                WriteJson();
            }
        }

        private void WriteJson() {
            String output = "[";
            int l = Data.Count;
            for (int i = 0; i < l; i++) {
                output += "{" + '"' + i + '"' + " : " + $"[{Data[i][0]},{Data[i][1]},{Data[i][2]},{Data[i][3]}]" + '}';
                if (i != l - 1) output += ",";
            }
            output += "]";

            Console.WriteLine(output);
        }

        private void Form1_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e) {
            if (new List<Keys> { Keys.Return, Keys.Space }.Contains(e.KeyCode)) return;

            switch(e.KeyCode) {
                case Keys.A:
                    if (KeyFlag[0] == 0) {
                        KeyState[0] = 1;
                        KeyFlag[0] = 1;
                    }
                    break;
                case Keys.S:
                    if (KeyFlag[1] == 0) {
                        KeyState[1] = 1;
                        KeyFlag[1] = 1;
                    }
                    break;
                case Keys.D:
                    if (KeyFlag[2] == 0) {
                        KeyState[2] = 1;
                        KeyFlag[2] = 1;
                    }
                    break;
                case Keys.F:
                    if (KeyFlag[3] == 0) {
                        KeyState[3] = 1;
                        KeyFlag[3] = 1;
                    }
                    break;
            }
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e) {
            if (new List<Keys> { Keys.Return, Keys.Space }.Contains(e.KeyCode)) return;

            switch (e.KeyCode) {
                case Keys.A:
                    if (KeyState[0] == 1)
                        KeyState[0] = 0;
                    else if (Sum[0] == 1) {
                        KeyState[0] = -1;
                        KeyFlag[0] = 0;
                    }
                    break;
                case Keys.S:
                    if (KeyState[1] == 1)
                        KeyState[1] = 0;
                    else if (Sum[1] == 1) {
                        KeyState[1] = -1;
                        KeyFlag[1] = 0;
                    }
                    break;
                case Keys.D:
                    if (KeyState[2] == 1)
                        KeyState[2] = 0;
                    else if (Sum[2] == 1) {
                        KeyState[2] = -1;
                        KeyFlag[2] = 0;
                    }
                    break;
                case Keys.F:
                    if (KeyState[3] == 1)
                        KeyState[3] = 0;
                    else if (Sum[3] == 1) {
                        KeyState[3] = -1;
                        KeyFlag[3] = 0;
                    }
                    break;
            }
        }


        private void Button1_PreviewKeyDown(object sender, PreviewKeyDownEventArgs e) {
            this.Form1_PreviewKeyDown(sender, e);
        }

        private void Timer1_Tick(object sender, EventArgs e) {
            g.Clear(this.BackColor);

            for(int i = 0;i < 4;i++) {
                if(Sum[i] == 1) {
                    g.FillRectangle(Brushes.Black,i * 50 + 50, 50, 50, 50);
                }
            }

            pictureBox1.Image = bitmap;
        }

        private void Button1_KeyUp(object sender, KeyEventArgs e) {
            this.Form1_KeyUp(sender, e);
        }
    }

    class Note {
        int[] Element = { 0 };
    }
}
