# Vérification des arguments de méthode

Rappelez-vous le décorateur `@validated` que vous avez écrit dans la dernière partie? Modifions le décorateur `@validate_attributes` de sorte que toute méthode dans la classe avec des annotations soit automatiquement enveloppée par `@validated`. Cela vous permet d'ajouter des annotations contraignantes à des méthodes telles que la méthode `sell()` :

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

Vous constaterez que `sell()` impose désormais l'argument.

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

Oui, tout cela devient très intéressant maintenant. La combinaison d'un décorateur de classe et d'héritage est une force puissante.
