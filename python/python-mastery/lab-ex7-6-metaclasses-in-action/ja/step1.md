# 最後のフロンティア

演習7.3では、次のように型チェックされた構造を定義できるようにしました。

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

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

内部ではたくさんのことが起こっています。ただし、1つの面倒なことは、上部のすべての型名のインポート（たとえば、`String`、`PositiveInteger`など）です。それはちょうど`from validate import *`文につながるようなものです。メタクラスに関する興味深いことは、クラスが定義されるプロセスを制御するために使用できるということです。これには、クラス定義自体の環境を管理することも含まれます。では、それらのインポートに取り組みましょう。

すべての検証子名を管理する最初のステップは、それらを収集することです。`validate.py`ファイルに移動して、再び`__init_subclass__()`を含むこの追加のコードで`Validator`ベースクラスを変更します。

```python
# validate.py

class Validator:
  ...

    # すべての派生クラスを辞書に収集する
    validators = { }
    @classmethod
    def __init_subclass__(cls):
        cls.validators[cls.__name__] = cls
```

それほど多くはありませんが、`Validator`サブクラスのすべての小さな名前空間を作成しています。見てみましょう。

```python
>>> from validate import Validator
>>> Validator.validators
{'Float': <class 'validate.Float'>,
 'Integer': <class 'validate.Integer'>,
 'NonEmpty': <class 'validate.NonEmpty'>,
 'NonEmptyString': <class 'validate.NonEmptyString'>,
 'Positive': <class 'validate.Positive'>,
 'PositiveFloat': <class 'validate.PositiveFloat'>,
 'PositiveInteger': <class 'validate.PositiveInteger'>,
 'String': <class 'validate.String'>,
 'Typed': <class 'validate.Typed'>}
>>>
```

これを行ったので、この名前空間を`Structure`から定義されるクラスの名前空間に注入しましょう。次のメタクラスを定義します。

```python
# structure.py
...

from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
  ...
```

このコードでは、`__prepare__()`メソッドは、空の辞書とすべての定義済み検証子の辞書で構成される特殊な`ChainMap`マッピングを作成しています。最初にリストされている空の辞書は、クラスボディ内で行われるすべての定義を収集します。`Validator.validators`辞書は、型定義のすべてを記述子または引数型アノテーションとして使用できるようにします。

`__new__()`メソッドは、余分な検証子辞書を破棄し、残りの定義を型コンストラクタに渡します。賢いですが、面倒なインポートを省くことができます。

```python
# stock.py

from structure import Structure

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
