# 辞書とオブジェクト

ユーザ定義オブジェクトも、インスタンスデータとクラスの両方に辞書を使用します。実際、オブジェクトシステム全体は、主に辞書の上に置かれる追加の層に過ぎません。

辞書はインスタンスデータである `__dict__` を保持します。

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG','shares' : 100, 'price': 490.1 }
```

この辞書（およびインスタンス）は、`self` に代入することで埋めます。

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

インスタンスデータである `self.__dict__` は、次のようになります。

```python
{
    'name': 'GOOG',
   'shares': 100,
    'price': 490.1
}
```

**各インスタンスは独自のプライベート辞書を持ちます。**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

あるクラスのインスタンスを100個作成した場合、データを保持する辞書が100個あります。
