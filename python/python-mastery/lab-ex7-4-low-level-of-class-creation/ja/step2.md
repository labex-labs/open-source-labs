# 型付き構造体

`structure.py` ファイルに、次の関数を定義します。

```python
# structure.py

...
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
```

この関数は、クラスを作成するという点で `namedtuple()` 関数に似ています。試してみましょう。

```python
>>> from validate import String, PositiveInteger, PositiveFloat
>>> from structure import typed_structure
>>> Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

この時点で、あなたの頭のひげが離れ始めているかもしれません。
