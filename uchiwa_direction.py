# うちわの向きを変える

import RPi.GPIO as GPIO
import time

# GPIOのモード設定
GPIO.setmode(GPIO.BCM)

# GPIO17を制御パルスの出力に設定
gp_out = 17
GPIO.setup(gp_out, GPIO.OUT)

# サーボの制御パルスと周波数の設定
servo = GPIO.PWM(gp_out, 50)

# パルス出力の開始
servo.start(0)

# ファイル読み込み
fr = open('direction', 'r')

# 現在の角度を取得
direction = 0
for row in fr:
    direction = int(row.strip())
fr.close()

# サーボを動作させる
servo.ChangeDutyCycle(direction)
time.sleep(0.5)

# ファイル書き込み
if direction >= 12:
    direction = 2

fw = open('direction', 'w')
fw.write(str(direction + 1))
fw.close()

# 後処理
servo.stop()
GPIO.cleanup()
