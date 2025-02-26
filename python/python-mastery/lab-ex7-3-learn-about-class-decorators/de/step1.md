# Wiederholung von Deskriptoren

In Übung 4.3 haben Sie einige Deskriptoren definiert, die es einem Benutzer ermöglicht, Klassen mit typengeprüften Attributen wie folgt zu definieren:

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
  ...
```

Ändern Sie Ihre `Stock`-Klasse so, dass sie die obigen Deskriptoren enthält und nun wie folgt aussieht (siehe Übung 6.4):

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    _fields = ('name','shares', 'price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

Führen Sie die Unit-Tests in `teststock.py` aus. Sie sollten sehen, dass eine erhebliche Anzahl von Tests mit der Hinzufügung der Typüberprüfung erfolgreich abgeschlossen wird. Großartig.
