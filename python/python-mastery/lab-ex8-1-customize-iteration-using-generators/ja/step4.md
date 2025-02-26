# ストリーミングデータソースの監視

ジェネレータは、データのストリームを生成するだけの便利な方法でもあります。このパートでは、ログファイルを監視するジェネレータを書くことで、この考え方を探求します。まず、次の指示に注意深く従ってください。

`stocksim.py` というプログラムは、株式市場データをシミュレートするプログラムです。出力として、このプログラムは常にリアルタイムデータを `stocklog.csv` というファイルに書き込みます。コマンドウィンドウ（IDLEではない）で、`stocksim.py` があるディレクトリに移動して、このプログラムを実行します：

    % python3 stocksim.py

Windowsの場合は、`stocksim.py` プログラムを見つけて、ダブルクリックして実行します。これ以上はこのプログラムについて考えないでください（ただ実行させておきます）。もう一度、このプログラムをバックグラウンドで実行させておいてください。数時間実行されます（心配する必要はありません）。

上記のプログラムが実行されているところで、ファイルを開き、末尾に移動して、新しい出力を監視するための小さなプログラムを書きましょう。`follow.py` というファイルを作成し、次のコードを入力します：

```python
# follow.py
import os
import time
f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

このプログラムを実行すると、リアルタイムの株価情報が表示されます。このコードは、Unixの `tail -f` コマンドに似ており、ログファイルを監視するために使用されます。

**注**：この例では、`readline()` メソッドの使用方法が少々異常です。通常、ファイルから行を読む際には `for` ループを使うことが多いですが、この場合は、ファイルの末尾を繰り返し調べて、新しいデータが追加されたかどうかを確認するために使用しています（`readline()` は新しいデータを返すか、空の文字列を返します）。

コードをよく見ると、コードの最初の部分がデータの行を生成している一方で、`while` ループの末尾の文がデータを消費しています。ジェネレータ関数の主な特徴は、すべてのデータ生成コードを再利用可能な関数に移動できることです。

コードを変更して、ファイル読み取りをジェネレータ関数 `follow(filename)` で行うようにしましょう。次のコードが動作するようにします：

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Should see lines of output produced here...
```

株価情報のコードを変更して、次のようになるようにしましょう：

```python
for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

**考察**

ここで非常に強力なことが起こりました。興味深い反復処理パターン（ファイルの末尾で行を読む）を独自の小さな関数に移動しました。`follow()` 関数は、これで完全に汎用的なユーティリティになり、任意のプログラムで使用できるようになりました。たとえば、サーバーログ、デバッグログ、その他の類似したデータソースを監視するために使用できます。これはかなり面白いです。
