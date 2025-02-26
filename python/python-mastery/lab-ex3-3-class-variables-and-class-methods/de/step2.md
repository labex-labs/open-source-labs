# Alternativkonstruktoren

Vielleicht kann die Erstellung eines `Stock`-Objekts aus einer Zeile von Rohdaten besser durch einen alternativen Konstruktor behandelt werden. Ändern Sie die `Stock`-Klasse so, dass sie eine `types`-Klassenvariable und eine `from_row()`-Klassenmethode hat, wie folgt:

```python
class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
  ...
```

Hier ist, wie Sie es testen können:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock.from_row(row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>> s.cost()
3220.0000000000005
>>>
```

Beobachten Sie genau, wie die Zeichenfolgenwerte in der Zeile in einen passenden Typ umgewandelt wurden.
