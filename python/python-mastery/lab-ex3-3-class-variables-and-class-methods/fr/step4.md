# Création d'un lecteur CSV polyvalent

Dans cette étape finale, nous allons créer une fonction polyvalente. Cette fonction sera capable de lire des fichiers CSV et de créer des objets de n'importe quelle classe qui a implémenté la méthode de classe `from_row()`. Cela montre la puissance de l'utilisation des méthodes de classe comme interface uniforme. Une interface uniforme signifie que différentes classes peuvent être utilisées de la même manière, ce qui rend notre code plus flexible et plus facile à gérer.

## Modification de la fonction read_portfolio()

Tout d'abord, nous allons mettre à jour la fonction `read_portfolio()` dans le fichier `stock.py`. Nous utiliserons notre nouvelle méthode de classe `from_row()`. Ouvrez le fichier `stock.py` et modifiez la fonction `read_portfolio()` comme ceci :

```python
def read_portfolio(filename):
    '''
    Read a stock portfolio file into a list of Stock instances
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            portfolio.append(Stock.from_row(row))
    return portfolio
```

Cette nouvelle version de la fonction est plus simple. Elle confie la responsabilité de la conversion de type à la classe `Stock`, là où elle appartient vraiment. La conversion de type consiste à changer les données d'un type à un autre, comme transformer une chaîne de caractères en entier. En faisant cela, nous rendons notre code plus organisé et plus facile à comprendre.

## Création d'un lecteur CSV polyvalent

Maintenant, nous allons créer une fonction plus polyvalente dans le fichier `reader.py`. Cette fonction peut lire des données CSV et créer des instances de n'importe quelle classe qui a une méthode de classe `from_row()`.

Ouvrez le fichier `reader.py` et ajoutez la fonction suivante :

```python
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances of the given class.

    Args:
        filename: Name of the CSV file
        cls: Class to instantiate (must have from_row class method)

    Returns:
        List of class instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Skip header
        for row in rows:
            records.append(cls.from_row(row))
    return records
```

Cette fonction prend deux entrées : un nom de fichier et une classe. Elle retourne ensuite une liste d'instances de cette classe, créées à partir des données du fichier CSV. Cela est très utile car nous pouvons l'utiliser avec différentes classes, tant qu'elles ont la méthode `from_row()`.

## Test du lecteur CSV polyvalent

Créons un fichier de test pour voir comment fonctionne notre lecteur polyvalent. Créez un fichier nommé `test_csv_reader.py` avec le contenu suivant :

```python
# test_csv_reader.py
from reader import read_csv_as_instances
from stock import Stock
from decimal_stock import DStock

# Read portfolio as Stock instances
portfolio = read_csv_as_instances('portfolio.csv', Stock)
print(f"Portfolio contains {len(portfolio)} stocks")
print(f"First stock: {portfolio[0].name}, {portfolio[0].shares} shares at ${portfolio[0].price}")

# Read portfolio as DStock instances (with Decimal prices)
decimal_portfolio = read_csv_as_instances('portfolio.csv', DStock)
print(f"\nDecimal portfolio contains {len(decimal_portfolio)} stocks")
print(f"First stock: {decimal_portfolio[0].name}, {decimal_portfolio[0].shares} shares at ${decimal_portfolio[0].price}")

# Define a new class for reading the bus data
class BusRide:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))

# Read some bus data (just the first 5 records for brevity)
print("\nReading bus data...")
import csv
with open('ctabus.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip header
    bus_rides = []
    for i, row in enumerate(rows):
        if i >= 5:  # Only read 5 records for the example
            break
        bus_rides.append(BusRide.from_row(row))

# Display the bus data
for ride in bus_rides:
    print(f"Route: {ride.route}, Date: {ride.date}, Type: {ride.daytype}, Rides: {ride.rides}")
```

Exécutez ce fichier pour voir les résultats. Ouvrez votre terminal et utilisez les commandes suivantes :

```bash
cd ~/project
python test_csv_reader.py
```

Vous devriez voir une sortie qui montre les données du portefeuille chargées sous forme d'instances `Stock` et `DStock`, ainsi que les données des itinéraires de bus chargées sous forme d'instances `BusRide`. Cela prouve que notre lecteur polyvalent fonctionne avec différentes classes.

## Principaux avantages de cette approche

Cette approche montre plusieurs concepts puissants :

1. **Séparation des préoccupations** : La lecture des données est séparée de la création des objets. Cela signifie que le code pour lire le fichier CSV n'est pas mélangé avec le code pour créer les objets. Cela rend le code plus facile à comprendre et à maintenir.
2. **Polymorphisme** : Le même code peut fonctionner avec différentes classes qui suivent la même interface. Dans notre cas, tant qu'une classe a la méthode `from_row()`, notre lecteur polyvalent peut l'utiliser.
3. **Flexibilité** : Nous pouvons facilement changer la façon dont les données sont converties en utilisant différentes classes. Par exemple, nous pouvons utiliser `Stock` ou `DStock` pour gérer les données du portefeuille différemment.
4. **Extensibilité** : Nous pouvons ajouter de nouvelles classes qui fonctionnent avec notre lecteur sans modifier le code du lecteur. Cela rend notre code plus durable.

C'est un modèle courant en Python qui rend le code plus modulaire, réutilisable et maintenable.

## Remarques finales sur les méthodes de classe

Les méthodes de classe sont souvent utilisées comme constructeurs alternatifs en Python. Vous pouvez généralement les reconnaître car leurs noms contiennent souvent le mot "from". Par exemple :

```python
# Some examples from Python's built-in types
dict.fromkeys(['a', 'b', 'c'], 0)  # Create a dict with default values
datetime.datetime.fromtimestamp(1627776000)  # Create datetime from timestamp
int.from_bytes(b'\x00\x01', byteorder='big')  # Create int from bytes
```

En suivant cette convention, vous rendez votre code plus lisible et cohérent avec les bibliothèques intégrées de Python. Cela aide les autres développeurs à comprendre votre code plus facilement.
