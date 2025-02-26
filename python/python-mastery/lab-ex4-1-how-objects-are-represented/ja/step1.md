# 準備

作成した `Stock` クラスの単純なバージョンに戻り、この実験を始めましょう。対話型プロンプトで、次のような `SimpleStock` という新しいクラスを定義します。

```python
>>> class SimpleStock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares * self.price

>>>
```

このクラスを定義したら、いくつかのインスタンスを作成します。

```python
>>> goog = SimpleStock('GOOG',100,490.10)
>>> ibm  = SimpleStock('IBM',50, 91.23)
>>>
```
