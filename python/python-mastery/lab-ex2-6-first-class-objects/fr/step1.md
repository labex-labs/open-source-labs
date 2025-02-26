# Données de première classe

Dans le fichier `portfolio.csv`, vous avez lu des données organisées en colonnes qui ressemblent à ceci :

```python
"AA",100,32.20
"IBM",50,91.10
...
```

Dans le code précédent, ces données étaient traitées en durcissant toutes les conversions de type. Par exemple :

```python
rows = csv.reader(f)
for row in rows:
    name   = row[0]
    shares = int(row[1])
    price  = float(row[2])
```

Ce type de conversion peut également être effectué de manière plus astucieuse en utilisant certaines opérations de liste. Créez une liste Python qui contient les conversions que vous souhaitez effectuer sur chaque colonne :

```python
>>> coltypes = [str, int, float]
>>>
```

La raison pour laquelle vous pouvez même créer cette liste est que tout en Python est "de première classe". Donc, si vous voulez avoir une liste de fonctions, c'est parfait.

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

Associez les types de colonnes à la ligne et regardez le résultat :

```python
>>> r = list(zip(coltypes, row))
>>> r
[(<class'str'>, 'AA'), (<class 'int'>, '100'), (<class 'float'>,'32.20')]
>>>
```

Vous remarquerez que cela a associé une conversion de type avec une valeur. Par exemple, `int` est associé à la valeur `'100'`. Maintenant, essayez ceci :

```python
>>> record = [func(val) for func, val in zip(coltypes, row)]
>>> record
['AA', 100, 32.2]
>>>
```

Assurez-vous de comprendre ce qui se passe dans le code ci-dessus. Dans la boucle, la variable `func` est l'une des fonctions de conversion de type (par exemple, `str`, `int`, etc.) et la variable `val` est l'une des valeurs telles que `'AA'`, `'100'`. L'expression `func(val)` convertit une valeur (un peu comme un cast de type).

Vous pouvez aller plus loin et créer des dictionnaires en utilisant les en-têtes de colonnes. Par exemple :

```python
>>> dict(zip(headers, record))
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```

Si vous le préférez, vous pouvez effectuer toutes ces étapes d'un coup en utilisant une compréhension de dictionnaire :

```python
>>> { name:func(val) for name, func, val in zip(headers, coltypes, row) }
{'name': 'AA','shares': 100, 'price': 32.2}
>>>
```
