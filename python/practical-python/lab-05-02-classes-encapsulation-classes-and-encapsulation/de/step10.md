# `__slots__`-Attribut

Sie können die Menge der Attributnamen einschränken.

```python
class Stock:
    __slots__ = ('name','_shares','price')
    def __init__(self, name, shares, price):
        self.name = name
     ...
```

Es wird ein Fehler für andere Attribute auslösen.

```python
>>> s.price = 385.15
>>> s.prices = 410.2
Traceback (most recent call last):
File "<stdin>", line 1, in?
AttributeError: 'Stock' Objekt hat kein Attribut 'prices'
```

Obwohl dies Fehler verhindert und die Verwendung von Objekten einschränkt, wird es tatsächlich für die Leistung verwendet und lässt Python den Arbeitsspeicher effizienter nutzen.
