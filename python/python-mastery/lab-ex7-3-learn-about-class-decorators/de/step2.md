# Verwendung von Klassen-Dekoratoren, um Details auszufüllen

Ein ärgerlicher Aspekt des obigen Codes ist, dass es zusätzliche Details wie die `_fields`-Variable und den letzten Schritt `Stock.create_init()` gibt. Viele davon könnten stattdessen in einem Klassen-Dekorator verpackt werden.

In der Datei `structure.py` erstellen Sie einen Klassen-Dekorator `@validate_attributes`, der den Klassenkörper auf Instanzen von Validatoren überprüft und die `_fields`-Variable ausfüllt. Beispielsweise:

```python
# structure.py

from validate import Validator

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls
```

Dieser Code stützt sich darauf, dass Klassen-Dictionaries in Python 3.6 in aufsteigender Reihenfolge sortiert sind. Somit wird er die verschiedenen `Validator`-Deskriptoren in der Reihenfolge antreffen, in der sie aufgelistet sind. Mit dieser Reihenfolge können Sie dann die `_fields`-Variable ausfüllen. Dadurch können Sie Code wie diesen schreiben:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
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

Sobald das funktioniert, ändern Sie den `@validate_attributes`-Dekorator, um zusätzlich den letzten Schritt auszuführen, nämlich `Stock.create_init()` aufzurufen. Dadurch wird die Klasse zu folgendem:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
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
