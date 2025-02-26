# 代替コンストラクタ

おそらく、生データの行から`Stock`を作成することは、代替コンストラクタによってより適切に処理されます。`Stock`クラスを次のように変更して、`types`クラス変数と`from_row()`クラスメソッドを持たせましょう。

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
  ...
```

これをテストする方法は次の通りです。

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

行内の文字列値が適切な型に変換された方法に注意深く注目してください。
