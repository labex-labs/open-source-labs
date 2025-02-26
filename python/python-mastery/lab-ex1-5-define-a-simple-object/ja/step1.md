# 簡単なオブジェクトの定義

`stock.py` というファイルを作成し、次のクラスを定義します。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
```

これを行ったら、プログラムを実行して新しい `Stock` オブジェクトを試してみましょう。

注: これを行うには、`-i` オプションを使用して Python を実行する必要がある場合があります。たとえば:

```bash
python3 -i stock.py
```

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>> print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
      GOOG        100     490.10
>>> t = Stock('IBM', 50, 91.5)
>>> t.cost()
4575.0
>>>
```
