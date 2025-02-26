# Exercice 2.22 : Extraction de données

Montrez comment vous pourriez construire une liste de tuples `(nom, nombre d'actions)` où `nom` et `nombre d'actions` sont extraits de `portfolio`.

```python
>>> name_shares =[ (s['name'], s['shares']) for s in portfolio ]
>>> name_shares
[('AA', 100), ('IBM', 50), ('CAT', 150), ('MSFT', 200), ('GE', 95), ('MSFT', 50), ('IBM', 100)]
>>>
```

Si vous changez les crochets (`[`, `]`) en accolades (`{`, `}`), vous obtenez ce qu'on appelle une compréhension de ensemble. Cela vous donne des valeurs uniques ou distinctes.

Par exemple, cela détermine l'ensemble des noms d'actions uniques qui apparaissent dans `portfolio` :

```python
>>> names = { s['name'] for s in portfolio }
>>> names
{ 'AA', 'GE', 'IBM', 'MSFT', 'CAT' }
>>>
```

Si vous spécifiez des paires `clé:valeur`, vous pouvez construire un dictionnaire. Par exemple, créez un dictionnaire qui associe le nom d'une action au nombre total d'actions détenues.

```python
>>> holdings = { name: 0 for name in names }
>>> holdings
{'AA': 0, 'GE': 0, 'IBM': 0, 'MSFT': 0, 'CAT': 0}
>>>
```

Cette dernière fonction est connue sous le nom de **compréhension de dictionnaire**. Tabulons :

```python
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
{ 'AA': 100, 'GE': 95, 'IBM': 150, 'MSFT':250, 'CAT': 150 }
>>>
```

Essayez cet exemple qui filtre le dictionnaire `prices` pour ne conserver que les noms qui apparaissent dans le portefeuille :

```python
>>> portfolio_prices = { name: prices[name] for name in names }
>>> portfolio_prices
{'AA': 9.22, 'GE': 13.48, 'IBM': 106.28, 'MSFT': 20.89, 'CAT': 35.46}
>>>
```
