# ファイルフォロワーを使ったコルーチンの理解

まずは、コルーチンとは何か、そして Python でどのように動作するかを理解しましょう。コルーチンはジェネレータ関数の特殊なバージョンです。Python では、関数は通常、呼び出されるたびに最初から実行されます。しかし、コルーチンは異なります。コルーチンはデータを消費することも生成することもでき、実行を一時停止して再開する機能を持っています。つまり、コルーチンはある時点で操作を一時停止し、後で中断したところから再開することができます。

## 基本的なコルーチンファイルフォロワーの作成

このステップでは、コルーチンを使用してファイルの新しい内容を監視し、それを処理するファイルフォロワーを作成します。これは Unix の`tail -f`コマンドに似ており、ファイルの末尾を継続的に表示し、新しい行が追加されると更新されます。

1. コードエディタを開き、`/home/labex/project`ディレクトリに`cofollow.py`という名前の新しいファイルを作成します。ここで、コルーチンを使用したファイルフォロワーを実装する Python コードを記述します。

2. 以下のコードをファイルにコピーします。

```python
# cofollow.py
import os
import time

# Data source
def follow(filename, target):
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = f.readline()
            if line != '':
                target.send(line)  # Send the line to the target coroutine
            else:
                time.sleep(0.1)  # Sleep briefly if no new content

# Decorator for coroutine functions
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args, **kwargs):
        f = func(*args, **kwargs)
        f.send(None)  # Prime the coroutine (necessary first step)
        return f
    return start

# Sample coroutine
@consumer
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('stocklog.csv', printer())
```

3. このコードの主要なコンポーネントを理解しましょう。

   - `follow(filename, target)`: この関数はファイルを開く役割を担っています。まず、`f.seek(0, os.SEEK_END)`を使用してファイルポインタをファイルの末尾に移動させます。その後、無限ループに入り、ファイルから新しい行を継続的に読み取ろうとします。新しい行が見つかった場合、`send`メソッドを使用してその行をターゲットのコルーチンに送信します。新しい内容がない場合は、`time.sleep(0.1)`を使用して短時間（0.1 秒）一時停止してから再度チェックします。
   - `@consumer`デコレータ：Python では、コルーチンはデータを受け取り始める前に「初期化」する必要があります。このデコレータはその役割を担っています。自動的にコルーチンに初期の`None`値を送信します。これは、コルーチンが実際のデータを受け取る準備をするために必要な最初のステップです。
   - `printer()`コルーチン：これは単純なコルーチンです。無限ループを持ち、`yield`キーワードを使用して送信されたアイテムを受け取ります。アイテムを受け取ると、単にそれを印刷します。

4. ファイルを保存し、ターミナルから実行します。

```bash
cd /home/labex/project
python3 cofollow.py
```

5. スクリプトが株式ログファイルの内容を印刷し、ファイルに新しい行が追加されるとそれを継続的に印刷するのが見えるはずです。`Ctrl+C`を押してプログラムを停止します。

ここでの重要な概念は、データが`follow`関数から`send`メソッドを通じて`printer`コルーチンに流れるということです。このデータの「押し出し」は、イテレーションを通じてデータを「引き出す」ジェネレータとは逆です。ジェネレータでは、通常、生成する値を反復処理するために`for`ループを使用します。しかし、このコルーチンの例では、データはコードの一部から別の部分に能動的に送信されます。
