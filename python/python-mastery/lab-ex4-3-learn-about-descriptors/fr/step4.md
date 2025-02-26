# Correction des Noms

Un aspect gênant des descripteurs est la spécification de nom redondante. Par exemple :

```python
class Stock:
  ...
    shares = PositiveInteger('shares')
  ...
```

Nous pouvons corriger cela. Modifiez la classe `Validator` de niveau supérieur pour inclure une méthode `__set_name__()` comme ceci :

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Maintenant, essayez de réécrire votre classe `Stock` de sorte qu'elle ressemble à ceci :

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ah, bien mieux. Notez cependant que cette capacité à définir le nom est une fonctionnalité de Python 3.6. Elle ne fonctionnera pas sur les versions antérieures.
