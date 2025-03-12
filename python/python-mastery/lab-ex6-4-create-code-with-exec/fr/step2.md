# Création d'une méthode **init**() dynamique

Maintenant, nous allons appliquer ce que nous avons appris sur la fonction `exec()` à un scénario de programmation du monde réel. En Python, la fonction `exec()` vous permet d'exécuter du code Python stocké dans une chaîne de caractères. Dans cette étape, nous allons modifier la classe `Structure` pour créer dynamiquement une méthode `__init__()`. La méthode `__init__()` est une méthode spéciale dans les classes Python, qui est appelée lorsque un objet de la classe est instancié. Nous allons baser la création de cette méthode sur la variable de classe `_fields`, qui contient une liste de noms de champs pour la classe.

Tout d'abord, regardons le fichier `structure.py` existant. Ce fichier contient l'implémentation actuelle de la classe `Structure` et d'une classe `Stock` qui en hérite. Pour afficher le contenu du fichier, ouvrez - le dans l'éditeur WebIDE en utilisant la commande suivante :

```bash
cat /home/labex/project/structure.py
```

Dans la sortie, vous verrez que l'implémentation actuelle utilise une approche manuelle pour gérer l'initialisation des objets. Cela signifie que le code pour initialiser les attributs de l'objet est écrit explicitement, plutôt que d'être généré dynamiquement.

Maintenant, nous allons modifier la classe `Structure`. Nous allons ajouter une méthode de classe `create_init()` qui générera dynamiquement la méthode `__init__()`. Pour apporter ces modifications, ouvrez le fichier `structure.py` dans l'éditeur WebIDE et suivez ces étapes :

1. Supprimez les méthodes `_init()` et `set_fields()` existantes de la classe `Structure`. Ces méthodes font partie de l'approche d'initialisation manuelle, et nous n'en aurons plus besoin car nous allons utiliser une approche dynamique.

2. Ajoutez la méthode de classe `create_init()` à la classe `Structure`. Voici le code de la méthode :

```python
@classmethod
def create_init(cls):
    """Dynamically create an __init__ method based on _fields."""
    # Create argument string from field names
    argstr = ','.join(cls._fields)

    # Create the function code as a string
    code = f'def __init__(self, {argstr}):\n'
    for name in cls._fields:
        code += f'    self.{name} = {name}\n'

    # Execute the code and get the generated function
    locs = {}
    exec(code, locs)

    # Set the function as the __init__ method of the class
    setattr(cls, '__init__', locs['__init__'])
```

Dans cette méthode, nous créons d'abord une chaîne `argstr` qui contient tous les noms de champs séparés par des virgules. Cette chaîne sera utilisée comme liste d'arguments pour la méthode `__init__()`. Ensuite, nous créons le code pour la méthode `__init__()` sous forme de chaîne. Nous parcourons les noms de champs et ajoutons des lignes au code qui attribuent chaque argument à l'attribut d'objet correspondant. Après cela, nous utilisons la fonction `exec()` pour exécuter le code et stockons la fonction générée dans le dictionnaire `locs`. Enfin, nous utilisons la fonction `setattr()` pour définir la fonction générée comme méthode `__init__()` de la classe.

3. Modifiez la classe `Stock` pour utiliser cette nouvelle approche :

```python
class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Ici, nous définissons les `_fields` pour la classe `Stock`, puis nous appelons la méthode `create_init()` pour générer la méthode `__init__()` pour la classe `Stock`.

Votre fichier `structure.py` complet devrait maintenant ressembler à ceci :

```python
class Structure:
    # Restrict attribute assignment
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"No attribute {name}")

    # String representation for debugging
    def __repr__(self):
        args = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f"{type(self).__name__}({args})"

    @classmethod
    def create_init(cls):
        """Dynamically create an __init__ method based on _fields."""
        # Create argument string from field names
        argstr = ','.join(cls._fields)

        # Create the function code as a string
        code = f'def __init__(self, {argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'

        # Execute the code and get the generated function
        locs = {}
        exec(code, locs)

        # Set the function as the __init__ method of the class
        setattr(cls, '__init__', locs['__init__'])

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

# Create the __init__ method for Stock
Stock.create_init()
```

Maintenant, testons notre implémentation pour nous assurer qu'elle fonctionne correctement. Nous allons exécuter le fichier de tests unitaires pour vérifier si tous les tests passent. Utilisez les commandes suivantes :

```bash
cd /home/labex/project
python3 -m unittest test_structure.py
```

Si votre implémentation est correcte, vous devriez voir que tous les tests passent. Cela signifie que la méthode `__init__()` générée dynamiquement fonctionne comme prévu.

Vous pouvez également tester la classe manuellement dans le shell Python. Voici comment vous pouvez le faire :

```python
>>> from structure import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s
Stock('GOOG', 100, 490.1)
>>> s.shares = 50
>>> s.share = 50  # This should raise an AttributeError
Traceback (most recent call last):
  ...
AttributeError: No attribute share
```

Dans le shell Python, nous importons d'abord la classe `Stock` à partir du fichier `structure.py`. Ensuite, nous créons une instance de la classe `Stock` et l'affichons. Nous pouvons également modifier l'attribut `shares` de l'objet. Cependant, lorsque nous essayons de définir un attribut qui n'existe pas dans la liste `_fields`, nous devrions obtenir une `AttributeError`.

Félicitations ! Vous avez utilisé avec succès la fonction `exec()` pour créer dynamiquement une méthode `__init__()` en fonction des attributs de classe. Cette approche peut rendre votre code plus flexible et plus facile à maintenir, en particulier lorsqu'il s'agit de classes ayant un nombre variable d'attributs.
