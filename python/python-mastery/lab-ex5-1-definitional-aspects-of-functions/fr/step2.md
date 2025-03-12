# Création des fonctions de base pour la lecture de fichiers CSV

Commençons par créer un fichier `reader.py` avec deux fonctions de base pour lire des données CSV. Ces fonctions nous aideront à manipuler les fichiers CSV de différentes manières, comme convertir les données en dictionnaires ou en instances de classe.

Tout d'abord, nous devons comprendre ce qu'est un fichier CSV. CSV signifie Comma-Separated Values (Valeurs séparées par des virgules). C'est un format de fichier simple utilisé pour stocker des données tabulaires, où chaque ligne représente une ligne du tableau et les valeurs de chaque ligne sont séparées par des virgules.

Maintenant, créons le fichier `reader.py`. Suivez ces étapes :

1. Ouvrez l'éditeur de code et créez un nouveau fichier appelé `reader.py` dans le répertoire `/home/labex/project`. C'est là que nous allons écrire nos fonctions pour lire les données CSV.

2. Ajoutez le code suivant à `reader.py` :

```python
# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = { name: func(val)
                       for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    records = []
    with open(filename) as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = cls.from_row(row)
            records.append(record)
    return records
```

Dans la fonction `read_csv_as_dicts`, nous ouvrons d'abord le fichier CSV à l'aide de la fonction `open`. Ensuite, nous utilisons `csv.reader` pour lire le fichier ligne par ligne. L'instruction `next(rows)` lit la première ligne du fichier, qui contient généralement les en-têtes. Après cela, nous itérons sur les lignes restantes. Pour chaque ligne, nous créons un dictionnaire où les clés sont les en-têtes et les valeurs sont les valeurs correspondantes de la ligne, avec une conversion de type facultative à l'aide de la liste `types`.

La fonction `read_csv_as_instances` est similaire, mais au lieu de créer des dictionnaires, elle crée des instances d'une classe donnée. Elle suppose que la classe a une méthode statique appelée `from_row` qui peut créer une instance à partir d'une ligne de données.

3. Testons ces fonctions pour nous assurer qu'elles fonctionnent correctement. Créez un nouveau fichier appelé `test_reader.py` avec le code suivant :

```python
# test_reader.py

import reader
import stock

# Test reading CSV as dictionaries
portfolio_dicts = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First portfolio item as dictionary:", portfolio_dicts[0])
print("Total items:", len(portfolio_dicts))

# Test reading CSV as class instances
portfolio_instances = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst portfolio item as Stock instance:", portfolio_instances[0])
print("Total items:", len(portfolio_instances))
```

Dans le fichier `test_reader.py`, nous importons le module `reader` que nous venons de créer et le module `stock`. Nous testons ensuite les deux fonctions en les appelant avec un fichier CSV d'exemple nommé `portfolio.csv`. Nous affichons le premier élément et le nombre total d'éléments du portefeuille pour vérifier que les fonctions fonctionnent comme prévu.

4. Exécutez le script de test depuis le terminal :

```bash
python test_reader.py
```

La sortie devrait ressembler à ceci :

```
First portfolio item as dictionary: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First portfolio item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7
```

Cela confirme que nos deux fonctions fonctionnent correctement. La première fonction convertit les données CSV en une liste de dictionnaires avec une conversion de type appropriée, et la deuxième fonction crée des instances de classe à l'aide d'une méthode statique de la classe fournie.

Dans l'étape suivante, nous allons refactoriser ces fonctions pour les rendre plus flexibles en leur permettant de fonctionner avec n'importe quelle source de données itérable, pas seulement des noms de fichiers.
