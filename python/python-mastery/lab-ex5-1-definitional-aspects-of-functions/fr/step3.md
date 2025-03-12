# Rendre les fonctions plus flexibles

Actuellement, nos fonctions sont limitées à la lecture de fichiers spécifiés par un nom de fichier. Cela restreint leur utilisabilité. En programmation, il est souvent avantageux de rendre les fonctions plus flexibles afin qu'elles puissent gérer différents types d'entrée. Dans notre cas, il serait idéal que nos fonctions puissent fonctionner avec n'importe quel itérable qui produit des lignes, comme des objets de fichier ou d'autres sources. De cette façon, nous pouvons utiliser ces fonctions dans plus de scénarios, comme la lecture de fichiers compressés ou d'autres flux de données.

Refactorisons notre code pour permettre cette flexibilité :

1. Ouvrez le fichier `reader.py`. Nous allons le modifier pour inclure de nouvelles fonctions. Ces nouvelles fonctions permettront à notre code de fonctionner avec différents types d'itérateurs. Voici le code à ajouter :

```python
# reader.py

import csv

def csv_as_dicts(lines, types):
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines, cls):
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV lines
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename, types):
    '''
    Read CSV data into a list of dictionaries with optional type conversion

    Args:
        filename: Path to the CSV file
        types: List of type conversion functions for each column

    Returns:
        List of dictionaries with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types)

def read_csv_as_instances(filename, cls):
    '''
    Read CSV data into a list of class instances

    Args:
        filename: Path to the CSV file
        cls: Class to create instances from

    Returns:
        List of class instances with data from the CSV file
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls)
```

Examinons de plus près comment nous avons refactorisé le code :

1. Nous avons créé deux fonctions plus génériques, `csv_as_dicts()` et `csv_as_instances()`. Ces fonctions sont conçues pour fonctionner avec n'importe quel itérable qui produit des lignes CSV. Cela signifie qu'elles peuvent gérer différents types de sources d'entrée, pas seulement des fichiers spécifiés par un nom de fichier.
2. Nous avons réimplémenté `read_csv_as_dicts()` et `read_csv_as_instances()` pour utiliser ces nouvelles fonctions. De cette façon, la fonctionnalité originale de lecture à partir d'un fichier par nom de fichier est toujours disponible, mais maintenant elle est construite sur des fonctions plus flexibles.
3. Cette approche maintient la compatibilité rétroactive avec le code existant. Cela signifie que tout code utilisant les anciennes fonctions continuera de fonctionner comme prévu. En même temps, notre bibliothèque devient plus flexible car elle peut maintenant gérer différents types de sources d'entrée.

4. Maintenant, testons ces nouvelles fonctions. Créez un fichier appelé `test_reader_flexibility.py` et ajoutez le code suivant. Ce code testera les nouvelles fonctions avec différents types de sources d'entrée :

```python
# test_reader_flexibility.py

import reader
import stock
import gzip

# Test opening a regular file
with open('portfolio.csv') as file:
    portfolio = reader.csv_as_dicts(file, [str, int, float])
    print("First item from open file:", portfolio[0])

# Test opening a gzipped file
with gzip.open('portfolio.csv.gz', 'rt') as file:  # 'rt' means read text
    portfolio = reader.csv_as_instances(file, stock.Stock)
    print("\nFirst item from gzipped file:", portfolio[0])

# Test backward compatibility
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("\nFirst item using backward compatible function:", portfolio[0])
```

3. Après avoir créé le fichier de test, nous devons exécuter le script de test depuis le terminal. Ouvrez votre terminal et naviguez jusqu'au répertoire où se trouve le fichier `test_reader_flexibility.py`. Ensuite, exécutez la commande suivante :

```bash
python test_reader_flexibility.py
```

La sortie devrait ressembler à ceci :

```
First item from open file: {'name': 'AA', 'shares': 100, 'price': 32.2}

First item from gzipped file: Stock('AA', 100, 32.2)

First item using backward compatible function: {'name': 'AA', 'shares': 100, 'price': 32.2}
```

Cette sortie confirme que nos fonctions fonctionnent maintenant avec différents types de sources d'entrée tout en maintenant la compatibilité rétroactive. Les fonctions refactorisées peuvent traiter des données provenant de :

- Des fichiers normaux ouverts avec `open()`
- Des fichiers compressés ouverts avec `gzip.open()`
- N'importe quel autre objet itérable qui produit des lignes de texte

Cela rend notre code beaucoup plus flexible et plus facile à utiliser dans différents scénarios.
