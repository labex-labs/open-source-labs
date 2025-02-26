# Exercice 7.7 : Utiliser les closures pour éviter la répétition

L'une des fonctionnalités les plus puissantes des closures est leur utilisation dans la génération de code répétitif. Si vous vous reportez à l'exercice 5.7, rappelez-vous le code pour définir une propriété avec une vérification de type.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
  ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value
  ...
```

Au lieu de taper répétitivement ce code à l'infini, vous pouvez le créer automatiquement à l'aide d'une closure.

Créez un fichier `typedproperty.py` et mettez le code suivant dedans :

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name
    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, value)

    return prop
```

Maintenant, essayez-le en définissant une classe comme ceci :

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Essayez de créer une instance et de vérifier que la vérification de type fonctionne.

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.name
'IBM'
>>> s.shares = '100'
... devrait générer un TypeError...
>>>
```
