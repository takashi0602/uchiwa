# Winds Servo 2018 Summer Edition

<img src="./img/logo.png" width="500">

**Winds Servo が切り開く未来
周囲の気温がどのようなものであっても、究極の涼を提供するシステムである Winds Servo がお役に立ちます。
オンプレミスまたはお手元の Uchiwa で Winds Servo のプログラムを実行します。**

<img src="./img/demo.gif" width="350">

短く押すとうちわが扇ぎ, 長く押すとうちわの方向転換を行います.

## 必要なもの

SSH接続が可能なRaspberry Pi

<img src="./img/raspberrypi.jpg" width="350">

ダイソーで300円で購入したBluetoothリモートシャッター

<img src="./img/bluetooth_remote_shutter.jpg" width="350">

サーボモーター２つ

<img src="./img/servo.jpg" width="350">

柄の部分を切断したうちわ

<img src="./img/uchiwa.jpg" width="350">

サーボ用カメラマウント

[これ](https://www.amazon.co.jp/gp/product/B07B2W39WJ/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1)

ジャンパー線(オス - メス型)

<img src="./img/jumper_code.jpg" width="350">

## ファイル構成

|ファイル名|説明|
|:--|:--|
|bluebutton|bluebuttonの設定ファイル|
|direction.example|うちわの方向転換用サーボの動作角度記録用ファイル|
|uchiwa_angle.py|うちわの首振り用サーボの制御コード|
|uchiwa_direction.py|うちわの方向転換用サーボの制御コード|

## ハードウェア側の設定

### サーボと土台の接合

木材にネジでえいってやる.

<img src="./img/base_and_servo.jpg" width="350">

### サーボとサーボの接合

サーボ用カメラマウントでいい感じにやる.

<img src="./img/servo_and_servo.jpg" width="350">

### サーボとうちわの接合

針金で適当にぐるぐるにする.

<img src="./img/servo_and_uchiwa.jpg" width="350">

### GPIOの設定

うちわ動作用のサーボ: GPIO18
うちわの方向転換用のサーボ: GPIO17

DC Power 5VとGroundは適当に.

## ソフトウェア側の設定

### SSH接続

```bash
$ ssh pi@raspberrypi.local
pi@raspberrypi.local's password:
...
pi@raspberrypi:~ $
```

### Bluetoothを扱うために必要なパッケージをインストール(初回のみ)

```bash
$ sudo apt-get install bluez bluetooth libbluetooth-dev build-essential
```

### ボタン操作の検知に必要なパッケージをインストール(初回のみ)

```bash
$ sudo apt-get install ruby
$ sudo gem install bluebutton
```

### リポジトリのクローン(初回のみ)

```
$ git clone https://github.com/tyokinuhata/uchiwa.git
$ cd uchiwa
```

### サーボの設定(初回のみ)

```bash
$ cp ./src/direction.example ./src/direction
```

### Bluetoothのペアリング

Bluetoothリモートシャッターの電源を入れ, コンソールで以下のコマンドを叩く.

```bash
$ bluetoothctl
[bluetooth]# power on                  // bluetoothctlを起動
[bluetooth]# scan on                   // スキャンを開始
...
Device FF:FF:XX:XX:XX:XX AB Shutter3
...
[bluetooth]# info FF:FF:XX:XX:XX:XX    // Shutter3の情報を表示
[bluetooth]# pair FF:FF:XX:XX:XX:XX    // Shutter3とペアリング
```

### bluebuttonの実行

```bash
$ bluebutton -d="Shutter3" -c ./bluebutton
```

bluebuttonの実行後, Bluetoothリモートシャッターのボタンを押すと設定ファイルの対応した処理が走る.
