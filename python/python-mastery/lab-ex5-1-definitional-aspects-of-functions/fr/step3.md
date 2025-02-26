# Penser à la flexibilité

En ce moment, les deux fonctions dans `reader.py` sont codées en dur pour fonctionner avec des noms de fichiers qui sont passés directement à `open()`. Refactorisez le code de sorte qu'il fonctionne avec n'importe quel objet itérable qui produit des lignes. Pour ce faire, créez deux nouvelles fonctions `csv_as_dicts(lignes, types)` et `csv_as_instances(lignes, cls)` qui convertissent n'importe quelle séquence itérable de lignes. Par exemple :

```python
>>> file = open('portfolio.csv')
>>> port = reader.csv_as_dicts(file, [str, int, float])
>>> port
[{'name': 'AA','shares': 100, 'price': 32.2}, {'name': 'IBM','shares': 50, 'price': 91.1},
 {'name': 'CAT','shares': 150, 'price': 83.44}, {'name': 'MSFT','shares': 200, 'price': 51.23},
 {'name': 'GE','shares': 95, 'price': 40.37}, {'name': 'MSFT','shares': 50, 'price': 65.1},
 {'name': 'IBM','shares': 100, 'price': 70.44}]
>>>
```

Le tout est de rendre possible le travail avec différents types de sources d'entrée. Par exemple :

```python
>>> import gzip
>>> import stock
>>> file = gzip.open('portfolio.csv.gz')
>>> port = reader.csv_as_instances(file, stock.Stock)
>>> port
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44),
 Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1),
 Stock('IBM', 100, 70.44)]
>>>
```

Pour maintenir la compatibilité descendante avec le code ancien, écrivez les fonctions `read_csv_as_dicts()` et `read_csv_as_instances()` qui prennent un nom de fichier comme avant. Ces fonctions devraient appeler `open()` sur le nom de fichier fourni et utiliser les nouvelles fonctions `csv_as_dicts()` ou `csv_as_instances()` sur le fichier résultant.
