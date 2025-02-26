# Regardez avec Étonnement

Essayez d'exécuter les tests unitaires de votre fichier `teststock.py` sur ce nouveau fichier. La plupart d'entre eux devraient maintenant passer. Pour le fun, essayez votre classe `Stock` avec du code précédent pour le formatage de tableaux et la lecture de données. Tout devrait fonctionner.

```python
>>> from stock import Stock
>>> from reader import read_csv_as_instances
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]
>>> from tableformat import create_formatter, print_table
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

Encore une fois, admirez le fichier `stock.py` final et observez à quel point le code semble propre. Essayez simplement de ne pas penser à tout ce qui se passe sous le capot avec la classe de base `Structure`.
