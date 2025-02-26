# Sortie en Tableau

Dans l'exercice 3.1, vous avez écrit une fonction `print_portfolio()` qui affichait un tableau bien formaté. Cette fonction était adaptée spécifiquement à une liste d'objets `Stock`. Cependant, elle peut être complètement généralisée pour fonctionner avec n'importe quelle liste d'objets en utilisant la technique de la partie (b).

Créez un nouveau module appelé `tableformat.py`. Dans ce programme, écrivez une fonction `print_table()` qui prend une séquence (liste) d'objets, une liste de noms d'attributs et affiche un tableau bien formaté. Par exemple :

```python
>>> import stock
>>> import tableformat
>>> portfolio = stock.read_portfolio('portfolio.csv')
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

>>> tableformat.print_table(portfolio,['shares','name'])
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
>>>
```

Pour simplifier, faites en sorte que la fonction `print_table()` affiche chaque champ dans une colonne de 10 caractères de large.
