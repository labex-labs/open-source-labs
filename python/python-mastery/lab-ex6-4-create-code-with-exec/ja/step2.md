# **init**() 関数の作成

演習6.3では、`__init__()` メソッドのシグネチャを調べて、`_fields` クラス変数に属性名を設定するコードを書きました。たとえば：

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

`__init__()` メソッドを調べる代わりに、`_fields` の値から `__init__()` メソッドを作成するクラスメソッド `create_init(cls)` を書きましょう。上記のように `exec()` 関数を使ってこれを行います。ユーザーがそれを使う方法は次のとおりです：

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')

Stock.create_init()
```

結果のクラスは、以前とまったく同じように機能する必要があります：

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

途中の `Stock` クラスを変更して、示されているように `create_init()` 関数を使用します。以前と同じようにユニットテストで検証します。

その際、`Structure` クラスの `_init()` メソッドと `set_fields()` メソッドを削除しましょう。そのアプローチは少し奇妙でした。
