# Типизированные структуры

В файле `structure.py` определите следующую функцию:

```python
# structure.py

...
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
```

Эта функция несколько похожа на функцию `namedtuple()`, так как создает класс. Попробуйте ее:

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

Возможно, вы почувствуете, что голова начинает расщепляться прямо сейчас.
