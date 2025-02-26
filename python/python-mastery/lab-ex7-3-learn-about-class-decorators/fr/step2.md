# Utiliser les décorateurs de classe pour compléter les détails

Un aspect gênant du code ci-dessus est qu'il y a des détails supplémentaires tels que la variable `_fields` et la dernière étape `Stock.create_init()`. Beaucoup de cela pourrait être emballé dans un décorateur de classe à la place.

Dans le fichier `structure.py`, créez un décorateur de classe `@validate_attributes` qui examine le corps de la classe pour des instances de Validators et remplit la variable `_fields`. Par exemple :

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

Ce code repose sur le fait que les dictionnaires de classe sont ordonnés à partir de Python 3.6. Ainsi, il rencontrera les différents descripteurs `Validator` dans l'ordre dans lequel ils sont listés. En utilisant cet ordre, vous pouvez ensuite remplir la variable `_fields`. Cela vous permet d'écrire du code comme ceci :

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

Une fois que cela fonctionne, modifiez le décorateur `@validate_attributes` pour effectuer en outre la dernière étape consistant à appeler `Stock.create_init()`. Cela réduira la classe au suivant :

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
