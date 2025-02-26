# 最初のデコレータ

デコレータを始めるには、関数が呼び出されるたびに単にメッセージを出力するという、とても簡単なデコレータ関数を書きます。`logcall.py` というファイルを作成し、次の関数を定義します。

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

次に、別のファイル `sample.py` を作成し、いくつかの関数定義に適用します。

```python
# sample.py

from logcall import logged

@logged
def add(x,y):
    return x+y

@logged
def sub(x,y):
    return x-y
```

コードを次のようにテストします。

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3,4)
Calling add
7
>>> sample.sub(2,3)
Calling sub
-1
>>>
```
