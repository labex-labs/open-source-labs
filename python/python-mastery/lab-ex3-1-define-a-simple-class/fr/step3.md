# Affichage d'un tableau

Mettez en tableau les données lues à l'étape 2 et utilisez-les pour créer un tableau bien formaté. Par exemple :

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> for s in portfolio:
           print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

Prenez ce code et mettez-le dans une fonction `print_portfolio()` qui produit la même sortie, mais ajoute en outre des en-têtes de tableau. Par exemple :

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> print_portfolio(portfolio)
      name     shares      price
---------- ---------- ----------
        AA        100      32.20
       IBM         50      91.10
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50      65.10
       IBM        100      70.44
>>>
```

## Note :

Complétez la fonction `print_portfolio()` dans le fichier `stock.py`.
