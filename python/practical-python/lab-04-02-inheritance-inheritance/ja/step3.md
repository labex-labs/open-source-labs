# 例

これがあなたの出発点となるクラスだとしましょう。

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

これを継承を通じて任意の部分を変更することができます。
