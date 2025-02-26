# ログ記録を行うコード

おそらく、ログ記録が追加された関数を生成する関数を作成できます。ラッパー関数です。

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

次に、それを使用します。

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

`logged` から返される関数を呼び出すと何が起こりますか？

```python
logged_add(3, 4)      # ログメッセージが表示されます
```

この例は、いわゆる _ラッパー関数_ を作成するプロセスを示しています。

ラッパーは、もう少しの処理を追加して別の関数をラップする関数ですが、それ以外は元の関数とまったく同じ方法で機能します。

```python
>>> logged_add(3, 4)
Calling add   # 追加出力。ラッパーによって追加されました
7
>>>
```

_注：`logged()` 関数はラッパーを作成し、それを結果として返します。_
