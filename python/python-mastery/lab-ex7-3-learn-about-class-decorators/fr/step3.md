# Appliquer les décorateurs via l'héritage

Devoir spécifier le décorateur de classe lui-même est un peu gênant. Modifiez la classe `Structure` avec la méthode `__init_subclass__()` suivante :

```python
# structure.py

class Structure:
 ...
    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)
```

Une fois que vous avez apporté ce changement, vous devriez être en mesure de supprimer complètement le décorateur et de vous fier uniquement à l'héritage. C'est l'héritage plus un peu de magie cachée!

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

Maintenant, le code commence vraiment à évoluer. En fait, il semble presque normal. Continuons à le pousser.
