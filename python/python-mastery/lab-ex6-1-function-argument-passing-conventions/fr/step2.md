# Création d'une classe de base pour les structures

Maintenant que nous comprenons bien le passage d'arguments de fonction, nous allons créer une classe de base réutilisable pour les structures de données. Cette étape est cruciale car elle nous aide à éviter d'écrire le même code à plusieurs reprises lorsque nous créons de simples classes pour stocker des données. En utilisant une classe de base, nous pouvons rationaliser notre code et le rendre plus efficace.

## Le problème du code répétitif

Dans les exercices précédents, vous avez défini une classe `Stock` comme indiqué ci - dessous :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Regardez attentivement la méthode `__init__`. Vous remarquerez qu'elle est assez répétitive. Vous devez attribuer manuellement chaque attribut un par un. Cela peut devenir très fastidieux et chronophage, surtout lorsque vous avez de nombreuses classes avec un grand nombre d'attributs.

## Création d'une classe de base flexible

Créons une classe de base `Structure` qui peut gérer automatiquement l'attribution des attributs. Tout d'abord, ouvrez le WebIDE et créez un nouveau fichier nommé `structure.py`. Ensuite, ajoutez le code suivant à ce fichier :

```python
# structure.py

class Structure:
    """
    A base class for creating simple data structures.
    Automatically populates object attributes from _fields and constructor arguments.
    """
    _fields = ()

    def __init__(self, *args):
        # Check that the number of arguments matches the number of fields
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")

        # Set the attributes
        for name, value in zip(self._fields, args):
            setattr(self, name, value)
```

Cette classe de base a plusieurs caractéristiques importantes :

1. Elle définit une variable de classe `_fields`. Par défaut, cette variable est vide. Cette variable contiendra les noms des attributs que la classe aura.
2. Elle vérifie si le nombre d'arguments passés au constructeur correspond au nombre de champs définis dans `_fields`. Si ce n'est pas le cas, elle lève une erreur `TypeError`. Cela nous aide à détecter les erreurs tôt.
3. Elle définit les attributs de l'objet en utilisant les noms de champ et les valeurs fournies en tant qu'arguments. La fonction `setattr` est utilisée pour définir dynamiquement les attributs.

## Test de notre classe de base Structure

Maintenant, créons quelques classes d'exemple qui héritent de la classe de base `Structure`. Ajoutez le code suivant à votre fichier `structure.py` :

```python
# Example classes using Structure
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

class Point(Structure):
    _fields = ('x', 'y')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

Pour tester si notre implémentation fonctionne correctement, nous allons créer un fichier de test nommé `test_structure.py`. Ajoutez le code suivant à ce fichier :

```python
# test_structure.py
from structure import Stock, Point, Date

# Test Stock class
s = Stock('GOOG', 100, 490.1)
print(f"Stock name: {s.name}, shares: {s.shares}, price: {s.price}")

# Test Point class
p = Point(3, 4)
print(f"Point coordinates: ({p.x}, {p.y})")

# Test Date class
d = Date(2023, 11, 9)
print(f"Date: {d.year}-{d.month}-{d.day}")

# Test error handling
try:
    s2 = Stock('AAPL', 50)  # Missing price argument
    print("This should not print")
except TypeError as e:
    print(f"Error correctly caught: {e}")
```

Pour exécuter le test, ouvrez votre terminal et exécutez la commande suivante :

```bash
python3 test_structure.py
```

Vous devriez voir la sortie suivante :

```
Stock name: GOOG, shares: 100, price: 490.1
Point coordinates: (3, 4)
Date: 2023-11-9
Error correctly caught: Expected 3 arguments
```

Comme vous pouvez le voir, notre classe de base fonctionne comme prévu. Elle a rendu beaucoup plus facile la définition de nouvelles structures de données sans avoir à écrire le même code de base à plusieurs reprises.
