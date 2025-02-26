# Collections

Le module `collections` a diverses classes pour une manipulation de données plus spécialisée. Par exemple, le dernier exemple pourrait être résolu avec un `Counter` comme ceci :

```python
>>> from collections import Counter
>>> totals = Counter()
>>> for s in portfolio:
        totals[s['name']] += s['shares']

>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>>
```

Les `Counter` sont intéressants car ils prennent en charge d'autres types d'opérations telles que le classement et les mathématiques. Par exemple :

```python
>>> # Obtenez les deux actions les plus courantes
>>> totals.most_common(2)
[('MSFT', 250), ('IBM', 150)]
>>>

>>> # Ajoutez deux compteurs ensemble
>>> more = Counter()
>>> more['IBM'] = 75
>>> more['AA'] = 200
>>> more['ACME'] = 30
>>> more
Counter({'AA': 200, 'IBM': 75, 'ACME': 30})
>>> totals
Counter({'MSFT': 250, 'IBM': 150, 'CAT': 150, 'AA': 100, 'GE': 95})
>>> totals + more
Counter({'AA': 300, 'MSFT': 250, 'IBM': 225, 'CAT': 150, 'GE': 95, 'ACME': 30})
>>>
```

L'objet `defaultdict` peut être utilisé pour regrouper des données. Par exemple, supposons que vous vouliez faciliter la recherche de toutes les entrées correspondantes pour un nom donné tel que IBM. Essayez ceci :

```python
>>> from collections import defaultdict
>>> byname = defaultdict(list)
>>> for s in portfolio:
        byname[s['name']].append(s)

>>> byname['IBM']
[{'name': 'IBM','shares': 50, 'price': 91.1}, {'name': 'IBM','shares': 100, 'price': 70.44}]
>>> byname['AA']
[{'name': 'AA','shares': 100, 'price': 32.2}]
>>>
```

La caractéristique clé qui permet ce fonctionnement est que `defaultdict` initialise automatiquement les éléments pour vous, ce qui permet de combiner l'insertion d'un nouvel élément et une opération `append()`.
