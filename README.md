# うちわ
[Bluetoothボタン] => [ラズパイ] => [サーボモータ] => [うちわ] => [風&#x1f300;] => 涼しい！

// TODO: gif

## 必要なもの

ダイソーで300円で購入したBluetoothリモートシャッター

<img src="./img/bluetooth_remote_shutter.jpg" width="350">

Raspberry Pi 3にRaspbianを書き込み済みのmicroSD, 電源, マウス, キーボード, ディスプレイ, LANケーブル等を繋げたもの

<img src="./img/raspberrypi.jpg" width="350">

// TODO: サーボモータ, うちわ

## 設定

### Bluetoothを扱うために必要なパッケージをインストール

```bash
$ sudo apt-get install bluez bluetooth libbluetooth-dev build-essential
```

### ボタン操作の検知に必要なパッケージをインストール

```bash
$ sudo apt-get install ruby
$ sudo gem install bluebutton
```

### bluebuttonの設定

```bash
$ vim bluebutton
```

`keyup`, `keydown`, `longup`, `longdown`に対してそれぞれそれぞれ動作を決めることができる.

```
keyup=echo KEY UP!
keydown=echo KEY DOWN!
longup=echo LONG UP!
longdown=echo LONG DOWN!
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
