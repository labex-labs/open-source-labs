# ストリーミングデータ用のジェネレータの作成

プログラミングにおいて、ジェネレータは強力なツールです。特に、ストリーミングデータソースの監視などの実世界の問題を扱う際に有用です。このセクションでは、これまで学んだジェネレータの知識を実際のシナリオに適用する方法を学びます。ログファイルを監視し、新しい行が追加されるたびにそれを返すジェネレータを作成します。

## データソースのセットアップ

ジェネレータを作成する前に、データソースをセットアップする必要があります。この場合、株式市場データを生成するシミュレーションプログラムを使用します。

まず、WebIDE で新しいターミナルを開きます。ここでシミュレーションを開始するコマンドを実行します。

ターミナルを開いた後、株式シミュレーションプログラムを実行します。以下のコマンドを入力します。

```bash
cd ~/project
python3 stocksim.py
```

最初のコマンド `cd ~/project` は、カレントディレクトリをホームディレクトリ内の `project` ディレクトリに変更します。2 番目のコマンド `python3 stocksim.py` は、株式シミュレーションプログラムを実行します。このプログラムは株式市場データを生成し、それをカレントディレクトリ内の `stocklog.csv` という名前のファイルに書き込みます。監視コードを作成している間、このプログラムをバックグラウンドで実行しておきます。

## シンプルなファイル監視プログラムの作成

データソースがセットアップされたので、`stocklog.csv` ファイルを監視するプログラムを作成しましょう。このプログラムは、価格が下落した株式を表示します。

1. まず、WebIDE で `follow.py` という新しいファイルを作成します。これを行うには、ターミナルで以下のコマンドを使用して `project` ディレクトリに移動します。

```bash
cd ~/project
```

2. 次に、以下のコードを `follow.py` ファイルに追加します。このコードは `stocklog.csv` ファイルを開き、ファイルポインタをファイルの末尾に移動し、新しい行を継続的にチェックします。新しい行が見つかり、それが価格下落を表す場合、株式名、価格、価格変動を表示します。

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

3. コードを追加した後、ファイルを保存します。次に、ターミナルで以下のコマンドを使用してプログラムを実行します。

```bash
python3 follow.py
```

価格が下落した株式が表示されるはずです。出力は次のようになるかもしれません。

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

プログラムを停止するには、ターミナルで `Ctrl+C` を押します。

## ジェネレータ関数への変換

前のコードは動作しますが、ジェネレータ関数に変換することで、より再利用可能でモジュール性の高いコードにすることができます。ジェネレータ関数は、一時停止と再開が可能で、値を 1 つずつ生成する特殊な関数です。

1. 再度 `follow.py` ファイルを開き、ジェネレータ関数を使用するように修正します。以下は更新後のコードです。

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

`follow` 関数は現在、ジェネレータ関数になっています。この関数はファイルを開き、末尾に移動し、新しい行を継続的にチェックします。新しい行が見つかると、その行を生成します。

2. ファイルを保存し、以下のコマンドを使用して再度実行します。

```bash
python3 follow.py
```

出力は前と同じになるはずです。ただし、現在はファイル監視のロジックが `follow` ジェネレータ関数にきれいにカプセル化されています。これは、ファイルを監視する必要がある他のプログラムでこの関数を再利用できることを意味します。

## ジェネレータの強力さの理解

ファイル読み取りコードをジェネレータ関数に変換することで、コードをはるかに柔軟で再利用可能なものにしました。`follow()` 関数は、株式データだけでなく、ファイルを監視する必要がある任意のプログラムで使用できます。

たとえば、サーバーログ、アプリケーションログ、または時間の経過とともに更新される他の任意のファイルを監視するために使用できます。これは、ジェネレータがストリーミングデータソースをクリーンでモジュール性の高い方法で処理する素晴らしい方法であることを示しています。
