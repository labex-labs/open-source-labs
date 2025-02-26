# Exercice 4.10 : Un exemple d'utilisation de getattr()

`getattr()` est un mécanisme alternatif pour lire les attributs. Il peut être utilisé pour écrire du code extrêmement flexible. Pour commencer, essayez cet exemple :

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name','shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

Observez attentivement que les données de sortie sont déterminées entièrement par les noms d'attributs listés dans la variable `columns`.

Dans le fichier `tableformat.py`, prenez cette idée et développez-la en une fonction généralisée `print_table()` qui imprime un tableau montrant les attributs spécifiés par l'utilisateur d'une liste d'objets arbitraires. Comme avec la fonction `print_report()` précédente, `print_table()` devrait également accepter une instance `TableFormatter` pour contrôler le format de sortie. Voici comment cela devrait fonctionner :

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares', 'price'], formatter)
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
