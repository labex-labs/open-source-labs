# Exercice 1.26: Préliminaires sur les fichiers

Tout d'abord, essayez de lire le fichier entier d'un coup sous forme d'une grande chaîne de caractères :

```python
>>> with open('portfolio.csv', 'rt') as f:
        data = f.read()

>>> data
'name,shares,price\n"AA",100,32.20\n"IBM",50,91.10\n"CAT",150,83.44\n"MSFT",200,51.23\n"GE",95,40.37\n"MSFT",50,65.10\n"IBM",100,70.44\n'
>>> print(data)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44
>>>
```

Dans l'exemple ci-dessus, il est important de noter que Python a deux modes d'affichage. Dans le premier mode où vous tapez `data` à l'invite, Python vous montre la représentation brute de la chaîne de caractères, y compris les guillemets et les codes d'échappement. Lorsque vous tapez `print(data)`, vous obtenez la sortie formatée réelle de la chaîne de caractères.

Bien que lire un fichier d'un coup soit simple, ce n'est souvent pas la manière la plus appropriée de le faire - surtout si le fichier est énorme ou si il contient des lignes de texte que vous voulez traiter une par une.

Pour lire un fichier ligne par ligne, utilisez une boucle `for` comme ceci :

```python
>>> with open('portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')

name,shares,price
"AA",100,32.20
"IBM",50,91.10
...
>>>
```

Lorsque vous utilisez ce code tel qu'il est montré, les lignes sont lues jusqu'à la fin du fichier, auquel moment la boucle s'arrête.

Dans certains cas, vous pouvez vouloir lire ou sauter manuellement _une seule_ ligne de texte (par exemple, peut-être que vous voulez sauter la première ligne d'en-têtes de colonnes).

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f)
>>> headers
'name,shares,price\n'
>>> for line in f:
    print(line, end='')

"AA",100,32.20
"IBM",50,91.10
...
>>> f.close()
>>>
```

`next()` renvoie la ligne de texte suivante dans le fichier. Si vous l'appeliez répétitivement, vous obtiendriez les lignes successives. Cependant, sachez que la boucle `for` utilise déjà `next()` pour obtenir ses données. Ainsi, vous ne l'appelleriez normalement pas directement, sauf si vous essayez d'explicitement sauter ou lire une seule ligne comme montré.

Une fois que vous lisez les lignes d'un fichier, vous pouvez commencer à effectuer plus de traitements, tels que le découpage. Par exemple, essayez ceci :

```python
>>> f = open('portfolio.csv', 'rt')
>>> headers = next(f).split(',')
>>> headers
['name','shares', 'price\n']
>>> for line in f:
    row = line.split(',')
    print(row)

['"AA"', '100', '32.20\n']
['"IBM"', '50', '91.10\n']
...
>>> f.close()
```

_Attention : Dans ces exemples, `f.close()` est appelé explicitement car l'instruction `with` n'est pas utilisée._
