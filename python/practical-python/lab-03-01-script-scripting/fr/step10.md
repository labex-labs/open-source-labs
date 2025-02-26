# Annotations de type

Vous pouvez également ajouter des indications de type optionnelles aux définitions de fonctions.

```python
def read_prices(filename: str) -> dict:
    '''
    Lire les prix à partir d'un fichier CSV contenant des données nom,prix
    '''
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
```

Les indications ne font rien sur le plan opérationnel. Elles sont purement informatives. Cependant, elles peuvent être utilisées par les IDE, les vérificateurs de code et d'autres outils pour faire plus.

Dans la section 2, vous avez écrit un programme appelé `report.py` qui affichait un rapport montrant les performances d'un portefeuille d'actions. Ce programme était composé de quelques fonctions. Par exemple :

```python
# report.py
import csv

def read_portfolio(filename):
    '''
    Lire un fichier de portefeuille d'actions dans une liste de dictionnaires avec les clés
    name, shares et price.
    '''
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            record = dict(zip(headers, row))
            stock = {
                'name' : record['name'],
               'shares' : int(record['shares']),
                'price' : float(record['price'])
            }
            portfolio.append(stock)
    return portfolio
...
```

Cependant, il y avait également des parties du programme qui ne faisaient que effectuer une série de calculs scriptés. Ce code apparaissait vers la fin du programme. Par exemple :

```python
...

# Afficher le rapport

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s'  % headers)
print(('-' * 10 +'') * len(headers))
for row in report:
    print('%10s %10d %10.2f %10.2f' % row)
...
```

Dans cet exercice, nous allons prendre ce programme et l'organiser un peu plus solidement autour de l'utilisation des fonctions.
