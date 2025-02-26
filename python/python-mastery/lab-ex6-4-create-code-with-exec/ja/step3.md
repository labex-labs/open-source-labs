# 名前付きタプル

演習2.1では、`collections` モジュールの `namedtuple` オブジェクトを使って実験しました。思い出してもらうために、それらの使い方を以下に示します：

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name','shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

内部的には、`namedtuple()` 関数は文字列を使ってコードを作成し、`exec()` を使って実行しています。コードを見て驚いてください：

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... 出力を見てください...
>>>
```
