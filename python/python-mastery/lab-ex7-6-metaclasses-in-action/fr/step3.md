# Création de la métaclasse StructureMeta

Maintenant, parlons de ce que nous allons faire ensuite. Nous avons trouvé un moyen de collecter tous les types de validateurs. Notre prochaine étape consiste à créer une métaclasse. Mais qu'est - ce exactement qu'une métaclasse ? En Python, une métaclasse est un type spécial de classe. Ses instances sont des classes elles - mêmes. Cela signifie qu'une métaclasse peut contrôler la façon dont une classe est créée. Elle peut gérer l'espace de noms où les attributs de classe sont définis.

Dans notre cas, nous voulons créer une métaclasse qui rendra les types de validateurs disponibles lorsque nous définissons une sous - classe de `Structure`. Nous ne voulons pas avoir à importer explicitement ces types de validateurs à chaque fois.

Commençons par rouvrir le fichier `structure.py`. Vous pouvez utiliser la commande suivante pour l'ouvrir :

```bash
code structure.py
```

Une fois le fichier ouvert, nous devons ajouter du code en haut, avant la définition de la classe `Structure`. Ce code définira notre métaclasse.

```python
from validate import Validator
from collections import ChainMap

class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        """Prepare the namespace for the class being defined"""
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        """Create the new class using only the local namespace"""
        methods = methods.maps[0]  # Extract the local namespace
        return super().__new__(meta, name, bases, methods)
```

Maintenant que nous avons défini la métaclasse, nous devons modifier la classe `Structure` pour l'utiliser. De cette façon, toute classe qui hérite de `Structure` bénéficiera de la fonctionnalité de la métaclasse.

```python
class Structure(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

        # Set the remaining keyword arguments
        for name, val in kwargs.items():
            if name not in self._fields:
                raise TypeError(f'Invalid argument: {name}')
            setattr(self, name, val)

    def __repr__(self):
        values = [getattr(self, name) for name in self._fields]
        args_str = ','.join(repr(val) for val in values)
        return f'{type(self).__name__}({args_str})'
```

Analysons ce que ce code fait :

1. La méthode `__prepare__()` est une méthode spéciale en Python. Elle est appelée avant la création de la classe. Son rôle est de préparer l'espace de noms où les attributs de classe seront définis. Nous utilisons `ChainMap` ici. `ChainMap` est un outil utile qui crée un dictionnaire en couches. Dans notre cas, il inclut nos types de validateurs, les rendant accessibles dans l'espace de noms de la classe.

2. La méthode `__new__()` est responsable de la création de la nouvelle classe. Nous extrayons uniquement l'espace de noms local, qui est le premier dictionnaire dans le `ChainMap`. Nous rejetons le dictionnaire des validateurs car nous avons déjà rendu les types de validateurs disponibles dans l'espace de noms.

Avec cette configuration, toute classe qui hérite de `Structure` aura accès à tous les types de validateurs sans avoir besoin de les importer explicitement.

Maintenant, testons notre implémentation. Nous allons créer une classe `Stock` en utilisant notre classe de base `Structure` améliorée.

```bash
cat > stock.py << EOF
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
EOF
```

Si notre métaclasse fonctionne correctement, nous devrions être en mesure de définir la classe `Stock` sans importer les types de validateurs. C'est parce que la métaclasse les a déjà rendus disponibles dans l'espace de noms.
