# Anwenden von Dekoratoren über Vererbung

Das Angeben des Klassen-Dekorators selbst ist ziemlich ärgerlich. Ändern Sie die `Structure`-Klasse mit der folgenden `__init_subclass__()`-Methode:

```python
# structure.py

class Structure:
 ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

Nachdem Sie diese Änderung vorgenommen haben, sollten Sie den Dekorator ganz weglassen können und sich ausschließlich auf Vererbung verlassen. Es ist Vererbung plus etwas verstecktes Magie!

```python
# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Jetzt beginnt der Code wirklich zu punkten. Tatsächlich sieht er fast normal aus. Lassen Sie uns ihn weiter verbessern.
