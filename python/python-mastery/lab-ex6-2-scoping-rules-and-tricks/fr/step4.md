# Implémentation de l'initialisation avancée dans la classe Structure

Nous venons de découvrir deux techniques puissantes pour accéder aux arguments d'une fonction. Maintenant, nous allons utiliser ces techniques pour mettre à jour notre classe `Structure`. Commençons par comprendre pourquoi nous le faisons. Ces techniques rendront notre classe plus flexible et plus facile à utiliser, notamment lorsqu'il s'agit de gérer différents types d'arguments.

Ouvrez le fichier `structure.py` dans votre éditeur de code. Vous pouvez le faire en exécutant les commandes suivantes dans le terminal. La commande `cd` permet de changer de répertoire pour accéder au dossier du projet, tandis que la commande `code` ouvre le fichier `structure.py` dans l'éditeur de code.

```bash
cd ~/project
code structure.py
```

Remplacez le contenu du fichier par le code suivant. Ce code définit une classe `Structure` avec plusieurs méthodes. Analysons chaque partie pour comprendre son fonctionnement.

```python
import sys

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Get the caller's frame (the __init__ method that called this)
        frame = sys._getframe(1)

        # Get the local variables from that frame
        locs = frame.f_locals

        # Extract self and set other variables as attributes
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({values})'

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'{type(self).__name__!r} has no attribute {name!r}')
```

Voici ce que nous avons fait dans le code :

1. Nous avons supprimé l'ancienne méthode `__init__()`. Étant donné que les sous - classes définiront leurs propres méthodes `__init__`, nous n'en avons plus besoin.
2. Nous avons ajouté une nouvelle méthode statique `_init()`. Cette méthode utilise l'inspection des cadres de pile pour capturer automatiquement tous les paramètres et les définir comme attributs. L'inspection des cadres de pile nous permet d'accéder aux variables locales de la méthode appelante.
3. Nous avons conservé la méthode `__repr__()`. Cette méthode fournit une représentation sous forme de chaîne de caractères de l'objet, ce qui est utile pour le débogage et l'affichage.
4. Nous avons ajouté une méthode `__setattr__()`. Cette méthode assure la validation des attributs, garantissant que seuls les attributs valides peuvent être définis sur l'objet.

Maintenant, mettons à jour la classe `Stock`. Ouvrez le fichier `stock.py` en utilisant la commande suivante :

```bash
code stock.py
```

Remplacez son contenu par le code suivant :

```python
from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    def __init__(self, name, shares, price):
        self._init()  # This magically captures and sets all parameters!

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Le changement clé ici est que notre méthode `__init__` appelle maintenant `self._init()` au lieu de définir manuellement chaque attribut. La méthode `_init()` utilise l'inspection des cadres de pile pour capturer automatiquement tous les paramètres et les définir comme attributs. Cela rend le code plus concis et plus facile à maintenir.

Testons notre implémentation en exécutant les tests unitaires. Les tests unitaires nous aideront à nous assurer que notre code fonctionne comme prévu. Exécutez les commandes suivantes dans le terminal :

```bash
cd ~/project
python3 teststock.py
```

Vous devriez constater que tous les tests passent, y compris le test pour les arguments nommés (keyword arguments) qui échouait auparavant. Cela signifie que notre implémentation fonctionne correctement.

Vérifions également la documentation d'aide pour notre classe `Stock`. La documentation d'aide fournit des informations sur la classe et ses méthodes. Exécutez la commande suivante dans le terminal :

```bash
python3 -c "from stock import Stock; help(Stock)"
```

Maintenant, vous devriez voir une signature appropriée pour la méthode `__init__`, affichant tous les noms de paramètres. Cela facilite la compréhension pour les autres développeurs sur la façon d'utiliser la classe.

Enfin, testons de manière interactive que les arguments nommés fonctionnent comme prévu. Exécutez la commande suivante dans le terminal :

```bash
python3 -c "from stock import Stock; s = Stock(name='GOOG', shares=100, price=490.1); print(s)"
```

Vous devriez voir l'objet `Stock` correctement créé avec les attributs spécifiés. Cela confirme que notre système d'initialisation de classe prend en charge les arguments nommés.

Avec cette implémentation, nous avons mis en place un système d'initialisation de classe beaucoup plus flexible et convivial qui :

1. Préserve les signatures de fonction appropriées dans la documentation, facilitant la compréhension pour les développeurs sur la façon d'utiliser la classe.
2. Prend en charge à la fois les arguments positionnels et les arguments nommés, offrant plus de flexibilité lors de la création d'objets.
3. Nécessite un minimum de code boilerplate dans les sous - classes, réduisant ainsi la quantité de code à écrire.
