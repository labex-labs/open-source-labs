# `__init__` と継承

`__init__` が再定義される場合、親を初期化することが不可欠です。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # `super` と `__init__` への呼び出しを確認
        super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
```

前に示したように、前のバージョンを呼び出す方法である `super` の `__init__()` メソッドを呼び出す必要があります。
