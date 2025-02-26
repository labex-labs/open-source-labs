# Utiliser l'instruction `import`

Dans les exercices précédents, vous avez écrit deux programmes `pcost.py` et `stock.py`. Utilisez l'instruction `import` pour charger ces programmes et utiliser leur fonctionnalité :

```python
>>> import pcost
44671.15
>>> pcost.portfolio_cost('portfolio2.dat')
19908.75
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

Si vous ne parvenez pas à faire fonctionner les instructions ci-dessus, vous avez peut-être placé vos programmes dans un répertoire étrange. Assurez-vous d'exécuter Python dans le même répertoire que vos fichiers ou que le répertoire est inclus dans `sys.path`.
