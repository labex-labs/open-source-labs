# Klassenvariablen und Vererbung

Klassenvariablen wie `types` werden manchmal als Anpassungsmechanismus verwendet, wenn Vererbung eingesetzt wird. Beispielsweise kann in der `Stock`-Klasse die Art der Typumwandlung in einer Unterklasse leicht geändert werden. Versuchen Sie dieses Beispiel, bei dem das `price`-Attribut in eine `Decimal`-Instanz umgewandelt wird (was für Finanzberechnungen oft besser geeignet ist):

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        types = (str, int, Decimal)

>>> row = ['AA', '100', '32.20']
>>> s = DStock.from_row(row)
>>> s.price
Decimal('32.20')
>>> s.cost()
Decimal('3220.0')
>>>
```

**Design-Diskussion**

Das Problem, das in diesem Labor behandelt wird, betrifft die Umwandlung von Daten, die aus einer Datei gelesen werden. Würde es Sinn ergeben, diese Umwandlungen in der `__init__()`-Methode der `Stock`-Klasse durchzuführen? Beispielsweise:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

Dadurch würden Sie eine Zeile von Daten wie folgt umwandeln:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock(*row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>>
```

Ist dies gut oder schlecht? Was sind Ihre Gedanken dazu? Im Allgemeinen finde ich es eine fragwürdige Designentscheidung, da es zwei verschiedene Dinge zusammenbringt - die Erstellung einer Instanz und die Umwandlung von Daten. Außerdem begrenzen die impliziten Umwandlungen in `__init__()` die Flexibilität und können merkwürdige Fehler verursachen, wenn ein Benutzer nicht genau aufpasst.
