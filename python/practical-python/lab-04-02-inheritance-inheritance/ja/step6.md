# オーバーライド

時には、クラスが既存のメソッドを拡張しますが、再定義の中で元の実装を使用したい場合があります。このために、`super()` を使用します。

```python
class Stock:
  ...
    def cost(self):
        return self.shares * self.price
  ...

class MyStock(Stock):
    def cost(self):
        # `super` への呼び出しを確認
        actual_cost = super().cost()
        return 1.25 * actual_cost
```

前のバージョンを呼び出すには `super()` を使用します。

_注意：Python 2 では、構文がもっと冗長でした。_

```python
actual_cost = super(MyStock, self).cost()
```
