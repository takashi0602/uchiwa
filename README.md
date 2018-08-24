# Winds Servo 2018 Summer Edition
[Bluetoothボタン] => [ラズパイ] => [サーボモータ] => [うちわ] => [風&#x1f300;] => 涼しい！

// TODO: gif

## 必要なもの

ダイソーで300円で購入したBluetoothリモートシャッター

<img src="./img/bluetooth_remote_shutter.jpg" width="350">

SSH接続が可能なRaspberry Pi

<img src="./img/raspberrypi.jpg" width="350">

サーボモーター２つ

<img src="./img/servo.jpg" width="350">

// TODO: うちわ

## ディレクトリ構成

|ファイル/ディレクトリ名|説明|
|:--|:--|
|bluebutton|bluebuttonの設定ファイル|
|direction.example|うちわの方向転換用サーボの動作角度記録用ファイル|
|uchiwa_angle.py|うちわの首振り用サーボの制御コード|
|uchiwa_direction.py|うちわの方向転換用サーボの制御コード|

## 設定

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
$ mv direction.example direction
```

### Bluetoothのペアリング(毎回)

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

### bluebuttonの実行(毎回)

```bash
$ bluebutton -d="Shutter3" -c ./bluebutton
```

bluebuttonの実行後, Bluetoothリモートシャッターのボタンを押すと設定ファイルの対応した処理が走る.
