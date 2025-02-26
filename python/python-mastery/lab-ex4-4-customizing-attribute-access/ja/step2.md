# プロキシ

プロキシクラスは、既存のクラスをラップし、似たようなインターフェイスを提供するクラスです。既存のオブジェクトの周りに読み取り専用の層を作る次のクラスを定義します。

```python
>>> class Readonly:
        def __init__(self, obj):
            self.__dict__['_obj'] = obj
        def __setattr__(self, name, value):
            raise AttributeError("Can't set attribute")
        def __getattr__(self, name):
            return getattr(self._obj, name)

>>>
```

このクラスを使用するには、既存のインスタンスの周りに単にラップします。

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> p = Readonly(s)
>>> p.name
'GOOG'
>>> p.shares
100
>>> p.cost
49010.0
>>> p.shares = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: Can't set attribute
>>>
```
