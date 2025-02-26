# Compréhensions

Les compréhensions de listes, d'ensembles et de dictionnaires peuvent être un outil utile pour manipuler des données. Par exemple, essayez ces opérations :

```python
>>> # Trouvez toutes les positions de plus de 100 actions
>>> [s for s in portfolio if s['shares'] > 100]
[{'name': 'CAT','shares': 150, 'price': 83.44},
 {'name': 'MSFT','shares': 200, 'price': 51.23}]

>>> # Calculez le coût total (nombre d'actions * prix)
>>> sum([s['shares']*s['price'] for s in portfolio])
44671.15
>>>

>>> # Trouvez tous les noms d'action uniques (ensemble)
>>> { s['name'] for s in portfolio }
{'MSFT', 'IBM', 'AA', 'GE', 'CAT'}
>>>

>>> # Comptez le nombre total d'actions de chaque action
>>> totals = { s['name']: 0 for s in portfolio }
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
{'AA': 100, 'IBM': 150, 'CAT': 150, 'MSFT': 250, 'GE': 95}
>>>
```
