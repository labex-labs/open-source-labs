# 単純化されたデータ構造

以前の演習では、次のように株を表すクラスを定義しました。

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

`__init__()` メソッドに注目してください。構造を埋めるたびに、これだけのコードを入力するのは面倒ではありませんか？ プログラムで数十個のそのような構造を定義しなければならない場合どうでしょう？

`structure.py` というファイルに、ユーザーが次のように単純なデータ構造を定義できる基底クラス `Structure` を定義します。

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year','month', 'day')
```

`Structure` クラスは、任意の数の引数を取り、`_fields` クラス変数の存在を探す `__init__()` メソッドを定義する必要があります。このメソッドは、`_fields` の属性名と `__init__()` に渡された値からインスタンスを埋めます。

実装をテストするためのサンプルコードは次のとおりです。

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
