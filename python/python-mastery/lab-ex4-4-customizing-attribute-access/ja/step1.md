# **slots** と setattr の比較

以前の演習では、`__slots__` を使用してクラスのインスタンス属性をリストしました。`__slots__` の主な目的は、メモリの使用を最適化することです。副次的な効果として、許可される属性をリストされたものに厳密に制限します。`__slots__` の欠点は、Python の他の部分と奇妙に相互作用することが多いことです (たとえば、`__slots__` を使用するクラスは多重継承とともに使用できません)。そのため、特殊なケースを除いて `__slots__` を使用するべきではありません。

もし本当に許可される属性のセットを制限したい場合は、`__setattr__()` メソッドを定義するという代替方法があります。この実験を試してみてください。

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def __setattr__(self, name, value):
            if name not in { 'name','shares', 'price' }:
                raise AttributeError('No attribute %s' % name)
            super().__setattr__(name, value)

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares = 75
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: No attribute share
>>>
```

この例では、`__slots__` はありませんが、`__setattr__()` メソッドが依然として属性を事前定義されたセット内のものに制限しています。このアプローチが継承とどのように相互作用するか (たとえば、サブクラスが新しい属性を追加したい場合、それを機能させるために `__setattr__()` を再定義する必要があるかもしれません) を考える必要があります。
