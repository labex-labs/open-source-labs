# Gestion des fichiers CSV sans en-têtes

Dans le domaine du traitement des données, tous les fichiers CSV ne comportent pas d'en-têtes dans leur première ligne. Les en-têtes sont les noms donnés à chaque colonne d'un fichier CSV, ce qui nous aide à comprendre le type de données que chaque colonne contient. Lorsqu'un fichier CSV n'a pas d'en-têtes, nous devons trouver un moyen de le gérer correctement. Dans cette section, nous allons modifier nos fonctions pour permettre à l'appelant de fournir manuellement les en-têtes, afin que nous puissions travailler avec des fichiers CSV avec et sans en-têtes.

1. Ouvrez le fichier `reader.py` et mettez-le à jour pour inclure la gestion des en-têtes :

```python
# reader.py

import csv

def csv_as_dicts(lines, types, headers=None):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls, headers=None):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers)

def read_csv_as_instances(filename, cls, headers=None):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers)
```

Comprenons les principales modifications que nous avons apportées à ces fonctions :

1. Nous avons ajouté un paramètre `headers` à toutes les fonctions et nous l'avons défini par défaut sur `None`. Cela signifie que si l'appelant ne fournit pas d'en-têtes, les fonctions utiliseront le comportement par défaut.
2. Dans la fonction `csv_as_dicts`, nous utilisons la première ligne comme en-têtes seulement si le paramètre `headers` est `None`. Cela nous permet de gérer automatiquement les fichiers avec en-têtes.
3. Dans la fonction `csv_as_instances`, nous sautons la première ligne seulement si le paramètre `headers` est `None`. En effet, si nous fournissons nos propres en-têtes, la première ligne du fichier contient des données réelles, pas des en-têtes.

4. Testons ces modifications avec notre fichier sans en-têtes. Créez un fichier appelé `test_headers.py` :

```python
# test_headers.py

import reader
import stock

# Define column names for the file without headers
column_names = ['name', 'shares', 'price']

# Test reading a file without headers
portfolio = reader.read_csv_as_dicts('portfolio_noheader.csv',
                                     [str, int, float],
                                     headers=column_names)
print("First item from file without headers:", portfolio[0])
print("Total items:", len(portfolio))

# Test reading the same file as instances
portfolio = reader.read_csv_as_instances('portfolio_noheader.csv',
                                        stock.Stock,
                                        headers=column_names)
print("\nFirst item as Stock instance:", portfolio[0])
print("Total items:", len(portfolio))

# Verify that original functionality still works
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item from file with headers:", portfolio[0])
```

Dans ce script de test, nous définissons d'abord les noms de colonne pour le fichier sans en-têtes. Ensuite, nous testons la lecture du fichier sans en-têtes sous forme de liste de dictionnaires et de liste d'instances de classe. Enfin, nous vérifions que la fonctionnalité originale fonctionne toujours en lisant un fichier avec en-têtes.

3. Exécutez le script de test depuis le terminal :

```bash
python test_headers.py
```

La sortie devrait ressembler à :

```
First item from file without headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
Total items: 7

First item as Stock instance: Stock('AA', 100, 32.2)
Total items: 7

First item from file with headers: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Cette sortie confirme que nos fonctions peuvent maintenant gérer les fichiers CSV avec et sans en-têtes. L'utilisateur peut fournir les noms de colonne si nécessaire, ou s'appuyer sur le comportement par défaut de lecture des en-têtes à partir de la première ligne.

En effectuant cette modification, nos fonctions de lecture de fichiers CSV sont maintenant plus polyvalentes et peuvent gérer une plus large gamme de formats de fichiers. C'est une étape importante pour rendre notre code plus robuste et utile dans différents scénarios.
