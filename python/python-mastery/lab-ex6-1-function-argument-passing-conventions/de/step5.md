# Von vorne beginnen

Erstellen Sie eine neue Datei `stock.py` (oder löschen Sie Ihren gesamten vorherigen Code). Beginnen Sie von vorne, indem Sie `Stock` wie folgt definieren:

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name','shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Sobald Sie das getan haben, führen Sie Ihre `teststock.py`-Unit-Tests aus. Sie sollten viele Fehler erhalten, aber zumindest ein paar der Tests sollten bestehen.
