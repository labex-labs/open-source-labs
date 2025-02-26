# Préliminaires

Pour commencer, revenons sur quelques bases avec un ensemble de données un peu plus simple - un portefeuille d'actions. Créez un fichier `readport.py` et mettez ce code dedans :

```python
# readport.py

import csv

# Une fonction qui lit un fichier et le convertit en une liste de dictionnaires
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name' : row[0],
               'shares' : int(row[1]),
                'price' : float(row[2])
            }
            portfolio.append(record)
    return portfolio
```

Ce fichier lit des données simples sur le marché boursier dans le fichier `portfolio.csv`. Utilisez la fonction pour lire le fichier et regardez les résultats :

Ouvrez une invite Python et essayez ceci :

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> from pprint import pprint
>>> pprint(portfolio)
[{'name': 'AA', 'price': 32.2,'shares': 100},
 {'name': 'IBM', 'price': 91.1,'shares': 50},
 {'name': 'CAT', 'price': 83.44,'shares': 150},
 {'name': 'MSFT', 'price': 51.23,'shares': 200},
 {'name': 'GE', 'price': 40.37,'shares': 95},
 {'name': 'MSFT', 'price': 65.1,'shares': 50},
 {'name': 'IBM', 'price': 70.44,'shares': 100}]
>>>
```

Dans ces données, chaque ligne est composée d'un nom d'action, d'un nombre d'actions détenues et d'un prix d'achat. Il y a plusieurs entrées pour certains noms d'action tels que MSFT et IBM.
