# Spezielle Methoden für Stringkonvertierungen

Objekte haben zwei Stringdarstellungen.

```python
>>> from datetime import date
>>> d = date(2012, 12, 21)
>>> print(d)
2012-12-21
>>> d
datetime.date(2012, 12, 21)
>>>
```

Die `str()`-Funktion wird verwendet, um eine hübsche ausdruckbare Ausgabe zu erzeugen:

```python
>>> str(d)
'2012-12-21'
>>>
```

Die `repr()`-Funktion wird verwendet, um eine detailliertere Darstellung für Programmierer zu erzeugen.

```python
>>> repr(d)
'datetime.date(2012, 12, 21)'
>>>
```

Diese Funktionen, `str()` und `repr()`, verwenden eine Reihe spezieller Methoden in der Klasse, um den anzuzeigenden String zu erzeugen.

```python
class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Wird mit `str()` verwendet
    def __str__(self):
        return f'{self.year}-{self.month}-{self.day}'

    # Wird mit `repr()` verwendet
    def __repr__(self):
        return f'Date({self.year},{self.month},{self.day})'
```

_Hinweis: Die Konvention für `__repr__()` besteht darin, einen String zurückzugeben, der, wenn an `eval()` übergeben wird, das zugrunde liegende Objekt wiederherstellt. Wenn dies nicht möglich ist, wird stattdessen eine leicht lesbare Darstellung verwendet._
