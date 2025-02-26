# Überprüfung von Methodenargumenten

Erinnern Sie sich an den `@validated`-Dekorator, den Sie im letzten Teil geschrieben haben? Ändern Sie den `@validate_attributes`-Dekorator so, dass jede Methode in der Klasse mit Anmerkungen automatisch von `@validated` umschlossen wird. Dadurch können Sie erzwungene Anmerkungen auf Methoden wie die `sell()`-Methode setzen:

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

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Sie werden feststellen, dass `sell()` jetzt das Argument erzwängt.

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.sell(-25)
Traceback (most recent call last):
...
TypeError: Bad Arguments
  nshares: must be >= 0
>>>
```

Ja, dies wird jetzt sehr interessant. Die Kombination aus einem Klassen-Dekorator und Vererbung ist eine mächtige Kraft.
