# Stackframe-Hacking

Eine Bedenken gegen den letzten Teil ist, dass die `__init__()`-Funktion jetzt ziemlich seltsam aussieht, da der Aufruf von `locals()` darin eingefügt wurde. Sie können das umgehen, wenn Sie bereit sind, ein bisschen Stackframe-Hacking durchzuführen. Versuchen Sie diese Variante der `_init()`-Funktion:

```python
>>> import sys
>>> def _init():
        locs = sys._getframe(1).f_locals   # Holen Sie sich die lokalen Variablen des Aufrufers
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
>>>
```

In diesem Code werden die lokalen Variablen aus dem Stackframe des Aufrufers extrahiert. Hier ist eine modifizierte Klassendefinition:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            _init()

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

Zu diesem Zeitpunkt werden Sie wahrscheinlich ziemlich unwohl fühlen. Ja, Sie haben gerade eine Funktion geschrieben, die in den Stackframe einer anderen Funktion eindringt und deren lokale Variablen untersucht.
