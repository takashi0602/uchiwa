# うちわの向きを変える

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# GPIO4を制御パルスの出力に設定
gp_out = 17
GPIO.setup(gp_out, GPIO.OUT)

# 「GPIO4出力」でPWMインスタンスを作成する。
# GPIO.PWM( [ピン番号] , [周波数Hz] )
# SG92RはPWMサイクル:20ms(=50Hz), 制御パルス:0.5ms〜2.4ms, (=2.5%〜12%)。
servo = GPIO.PWM(gp_out, 50)

# パルス出力開始。　servo.start( [デューティサイクル 0~100%] )
# とりあえずゼロ指定だとサイクルが生まれないので特に動かないっぽい？
servo.start(0)

# ファイル読み込み
fr = open('direction', 'r')

# 現在の角度を取得
direction = 0
for row in fr:
    direction = int(row.strip())
fr.close()

# デューティサイクルの値を変更することでサーボが回って角度が変わる。
servo.ChangeDutyCycle(direction)
time.sleep(0.5)

# ファイル書き込み
if direction >= 12:
    direction = 2

fw = open('direction', 'w')
fw.write(str(direction + 1))
fw.close()

servo.stop()
GPIO.cleanup()
