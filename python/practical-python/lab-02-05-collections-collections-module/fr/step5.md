# Exercice 2.18 : Tabulation avec des Compteurs

Supposons que vous vouliez tabuler le nombre total d'actions de chaque action. C'est facile à faire avec des objets `Counter`. Essayez :

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> from collections import Counter
>>> holdings = Counter()
>>> for s in portfolio:
        holdings[s['name']] += s['shares']

>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Observez attentivement comment les multiples entrées pour `MSFT` et `IBM` dans `portfolio` sont combinées en une seule entrée ici.

Vous pouvez utiliser un Compteur tout comme un dictionnaire pour récupérer des valeurs individuelles :

```python
>>> holdings['IBM']
150
>>> holdings['MSFT']
250
>>>
```

Si vous voulez classer les valeurs, faites ceci :

```python
>>> # Obtenez les trois actions les plus détenues
>>> holdings.most_common(3)
[('MSFT', 250), ('IBM', 150), ('CAT', 150)]
>>>
```

Prenons un autre portefeuille d'actions et créons un nouveau Compteur :

```python
>>> portfolio2 = read_portfolio('portfolio2.csv')
>>> holdings2 = Counter()
>>> for s in portfolio2:
          holdings2[s['name']] += s['shares']

>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>>
```

Enfin, combinons tous les portefeuilles en effectuant une simple opération :

```python
>>> holdings
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> holdings2
Counter({'HPQ': 250, 'GE': 125, 'AA': 50, 'MSFT': 25})
>>> combined = holdings + holdings2
>>> combined
Counter({'MSFT': 275, 'HPQ': 250, 'GE': 220, 'AA': 150, 'IBM': 150, 'CAT': 150})
>>>
```

Cela ne représente qu'un tout petit aperçu de ce que les Compteurs offrent. Cependant, si vous constatez que vous avez besoin de tabuler des valeurs, vous devriez envisager d'en utiliser un.
