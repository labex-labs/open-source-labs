# Typisierte Strukturen

In der Datei `structure.py` definieren Sie die folgende Funktion:

```python
# structure.py

...
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
```

Diese Funktion ähnelt in gewisser Weise der Funktion `namedtuple()`, insofern als sie eine Klasse erstellt. Testen Sie es:

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

Sie werden vielleicht merken, dass Ihre Kopfhaut sich hier langsam auseinanderzieht.
