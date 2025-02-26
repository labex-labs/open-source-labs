# Zusammenführen

Nehmen Sie die Ideen aus den ersten beiden Teilen und löschen Sie die `__init__()`-Methode, die ursprünglich Teil der `Structure`-Klasse war. Fügen Sie anschließend eine `_init()`-Methode hinzu, wie folgt:

```python
# structure.py
import sys

class Structure:
  ...
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
  ...
```

Hinweis: Der Grund, warum dies als `@staticmethod` definiert ist, ist, dass das `self`-Argument aus den lokalen Variablen abgerufen wird - es ist nicht erforderlich, dass es zusätzlich als Argument an die Methode selbst übergeben wird (zugegebenermaßen ist dies ein bisschen subtil).

Ändern Sie nun Ihre `Stock`-Klasse, sodass sie wie folgt aussieht:

```python
# stock.py
from structure import Structure

class Stock(Structure):
    _fields = ('name','shares','price')
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= shares
```

Vergewissern Sie sich, dass die Klasse richtig funktioniert, Schlüsselwortargumente unterstützt und eine korrekte Hilfssignatur hat.

```python
>>> s = Stock(name='GOOG', price=490.1, shares=50)
>>> s.name
'GOOG'
>>> s.shares
50
>>> s.price
490.1
>>> help(Stock)
... schauen Sie sich die Ausgabe an...
>>>
```

Führen Sie Ihre Unit-Tests in `teststock.py` erneut aus. Sie sollten mindestens einen weiteren Test bestehen sehen. Hurra!

Zu diesem Zeitpunkt wird es so aussehen, als hätten wir gerade einen großen Schritt zurückgetan. Nicht nur benötigen die Klassen die `__init__()`-Methode, sondern auch die `_fields`-Variable, damit einige der anderen Methoden funktionieren (`__repr__()` und `__setattr__()`). Darüber hinaus sieht das Verwenden von `self._init()` ziemlich hacky aus. Wir werden uns darum kümmern, aber seien Sie geduldig.
