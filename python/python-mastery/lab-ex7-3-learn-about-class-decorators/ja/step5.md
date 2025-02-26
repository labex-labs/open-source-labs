# メソッド引数のチェック

前のパートで書いた `@validated` デコレータを覚えていますか？`@validate_attributes` デコレータを変更して、クラス内の注釈付きの任意のメソッドを自動的に `@validated` でラップするようにしましょう。これにより、`sell()` メソッドなどのメソッドに強制的な注釈を付けることができます。

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

`sell()` が引数を強制することがわかります。

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.sell(-25)
Traceback (most recent call last):
...
TypeError: Bad Arguments
  nshares: must be >= 0
>>>
```

はい、これは今や非常に面白くなってきました。クラスデコレータと継承の組み合わせは強力な力です。
