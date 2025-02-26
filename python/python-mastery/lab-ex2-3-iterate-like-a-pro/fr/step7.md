# Économiser beaucoup de mémoire

Dans l'exercice 2.1, vous avez écrit une fonction `read_rides_as_dicts()` qui lisait les données du bus CTA dans une liste de dictionnaires. L'utilisation de cette fonction nécessite beaucoup de mémoire. Par exemple, cherchons le jour où le bus de la ligne 22 a eu le plus de passagers :

```python
>>> import tracemalloc
>>> tracemalloc.start()
>>> import readrides
>>> rows = readrides.read_rides_as_dicts('ctabus.csv')
>>> rt22 = [row for row in rows if row['route'] == '22']
>>> max(rt22, key=lambda row: row['rides'])
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... regardez le résultat. Cela devrait être d'environ 220 Mo
>>>
```

Maintenant, essayons un exemple impliquant des générateurs. Redémarrez Python et essayez ceci :

```python
>>> # RESTART
>>> import tracemalloc
>>> tracemalloc.start()
>>> import csv
>>> f = open('ctabus.csv')
>>> f_csv = csv.reader(f)
>>> headers = next(f_csv)
>>> rows = (dict(zip(headers,row)) for row in f_csv)
>>> rt22 = (row for row in rows if row['route'] == '22')
>>> max(rt22, key=lambda row: int(row['rides']))
{'date': '06/11/2008', 'route': '22', 'daytype': 'W', 'rides': 26896}
>>> tracemalloc.get_traced_memory()
... regardez le résultat. Cela devrait être beaucoup plus petit que précédemment
>>>
```

Gardez à l'esprit que vous venez de traiter l'ensemble du jeu de données comme s'il était stocké sous forme de séquence de dictionnaires. Pourtant, vous n'avez nulle part créé et stocké réellement une liste de dictionnaires. Pas tous les problèmes peuvent être structurés de cette manière, mais si vous pouvez travailler avec les données de manière itérative, les expressions génératrices peuvent économiser une quantité énorme de mémoire.
