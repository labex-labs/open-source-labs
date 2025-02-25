# Pourquoi utiliser des dictionnaires?

Les dictionnaires sont utiles lorsqu'il y a _beaucoup_ de valeurs différentes et que ces valeurs peuvent être modifiées ou manipulées. Les dictionnaires rendent votre code plus lisible.

```python
s['price']
# vs
s[2]
```

Dans les derniers exercices, vous avez écrit un programme qui lisait un fichier de données `portfolio.csv`. En utilisant le module `csv`, il est facile de lire le fichier ligne par ligne.

```python
>>> import csv
>>> f = open('portfolio.csv')
>>> rows = csv.reader(f)
>>> next(rows)
['name','shares', 'price']
>>> row = next(rows)
>>> row
['AA', '100', '32.20']
>>>
```

Bien que la lecture du fichier soit facile, vous voulez souvent faire plus avec les données que simplement les lire. Par exemple, peut-être que vous voulez les stocker et commencer à effectuer des calculs sur elles. Malheureusement, une simple "ligne" de données brutes ne vous donne pas assez pour travailler. Par exemple, même un calcul mathématique simple ne fonctionne pas :

```python
>>> row = ['AA', '100', '32.20']
>>> cost = row[1] * row[2]
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type'str'
>>>
```

Pour faire plus, vous devez généralement interpréter les données brutes d'une certaine manière et les transformer en un type d'objet plus utile afin que vous puissiez travailler avec plus tard. Deux options simples sont les tuples ou les dictionnaires.
