# クラスメンバー

別の辞書がメソッドを保持します。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

この辞書は `Stock.__dict__` にあります。

```python
{
    'cost': <function>,
   'sell': <function>,
    '__init__': <function>
}
```
