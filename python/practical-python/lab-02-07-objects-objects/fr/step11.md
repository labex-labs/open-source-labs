# Exercice 2.24 : Données de première classe

Dans le fichier `portfolio.csv`, nous lisons des données organisées en colonnes qui ressemblent à ceci :

```csv
name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
```

Dans le code précédent, nous avons utilisé le module `csv` pour lire le fichier, mais avons encore dû effectuer des conversions de type manuellement. Par exemple :

```python
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Ce type de conversion peut également être effectué de manière plus astucieuse en utilisant certaines opérations de base de liste.

Créez une liste Python qui contient les noms des fonctions de conversion que vous utiliseriez pour convertir chaque colonne en son type approprié :

```python
>>> types = [str, int, float]
>>>
```

La raison pour laquelle vous pouvez même créer cette liste est que tout en Python est _de première classe_. Donc, si vous voulez avoir une liste de fonctions, c'est parfait. Les éléments de la liste que vous avez créé sont des fonctions pour convertir une valeur `x` en un type donné (par exemple, `str(x)`, `int(x)`, `float(x)`).

Maintenant, lisez une ligne de données à partir du fichier ci-dessus :

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> headers = next(rows)
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Comme indiqué, cette ligne n'est pas suffisante pour effectuer des calculs car les types sont incorrects. Par exemple :

```python
>>> row[1] * row[2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Cependant, peut-être que les données peuvent être associées aux types que vous avez spécifiés dans `types`. Par exemple :

```python
>>> types[1]
<type 'int'>
>>> row[1]
'100'
>>>
```

Essayez de convertir l'une des valeurs :

```python
>>> types[1](row[1])     # Identique à int(row[1])
100
>>>
```

Essayez de convertir une autre valeur :

```python
>>> types[2](row[2])     # Identique à float(row[2])
32.2
>>>
```

Essayez le calcul avec les valeurs converties :

```python
>>> types[1](row[1])*types[2](row[2])
3220.0000000000005
>>>
```

Associez les types de colonne aux champs et regardez le résultat :

```python
>>> r = list(zip(types, row))
>>> r
[(<type'str'>, 'AA'), (<type 'int'>, '100'), (<type 'float'>,'32.20')]
>>>
```

Vous remarquerez que cela a associé une conversion de type avec une valeur. Par exemple, `int` est associé à la valeur `'100'`.

La liste associée est utile si vous voulez effectuer des conversions sur toutes les valeurs, l'une après l'autre. Essayez ceci :

```python
>>> converted = []
>>> for func, val in zip(types, row):
          converted.append(func(val))
...
>>> converted
['AA', 100, 32.2]
>>> converted[1] * converted[2]
3220.0000000000005
>>>
```

Assurez-vous de comprendre ce qui se passe dans le code ci-dessus. Dans la boucle, la variable `func` est l'une des fonctions de conversion de type (par exemple, `str`, `int`, etc.) et la variable `val` est l'une des valeurs telles que `'AA'`, `'100'`. L'expression `func(val)` convertit une valeur (un peu comme un cast de type).

Le code ci-dessus peut être compressé en une seule compréhension de liste.

```python
>>> converted = [func(val) for func, val in zip(types, row)]
>>> converted
['AA', 100, 32.2]
>>>
```
