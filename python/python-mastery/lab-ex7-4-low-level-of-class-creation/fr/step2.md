# Création d'un outil pour des structures typées

Dans cette étape, nous allons construire un exemple plus pratique. Nous allons implémenter une fonction qui crée des classes avec validation de type. La validation de type est cruciale car elle garantit que les données assignées aux attributs de classe répondent à des critères spécifiques, comme être d'un certain type de données ou se trouver dans une plage particulière. Cela permet de détecter les erreurs tôt et rend notre code plus robuste.

## Compréhension de la classe Structure

Tout d'abord, nous devons ouvrir le fichier `structure.py` dans l'éditeur WebIDE. Ce fichier contient une classe `Structure` de base. Cette classe fournit la fonctionnalité fondamentale pour l'initialisation et la représentation d'objets structurés. L'initialisation consiste à configurer l'objet avec les données fournies, et la représentation concerne la façon dont l'objet est affiché lorsqu'on l'imprime.

Pour ouvrir le fichier, nous allons utiliser la commande suivante dans le terminal :

```bash
cd ~/project
```

Après avoir exécuté cette commande, vous vous trouverez dans le bon répertoire où se trouve le fichier `structure.py`. Lorsque vous ouvrez le fichier, vous remarquerez la classe `Structure` de base. Notre objectif est d'étendre cette classe pour prendre en charge la validation de type.

## Implémentation de la fonction typed_structure

Maintenant, ajoutons la fonction `typed_structure` au fichier `structure.py`. Cette fonction créera une nouvelle classe qui hérite de la classe `Structure` et inclut les validateurs spécifiés. L'héritage signifie que la nouvelle classe aura toute la fonctionnalité de la classe `Structure` et peut également ajouter ses propres fonctionnalités. Les validateurs sont utilisés pour vérifier si les valeurs assignées aux attributs de classe sont valides.

Voici le code de la fonction `typed_structure` :

```python
def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

Le paramètre `clsname` est le nom que nous voulons donner à la nouvelle classe. Le paramètre `validators` est un dictionnaire où les clés sont les noms des attributs et les valeurs sont les objets validateurs. La fonction `type()` est utilisée pour créer dynamiquement une nouvelle classe. Elle prend trois arguments : le nom de la classe, un tuple de classes de base (dans ce cas, seulement la classe `Structure`), et un dictionnaire d'attributs de classe (les validateurs).

Après avoir ajouté cette fonction, votre fichier `structure.py` devrait ressembler à ceci :

```python
# Structure class definition

class Structure:
    _fields = ()

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __repr__(self):
        attrs = ', '.join(f'{name}={getattr(self, name)!r}' for name in self._fields)
        return f'{type(self).__name__}({attrs})'

def typed_structure(clsname, **validators):
    """
    Create a Structure class with type validation.

    Parameters:
    - clsname: Name of the class to create
    - validators: Keyword arguments mapping attribute names to validator objects

    Returns:
    - A new class with the specified name and validators
    """
    cls = type(clsname, (Structure,), validators)
    return cls
```

## Test de la fonction typed_structure

Testons notre fonction `typed_structure` en utilisant les validateurs du fichier `validate.py`. Ces validateurs sont utilisés pour vérifier si les valeurs assignées aux attributs de classe sont du bon type et répondent à d'autres critères.

Tout d'abord, ouvrez un shell interactif Python. Nous allons utiliser les commandes suivantes dans le terminal :

```bash
cd ~/project
python3
```

La première commande nous amène dans le bon répertoire, et la deuxième commande lance le shell interactif Python.

Maintenant, importez les composants nécessaires et créez une structure typée :

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import typed_structure

# Create a Stock class with type validation
Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())

# Create a stock instance
s = Stock('GOOG', 100, 490.1)

# Test the instance
print(s.name)
print(s)

# Test validation
try:
    invalid_stock = Stock('AAPL', -10, 150.25)  # Should raise an error
except ValueError as e:
    print(f"Validation error: {e}")
```

Nous importons les validateurs `String`, `PositiveInteger` et `PositiveFloat` du fichier `validate.py`. Ensuite, nous utilisons la fonction `typed_structure` pour créer une classe `Stock` avec validation de type. Nous créons une instance de la classe `Stock` et la testons en imprimant ses attributs. Enfin, nous essayons de créer une instance de stock invalide pour tester la validation.

Vous devriez voir une sortie similaire à :

```
GOOG
Stock('GOOG', 100, 490.1)
Validation error: Expected a positive value
```

Lorsque vous avez terminé de tester, quittez le shell Python :

```python
exit()
```

Cet exemple montre comment nous pouvons utiliser la fonction `type()` pour créer des classes personnalisées avec des règles de validation spécifiques. Cette approche est très puissante car elle nous permet de générer des classes de manière programmée, ce qui peut économiser beaucoup de temps et rendre notre code plus flexible.
