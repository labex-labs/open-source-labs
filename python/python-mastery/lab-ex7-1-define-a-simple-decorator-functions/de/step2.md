# Ein echter Dekorator

Hinweis: Vollständigen Sie Folgendes in der Datei `validate.py`

In Übung 6.6 haben Sie eine aufrufbare Klasse `ValidatedFunction` erstellt, die die Typanmerkungen durchsetzt. Schreiben Sie diese Klasse als Dekoratorfunktion namens `validated` um. Es sollte Ihnen ermöglichen, Code wie diesen zu schreiben:

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

So sollten die dekorierten Funktionen funktionieren:

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
```

Ihr Dekorator sollte versuchen, die Ausnahmen zu verbessern, sodass sie wie gezeigt nützlichere Informationen anzeigen. Außerdem sollte der `@validated`-Dekorator in Klassen funktionieren (Sie müssen nichts Besonderes tun).

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

Hinweis: Dieser Teil beinhaltet nicht viel Code, aber es gibt viele kleine, umständliche Details. Die Lösung wird fast genauso aussehen wie für Übung 6.6. Seien Sie nicht schüchtern, die Lösungs-Code anzusehen.
