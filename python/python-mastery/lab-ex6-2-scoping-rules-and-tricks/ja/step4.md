# まとめる

最初の2つの部分のアイデアを取り入れて、元々 `Structure` クラスの一部であった `__init__()` メソッドを削除します。次に、次のような `_init()` メソッドを追加します。

```python
# structure.py
import sys

class Structure:
  ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
  ...
```

注：これが `@staticmethod` として定義されている理由は、`self` 引数が局所変数から取得されるため、メソッド自体に引数として追加で渡す必要がないからです（確かにこれは少し微妙です）。

次に、`Stock` クラスを以下のように変更します。

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares','price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

クラスが正常に機能し、キーワード引数をサポートし、適切なヘルプシグネチャを持っていることを確認します。

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... 出力を見る...
>>>
```

`teststock.py` の単体テストを再度実行します。少なくとも1つ以上のテストが合格するはずです。やった！

この時点では、まるで大きく後退したように見えるかもしれません。クラスには `__init__()` メソッドが必要なだけでなく、他の一部のメソッド（`__repr__()` と `__setattr__()`）が機能するために `_fields` 変数も必要です。さらに、`self._init()` の使用はかなり不自然に見えます。これについては改善しますが、しばらくお待ちください。
