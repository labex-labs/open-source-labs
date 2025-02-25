# Idiomes courants pour écrire dans un fichier

Écrire des données sous forme de chaîne de caractères.

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
 ...
```

Rediriger la fonction `print`.

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
 ...
```

Ces exercices dépendent d'un fichier `portfolio.csv`. Le fichier contient une liste de lignes avec des informations sur un portefeuille d'actions. On suppose que vous travaillez dans le répertoire `~/project/`. Si vous n'êtes pas sûr, vous pouvez découvrir où Python pense qu'il est exécuté en faisant ceci :

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # Output vary
>>>
```
