# Die überraschende Macht der Iteration

Python verwendet Iteration auf Weise, die Sie vielleicht nicht erwarten. Nachdem Sie `__iter__()` zur `Structure`-Klasse hinzugefügt haben, stellen Sie fest, dass es einfach ist, alle sorts neuer Operationen durchzuführen. Beispielsweise Konvertierungen in Sequenzen und Entpackungen:

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> list(s)
['GOOG', 100, 490.1]
>>> tuple(s)
('GOOG', 100, 490.1)
>>> name, shares, price = s
>>> name
'GOOG'
>>> shares
100
>>> price
490.1
>>>
```

Während wir dabei sind, können wir jetzt einen Vergleichsoperator zur `Structure`-Klasse hinzufügen:

```python
# structure.py
class Structure(metaclass=StructureMeta):
 ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
 ...
```

Sie sollten jetzt in der Lage sein, Objekte zu vergleichen:

```python
>>> a = Stock('GOOG', 100, 490.1)
>>> b = Stock('GOOG', 100, 490.1)
>>> a == b
True
>>>
```

Versuchen Sie, Ihre `teststock.py`-Einhheits-Tests erneut auszuführen. Jetzt sollten alle Tests bestanden werden. Großartig.
