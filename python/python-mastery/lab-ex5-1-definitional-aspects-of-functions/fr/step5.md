# Ajout d'indications de type

Dans Python 3.5 et les versions ultérieures, les indications de type (type hints) sont prises en charge. Les indications de type sont un moyen d'indiquer les types de données attendus pour les variables, les paramètres de fonction et les valeurs de retour dans votre code. Elles ne changent pas le fonctionnement du code, mais elles le rendent plus lisible et peuvent aider à détecter certains types d'erreurs avant l'exécution effective du code. Maintenant, ajoutons des indications de type à nos fonctions de lecture de fichiers CSV.

1. Ouvrez le fichier `reader.py` et mettez-le à jour pour inclure les indications de type :

```python
# reader.py

import csv
from typing import List, Callable, Dict, Any, Type, Optional, TextIO, Iterator, TypeVar

# Define a generic type for the class parameter
T = TypeVar('T')

def csv_as_dicts(lines: Iterator[str],
                types: List[Callable[[str], Any]],
                headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    '''
    Parse CSV data from an iterable into a list of dictionaries

    Args:
        lines: An iterable producing CSV lines
        types: List of type conversion functions for each column
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of dictionaries with data from the CSV lines
    '''
    records: List[Dict[str, Any]] = []
    rows = csv.reader(lines)

    if headers is None:
        # Use the first row as headers if none provided
        headers = next(rows)

    for row in rows:
        record = { name: func(val)
                  for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records

def csv_as_instances(lines: Iterator[str],
                    cls: Type[T],
                    headers: Optional[List[str]] = None) -> List[T]:
    '''
    Parse CSV data from an iterable into a list of class instances

    Args:
        lines: An iterable producing CSV lines
        cls: Class to create instances from
        headers: Optional list of column names. If None, first row is used as headers

    Returns:
        List of class instances with data from the CSV lines
    '''
    records: List[T] = []
    rows = csv.reader(lines)

    if headers is None:
        # Skip the first row if no headers provided
        next(rows)

    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

def read_csv_as_dicts(filename: str,
                     types: List[Callable[[str], Any]],
                     headers: Optional[List[str]] = None) -> List[Dict[str, Any]]:
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

def read_csv_as_instances(filename: str,
                         cls: Type[T],
                         headers: Optional[List[str]] = None) -> List[T]:
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

Comprenons les principales modifications que nous avons apportées au code :

1. Nous avons importé des types du module `typing`. Ce module fournit un ensemble de types que nous pouvons utiliser pour définir des indications de type. Par exemple, `List`, `Dict` et `Optional` sont des types de ce module.
2. Nous avons ajouté une variable de type générique `T` pour représenter le type de classe. Une variable de type générique nous permet d'écrire des fonctions qui peuvent fonctionner avec différents types de manière sûre en termes de types.
3. Nous avons ajouté des indications de type à tous les paramètres de fonction et aux valeurs de retour. Cela rend clair quels types d'arguments une fonction attend et quel type de valeur elle retourne.
4. Nous avons utilisé des types de conteneurs appropriés tels que `List`, `Dict` et `Optional`. `List` représente une liste, `Dict` représente un dictionnaire et `Optional` indique qu'un paramètre peut avoir un certain type ou être `None`.
5. Nous avons utilisé `Callable` pour les fonctions de conversion de type. `Callable` est utilisé pour indiquer qu'un paramètre est une fonction qui peut être appelée.
6. Nous avons utilisé le type générique `T` pour indiquer que `csv_as_instances` retourne une liste d'instances de la classe passée en paramètre. Cela aide l'IDE et d'autres outils à comprendre le type des objets retournés.

7. Maintenant, créons un simple fichier de test pour nous assurer que tout fonctionne toujours correctement :

```python
# test_types.py

import reader
import stock

# The functions should work exactly as before
portfolio = reader.read_csv_as_dicts('portfolio.csv', [str, int, float])
print("First item:", portfolio[0])

# But now we have better type checking and IDE support
stock_portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
print("\nFirst stock:", stock_portfolio[0])

# We can see that stock_portfolio is a list of Stock objects
# This helps IDEs provide better code completion
first_stock = stock_portfolio[0]
print(f"\nName: {first_stock.name}")
print(f"Shares: {first_stock.shares}")
print(f"Price: {first_stock.price}")
print(f"Value: {first_stock.shares * first_stock.price}")
```

3. Exécutez le script de test depuis le terminal :

```bash
python test_types.py
```

La sortie devrait ressembler à :

```
First item: {'name': 'AA', 'shares': 100, 'price': 32.2}

First stock: Stock('AA', 100, 32.2)

Name: AA
Shares: 100
Price: 32.2
Value: 3220.0
```

Les indications de type ne changent pas le fonctionnement du code, mais elles offrent plusieurs avantages :

1. Elles offrent un meilleur support de l'IDE avec l'autocomplétion du code. Lorsque vous utilisez un IDE comme PyCharm ou VS Code, il peut utiliser les indications de type pour suggérer les méthodes et les attributs corrects pour vos variables.
2. Elles fournissent une documentation plus claire sur les types de paramètres et de valeurs de retour attendus. En regardant simplement la définition de la fonction, vous pouvez savoir quels types d'arguments elle attend et quel type de valeur elle retourne.
3. Elles vous permettent d'utiliser des vérificateurs de types statiques comme mypy pour détecter les erreurs tôt. Les vérificateurs de types statiques analysent votre code sans l'exécuter et peuvent trouver des erreurs liées aux types avant d'exécuter le code.
4. Elles améliorent la lisibilité et la maintenabilité du code. Lorsque vous ou d'autres développeurs reviendrez sur le code plus tard, il sera plus facile de comprendre ce que le code fait.

Dans une base de code importante, ces avantages peuvent réduire considérablement les bugs et rendre le code plus facile à comprendre et à maintenir.

**Remarque :** Les indications de type sont facultatives en Python, mais elles sont de plus en plus utilisées dans le code professionnel. Des bibliothèques telles que celles de la bibliothèque standard de Python et de nombreux packages tiers populaires incluent désormais de nombreuses indications de type.
