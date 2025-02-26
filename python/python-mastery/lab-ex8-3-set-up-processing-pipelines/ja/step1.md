# コルーチンの例

コルーチンを始めることは少し厄介かもしれません。ここには、演習8.2と同じタスクをコルーチンを使って行うサンプルプログラムがあります。このプログラムをコピーして、`cofollow.py` という名前のファイルに保存してください。

```python
# cofollow.py
import os
import time

# データソース
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line!= '':
                target.send(line)
            else:
                time.sleep(0.1)

# コルーチン関数用のデコレータ
from functools import wraps

def consumer(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        f.send(None)
        return f
    return start

# サンプルコルーチン
@consumer
def printer():
    while True:
        item = yield     # 私に送られたアイテムを受け取る
        print(item)

# 例の使用方法
if __name__ == '__main__':
    follow('stocklog.csv',printer())
```

このプログラムを実行して、出力が得られることを確認してください。異なる部分がどのように結び付いているか理解してください。
