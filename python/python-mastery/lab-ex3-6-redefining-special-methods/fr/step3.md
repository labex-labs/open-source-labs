# Un gestionnaire de contexte

Dans l'exercice 3.5, vous avez rendu possible pour les utilisateurs de créer des tableaux bien formatés. Par exemple :

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

Un problème avec le code est que tous les tableaux sont imprimés sur la sortie standard (`sys.stdout`). Supposons que vous vouliez rediriger la sortie vers un fichier ou un autre emplacement. Dans l'ensemble, vous pourriez modifier tout le code de formatage de table pour autoriser un fichier de sortie différent. Cependant, dans l'improviste, vous pourriez également résoudre ce problème avec un gestionnaire de contexte.

Définissez le gestionnaire de contexte suivant :

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

Ce gestionnaire de contexte fonctionne en effectuant un patch temporaire sur `sys.stdout` pour forcer toute la sortie à être redirigée vers un autre fichier. Lors de la sortie, le patch est rétabli. Essayez-le :

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # Inspectez le fichier
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
