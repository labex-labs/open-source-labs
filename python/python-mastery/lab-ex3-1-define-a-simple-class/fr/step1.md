# Ajout d'une nouvelle méthode

Ajoutez une nouvelle méthode `sell(nshares)` à `Stock` qui vend un certain nombre d'actions en décrémentant le compte d'actions. Faites en sorte qu'elle fonctionne comme ceci :

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>>
```

## Note :

Complétez la fonction `sell(nshares)` dans le fichier `stock.py`.
