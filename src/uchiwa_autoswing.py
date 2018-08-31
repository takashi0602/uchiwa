# うちわ動かすやつ
import RPi.GPIO as GPIO
import time
# Http レスポンス送るやつ
import requests
# 温度取るやつ
import smbus
import time

# 温度用の定数
i2c = smbus.SMBus(1)
address = 0x5c

def get_discomfort():
    global i2c
    global address
    # センサsleep解除
    try:
        i2c.write_i2c_block_data(address,0x00,[])
    except:
        pass
    # 読み取り命令
    time.sleep(0.003)
    i2c.write_i2c_block_data(address,0x03,[0x00,0x04])

    # データ受取
    time.sleep(0.015)
    block = i2c.read_i2c_block_data(address,0,6)
    shitudo = float(block[2] << 8 | block[3])/10
    ondo = float(block[4] << 8 | block[5])/10

    # 不快指数を算出
    discomfort = (0.81 * ondo) + (0.01 * shitudo) * (0.99 * ondo - 14.3 ) + 46.3
    print(shitudo) # 湿度表示
    print(ondo) # 温度表示
    print(discomfort)

    return {"discomfort": discomfort, "shitudo": shitudo, "ondo": ondo}

def move_servo(servo):

    # サーボを動作させる
    servo.ChangeDutyCycle(13)
    time.sleep(0.5)
    servo.ChangeDutyCycle(6)
    time.sleep(1)

# メイン関数
def main():
    # GPIOのモード設定
    GPIO.setmode(GPIO.BCM)

    # GPIO18を制御パルスの出力に設定
    gp_out = 18
    GPIO.setup(gp_out, GPIO.OUT)

    # サーボの制御パルスと周波数の設定
    servo = GPIO.PWM(gp_out, 50)
    servo.start(0)

    # 以下、無限ループ
    try:
        while True:
            discomfort = get_discomfort()
            if discomfort["discomfort"] > 70:
                requests.post('https://hooks.slack.com/services/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',
                    json = {
                        "text":
                        "*アツイアツーーーーーーイｗｗｗｗｗｗｗ*\n\n" +
                        "温度: " + str(discomfort['ondo']) + "\n" +
                        "湿度: " + str(discomfort['shitudo'])
                    }
                )
                move_servo(servo)

            time.sleep(4)
    except KeyboardInterrupt:
        servo.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
