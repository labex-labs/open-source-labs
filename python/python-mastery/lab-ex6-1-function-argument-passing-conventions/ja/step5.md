# 最初からやり直す

新しいファイル `stock.py` を作成します（または以前のコードをすべて削除します）。次のように `Stock` を定義することから始めます。

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

これを行ったら、`teststock.py` のユニットテストを実行します。多くのテストが失敗するはずですが、少なくともいくつかのテストは合格するはずです。
