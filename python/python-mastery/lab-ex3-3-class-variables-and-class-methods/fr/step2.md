# Implémentation de constructeurs alternatifs avec des méthodes de classe

Dans cette étape, nous allons apprendre à implémenter un constructeur alternatif en utilisant une méthode de classe. Cela nous permettra de créer des objets `Stock` à partir de données de lignes CSV d'une manière plus élégante.

## Qu'est-ce qu'un constructeur alternatif ?

En Python, un constructeur alternatif est un modèle utile. Habituellement, nous créons des objets en utilisant la méthode standard `__init__`. Cependant, un constructeur alternatif nous offre un moyen supplémentaire de créer des objets. Les méthodes de classe sont très appropriées pour implémenter des constructeurs alternatifs car elles peuvent accéder à la classe elle - même.

## Implémentation de la méthode de classe from_row()

Nous allons ajouter une variable de classe `types` et une méthode de classe `from_row()` à notre classe `Stock`. Cela simplifiera le processus de création d'instances de `Stock` à partir de données CSV.

Modifions le fichier `stock.py` en ajoutant le code mis en évidence :

```python
# stock.py

class Stock:
    types = (str, int, float)  # Type conversions to apply to CSV data

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Create a Stock instance from a row of CSV data.

        Args:
            row: A list of strings [name, shares, price]

        Returns:
            A new Stock instance
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# The rest of the file remains unchanged
```

Maintenant, comprenons étape par étape ce qui se passe dans ce code :

1. Nous avons défini une variable de classe `types`. C'est un tuple qui contient des fonctions de conversion de type `(str, int, float)`. Ces fonctions seront utilisées pour convertir les données de la ligne CSV en types appropriés.
2. Nous avons ajouté une méthode de classe `from_row()`. Le décorateur `@classmethod` marque cette méthode comme une méthode de classe.
3. Le premier paramètre de cette méthode est `cls`, qui est une référence à la classe elle - même. Dans les méthodes normales, nous utilisons `self` pour faire référence à une instance de la classe, mais ici nous utilisons `cls` car il s'agit d'une méthode de classe.
4. La fonction `zip()` est utilisée pour associer chaque fonction de conversion de type dans `types` à la valeur correspondante dans la liste `row`.
5. Nous utilisons une compréhension de liste pour appliquer chaque fonction de conversion à la valeur correspondante dans la liste `row`. De cette façon, nous convertissons les données de chaîne de caractères de la ligne CSV en types appropriés.
6. Enfin, nous créons une nouvelle instance de la classe `Stock` en utilisant les valeurs converties et la retournons.

## Test du constructeur alternatif

Maintenant, nous allons créer un nouveau fichier appelé `test_class_method.py` pour tester notre nouvelle méthode de classe. Cela nous aidera à vérifier que le constructeur alternatif fonctionne comme prévu.

```python
# test_class_method.py
from stock import Stock

# Test the from_row() class method
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try with a different row
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

Pour voir les résultats, exécutez les commandes suivantes dans votre terminal :

```bash
cd ~/project
python test_class_method.py
```

Vous devriez voir une sortie similaire à ceci :

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

Notez que maintenant nous pouvons créer des instances de `Stock` directement à partir de données de chaîne de caractères sans avoir à effectuer manuellement des conversions de type en dehors de la classe. Cela rend notre code plus propre et assure que la responsabilité de la conversion des données est gérée au sein de la classe elle - même.
