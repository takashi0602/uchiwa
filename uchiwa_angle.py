# うちわを動かす

import RPi.GPIO as GPIO
import time

def main():
    # GPIOのモード設定
    GPIO.setmode(GPIO.BCM)

    # GPIO18を制御パルスの出力に設定
    gp_out = 18
    GPIO.setup(gp_out, GPIO.OUT)

    # サーボの制御パルスと周波数の設定
    servo = GPIO.PWM(gp_out, 50)

    # パルス出力の開始
    servo.start(0)

    # サーボを動作させる
    servo.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo.ChangeDutyCycle(7)
    time.sleep(0.5)

    # 後処理
    servo.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()