# うちわ
涼しい。

# 必要なもの

// TODO: あとで書く

# 設定

### Bluetoothを扱うために必要なパッケージをインストール

```bash
$ sudo apt-get install bluez bluetooth libbluetooth-dev build-essential
```

### Bluetoothのペアリング

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

### bluebuttonを起動

```bash
$ bluebutton -d="Shutter3" -c ./bluebutton
```