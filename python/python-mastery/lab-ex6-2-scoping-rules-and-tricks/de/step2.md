# Zeig mir deine lokalen Variablen

Versuchen Sie zunächst ein Experiment, indem Sie die folgende Klasse definieren:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            print(locals())

>>>
```

Versuchen Sie nun, das folgende auszuführen:

```python
>>> s = Stock('GOOG', 100, 490.1)
{'self': <__main__.Stock Objekt am 0x100699b00>, 'price': 490.1, 'name': 'GOOG','shares': 100}
>>>
```

Bemerken Sie, wie das lokale Wörterbuch alle Argumente enthält, die an `__init__()` übergeben wurden. Das ist interessant. Definieren Sie nun die folgenden Funktions- und Klassendefinitionen:

```python
>>> def _init(locs):
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

>>> class Stock:
        def __init__(self, name, shares, price):
            _init(locals())
```

In diesem Code wird die `_init()`-Funktion verwendet, um ein Objekt automatisch aus einem Wörterbuch von übergebenen lokalen Variablen zu initialisieren. Sie werden feststellen, dass `help(Stock)` und Schlüsselwortargumente perfekt funktionieren.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>>
```
