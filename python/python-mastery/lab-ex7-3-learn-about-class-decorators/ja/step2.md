# クラスデコレータを使って詳細を埋める

上記のコードの厄介な点は、`_fields` 変数や `Stock.create_init()` の最後のステップのような余分な詳細があることです。この多くの部分を代わりにクラスデコレータにまとめることができます。

`structure.py` ファイルで、クラスデコレータ `@validate_attributes` を作成して、クラスボディを調べてバリデータのインスタンスを探し、`_fields` 変数を埋めます。たとえば：

```python
# structure.py

from validate import Validator

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls
```

このコードは、Python 3.6以降ではクラス辞書が順序付けられているという事実に依存しています。したがって、リストされている順序で異なる `Validator` ディスクリプタに遭遇します。この順序を使って、その後 `_fields` 変数を埋めることができます。これにより、次のようなコードを書くことができます：

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
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

これが機能するようになったら、`@validate_attributes` デコレータを変更して、さらに `Stock.create_init()` を呼び出す最後のステップを実行します。これにより、クラスは次のようになります：

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```
