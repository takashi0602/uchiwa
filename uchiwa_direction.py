# うちわの向きを変える

import RPi.GPIO as GPIO
import time

def main():
    # GPIOのモード設定
    GPIO.setmode(GPIO.BCM)

    # GPIO17を制御パルスの出力に設定
    gp_out = 17
    GPIO.setup(gp_out, GPIO.OUT)

    # サーボの制御パルスと周波数の設定
    servo = GPIO.PWM(gp_out, 50)

    # パルス出力の開始
    servo.start(0)

    # 現在の角度を取得
    direction = read_direction()

    # サーボを動作させる
    servo.ChangeDutyCycle(direction)
    time.sleep(0.5)

    # 角度を書き込み
    if direction >= 12:
        direction = 1
    write_direction(direction)

    # 後処理
    servo.stop()
    GPIO.cleanup()

def read_direction():
    fr = open('direction', 'r')
    direction = 0
    for row in fr:
        direction = int(row.strip())
    fr.close()
    return direction

def write_direction(direction):
    fw = open('direction', 'w')
    fw.write(str(direction + 1))
    fw.close()

if __name__ == '__main__':
    main()