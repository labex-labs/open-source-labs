# Dicts and Objects

Benutzerdefinierte Objekte verwenden ebenfalls Wörterbücher für Instanzdaten und Klassen. Tatsächlich besteht das gesamte Objektsystem größtenteils aus einer zusätzlichen Schicht, die auf Wörterbüchern aufgesetzt ist.

Ein Wörterbuch enthält die Instanzdaten, `__dict__`.

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.__dict__
{'name' : 'GOOG','shares' : 100, 'price': 490.1 }
```

Sie füllen dieses Dict (und die Instanz) bei der Zuweisung an `self`.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Die Instanzdaten, `self.__dict__`, sehen so aus:

```python
{
    'name': 'GOOG',
   'shares': 100,
    'price': 490.1
}
```

**Jede Instanz bekommt ihr eigenes privates Wörterbuch.**

```python
s = Stock('GOOG', 100, 490.1)     # {'name' : 'GOOG','shares' : 100, 'price': 490.1 }
t = Stock('AAPL', 50, 123.45)     # {'name' : 'AAPL','shares' : 50, 'price': 123.45 }
```

Wenn Sie 100 Instanzen einer Klasse erzeugen, gibt es 100 Wörterbücher, die Daten speichern.
