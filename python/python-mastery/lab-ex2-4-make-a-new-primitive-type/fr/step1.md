# Création d'une classe MutInt de base

Commençons par créer une classe de base pour notre type Entier mutable. En programmation, une classe est comme un modèle pour créer des objets. Dans cette étape, nous allons créer les bases de notre nouveau type primitif. Un type primitif est un type de données de base fourni par un langage de programmation, et ici nous allons en construire un personnalisé.

1. Ouvrez le WebIDE et accédez au répertoire `/home/labex/project`. Le WebIDE est un environnement de développement intégré où vous pouvez écrire, éditer et exécuter votre code. Accéder à ce répertoire garantit que tous vos fichiers sont organisés en un seul endroit et peuvent interagir correctement les uns avec les autres.

2. Ouvrez le fichier `mutint.py` qui a été créé pour vous lors de l'étape de configuration. Ce fichier sera le lieu de définition de notre classe `MutInt`.

3. Ajoutez le code suivant pour définir une classe `MutInt` de base :

```python
# mutint.py

class MutInt:
    """
    A mutable integer class that allows its value to be modified after creation.
    """
    __slots__ = ['value']

    def __init__(self, value):
        """Initialize with an integer value."""
        self.value = value
```

L'attribut `__slots__` est utilisé pour définir les attributs que cette classe peut avoir. Les attributs sont comme des variables appartenant à un objet de la classe. En utilisant `__slots__`, nous indiquons à Python d'utiliser une méthode plus efficace en mémoire pour stocker les attributs. Dans ce cas, notre classe `MutInt` n'aura qu'un seul attribut appelé `value`. Cela signifie que chaque objet de la classe `MutInt` ne pourra contenir qu'une seule donnée, qui est la valeur entière.

La méthode `__init__` est le constructeur de notre classe. Un constructeur est une méthode spéciale qui est appelée lorsqu'un objet de la classe est créé. Il prend un paramètre de valeur et le stocke dans l'attribut `value` de l'instance. Une instance est un objet individuel créé à partir du modèle de la classe.

Testons notre classe en créant un script Python pour l'utiliser :

4. Créez un nouveau fichier appelé `test_mutint.py` dans le même répertoire :

```python
# test_mutint.py

from mutint import MutInt

# Create a MutInt object
a = MutInt(3)
print(f"Created MutInt with value: {a.value}")

# Modify the value (demonstrating mutability)
a.value = 42
print(f"Modified value to: {a.value}")

# Try adding (this will fail)
try:
    result = a + 10
    print(f"Result of a + 10: {result}")
except TypeError as e:
    print(f"Error when adding: {e}")
```

Dans ce script de test, nous importons d'abord la classe `MutInt` à partir du fichier `mutint.py`. Ensuite, nous créons un objet de la classe `MutInt` avec une valeur initiale de 3. Nous affichons la valeur initiale, puis nous la modifions à 42 et affichons la nouvelle valeur. Enfin, nous essayons d'ajouter 10 à l'objet `MutInt`, ce qui entraînera une erreur car notre classe ne prend pas encore en charge l'opération d'addition.

5. Exécutez le script de test en exécutant la commande suivante dans le terminal :

```bash
python3 /home/labex/project/test_mutint.py
```

Le terminal est une interface en ligne de commande où vous pouvez exécuter diverses commandes pour interagir avec votre système et votre code. Exécuter cette commande exécutera le script `test_mutint.py`.

Vous devriez voir une sortie similaire à ceci :

```
Created MutInt with value: 3
Modified value to: 42
Error when adding: unsupported operand type(s) for +: 'MutInt' and 'int'
```

Notre classe `MutInt` stocke et met à jour une valeur avec succès. Cependant, elle présente plusieurs limitations :

- Elle n'est pas affichée correctement lorsqu'elle est imprimée
- Elle ne prend pas en charge les opérations mathématiques telles que l'addition
- Elle ne prend pas en charge les comparaisons
- Elle ne prend pas en charge les conversions de type

Dans les étapes suivantes, nous allons résoudre ces limitations une par une pour que notre classe `MutInt` se comporte plus comme un véritable type primitif.
