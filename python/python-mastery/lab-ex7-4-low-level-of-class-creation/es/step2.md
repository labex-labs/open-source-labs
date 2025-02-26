# Estructuras tipadas

En el archivo `structure.py`, defina la siguiente función:

```python
# structure.py

...
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
```

Esta función es en cierto modo similar a la función `namedtuple()` en que crea una clase. Pruebe la siguiente forma:

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

Es posible que empiece a sentir que los cabos de su cerebro se están rompiendo en este momento.
