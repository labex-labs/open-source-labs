# 単純な属性

次のクラスを考えてみましょう。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

驚くべきことに、属性を全く任意の値に設定できます。

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

これを見ると、追加のチェックが必要だと思うかもしれません。

```python
s.shares = '50'     # TypeError が発生します、これは文字列です
```

どのようにすればよいでしょうか。
