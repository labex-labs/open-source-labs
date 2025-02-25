# Exercice 2.5 : Liste de dictionnaires

Prenez la fonction que vous avez écrite dans l'exercice 2.4 et modifiez-la pour représenter chaque action dans le portefeuille avec un dictionnaire au lieu d'un tuple. Dans ce dictionnaire, utilisez les noms de champs "name", "shares" et "price" pour représenter les différentes colonnes dans le fichier d'entrée.

Expérimentez cette nouvelle fonction de la même manière que vous l'avez fait dans l'exercice 2.4.

```python
>>> portfolio = read_portfolio('/home/labex/project/portfolio.csv')
>>> portfolio
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
    {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
    {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
    {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> portfolio[0]
{'name': 'AA','shares': 100, 'price': 32.2}
>>> portfolio[1]
{'name': 'IBM','shares': 50, 'price': 91.1}
>>> portfolio[1]['shares']
50
>>> total = 0.0
>>> for s in portfolio:
        total += s['shares']*s['price']

>>> print(total)
44671.15
>>>
```

Ici, vous remarquerez que les différents champs pour chaque entrée sont accessibles par des noms de clés au lieu de numéros de colonne numériques. Cela est souvent préférable car le code résultant est plus facile à lire plus tard.

La visualisation de grands dictionnaires et de listes peut être embrouillante. Pour nettoyer la sortie pour le débogage, considérez utiliser la fonction `pprint`.

```python
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
