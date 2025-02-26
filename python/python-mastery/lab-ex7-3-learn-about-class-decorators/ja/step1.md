# ディスクリプタの再検討

演習4.3では、ユーザーが次のように型チェック付きの属性を持つクラスを定義できるようにいくつかのディスクリプタを定義しました。

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
 ...
```

`Stock` クラスを変更して、上記のディスクリプタを含め、次のようになるようにします（演習6.4を参照）。

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name','shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

`teststock.py` のユニットテストを実行します。型チェックを追加することで、多数のテストが通過するはずです。素晴らしいです。
