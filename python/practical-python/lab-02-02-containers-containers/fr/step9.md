# Exercice 2.4 : Une liste de tuples

Le fichier `portfolio.csv` contient une liste d'actions dans un portefeuille. Dans l'exercice 1.30, vous avez écrit une fonction `portfolio_cost(filename)` qui lisait ce fichier et effectuait un calcul simple.

Votre code aurait dû ressembler à ceci :

```python
# pcost.py

import csv

def portfolio_cost(filename):
    '''Calcule le coût total (nombre d'actions * prix) d'un fichier de portefeuille'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost
```

En utilisant ce code comme guide, créez un nouveau fichier `report.py`. Dans ce fichier, définissez une fonction `read_portfolio(filename)` qui ouvre un fichier de portefeuille donné et le lit dans une liste de tuples. Pour ce faire, vous allez apporter quelques modifications mineures au code ci-dessus.

Tout d'abord, au lieu de définir `total_cost = 0`, vous allez créer une variable initialement définie comme une liste vide. Par exemple :

```python
portfolio = []
```

Ensuite, au lieu de additionner le coût, vous allez transformer chaque ligne en tuple exactement comme vous l'avez fait dans l'exercice précédent et l'ajouter à cette liste. Par exemple :

```python
for row in rows:
    holding = (row[0], int(row[1]), float(row[2]))
    portfolio.append(holding)
```

Enfin, vous retournerez la liste `portfolio` résultante.

Expérimentez votre fonction de manière interactive (un rappel : pour ce faire, vous devez d'abord exécuter le programme `report.py` dans l'interpréteur) :

_Indice : Utilisez `-i` lors de l'exécution du fichier dans le terminal_

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[('AA', 100, 32.2), ('IBM', 50, 91.1), ('CAT', 150, 83.44), ('MSFT', 200, 51.23),
    ('GE', 95, 40.37), ('MSFT', 50, 65.1), ('IBM', 100, 70.44)]
>>>
>>> portfolio[0]
('AA', 100, 32.2)
>>> portfolio[1]
('IBM', 50, 91.1)
>>> portfolio[1][1]
50
>>> total = 0.0
>>> for s in portfolio:
        total += s[1] * s[2]

>>> print(total)
44671.15
>>>
```

Cette liste de tuples que vous avez créée est très similaire à un tableau 2D. Par exemple, vous pouvez accéder à une colonne et une ligne spécifiques en utilisant une recherche telle que `portfolio[row][column]` où `row` et `column` sont des entiers.

Cela étant dit, vous pouvez également réécrire la dernière boucle `for` en utilisant une instruction comme celle-ci :

```python
>>> total = 0.0
>>> for name, shares, price in portfolio:
            total += shares*price

>>> print(total)
44671.15
>>>
```
