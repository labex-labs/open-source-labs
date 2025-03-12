# Comprendre les variables de classe et les méthodes de classe

Dans cette première étape, nous allons plonger dans les concepts de variables de classe et de méthodes de classe en Python. Ce sont des concepts importants qui vous aideront à écrire un code plus efficace et mieux organisé. Avant de commencer à travailler avec les variables de classe et les méthodes de classe, regardons d'abord comment les instances de notre classe `Stock` sont actuellement créées. Cela nous donnera une compréhension de base et nous montrera où nous pouvons apporter des améliorations.

## Quelles sont les variables de classe ?

Les variables de classe sont un type spécial de variables en Python. Elles sont partagées entre toutes les instances d'une classe. Pour mieux comprendre cela, comparons-les avec les variables d'instance. Les variables d'instance sont uniques à chaque instance d'une classe. Par exemple, si vous avez plusieurs instances d'une classe, chaque instance peut avoir sa propre valeur pour une variable d'instance. En revanche, les variables de classe sont définies au niveau de la classe. Cela signifie que toutes les instances de cette classe peuvent accéder et partager la même valeur de la variable de classe.

## Quelles sont les méthodes de classe ?

Les méthodes de classe sont des méthodes qui opèrent sur la classe elle-même, et non sur les instances individuelles de la classe. Elles sont liées à la classe, ce qui signifie qu'elles peuvent être appelées directement sur la classe sans créer d'instance. Pour définir une méthode de classe en Python, nous utilisons le décorateur `@classmethod`. Et au lieu de prendre l'instance (`self`) comme premier paramètre, les méthodes de classe prennent la classe (`cls`) comme premier paramètre. Cela leur permet d'opérer sur les données au niveau de la classe et d'effectuer des actions liées à la classe dans son ensemble.

## Approche actuelle de la création d'instances de Stock

Voyons d'abord comment nous créons actuellement des instances de la classe `Stock`. Ouvrez le fichier `stock.py` dans l'éditeur pour observer l'implémentation actuelle :

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

Les instances de cette classe sont généralement créées de l'une des manières suivantes :

1. Initialisation directe avec des valeurs :

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

   Ici, nous créons directement une instance de la classe `Stock` en fournissant les valeurs pour les attributs `name`, `shares` et `price`. C'est un moyen simple de créer une instance lorsque vous connaissez les valeurs à l'avance.

2. Création à partir de données lues dans un fichier CSV :
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   Lorsque nous lisons des données dans un fichier CSV, les valeurs sont initialement au format chaîne de caractères. Donc, lorsque nous créons une instance de `Stock` à partir de données CSV, nous devons convertir manuellement les valeurs de chaîne en types appropriés. Par exemple, la valeur de `shares` doit être convertie en entier, et la valeur de `price` doit être convertie en nombre à virgule flottante.

Essayons cela. Créez un nouveau fichier Python appelé `test_stock.py` dans le répertoire `~/project` avec le contenu suivant :

```python
# test_stock.py
from stock import Stock
import csv

# Méthode 1 : Création directe
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Méthode 2 : Création à partir d'une ligne CSV
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header
    row = next(rows)      # Get the first data row
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

Exécutez ce fichier pour voir les résultats :

```bash
cd ~/project
python test_stock.py
```

Vous devriez voir une sortie similaire à :

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

Cette conversion manuelle fonctionne, mais elle présente certains inconvénients. Nous devons connaître le format exact des données, et nous devons effectuer les conversions chaque fois que nous créons une instance à partir de données CSV. Cela peut être source d'erreurs et chronophage. Dans l'étape suivante, nous allons créer une solution plus élégante en utilisant des méthodes de classe.
