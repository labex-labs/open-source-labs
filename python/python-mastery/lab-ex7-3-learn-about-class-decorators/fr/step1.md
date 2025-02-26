# Revoir les descripteurs

Dans l'exercice 4.3, vous avez défini certains descripteurs qui permettent à un utilisateur de définir des classes avec des attributs vérifiés par type comme ceci :

```python
from validate import String, PositiveInteger, PositiveFloat

class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()
  ...
```

Modifiez votre classe `Stock` de sorte qu'elle inclue les descripteurs ci-dessus et ressemble maintenant à ceci (voir l'exercice 6.4) :

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

Exécutez les tests unitaires dans `teststock.py`. Vous devriez voir un nombre important de tests réussir avec l'ajout de la vérification de type. Excellent.
