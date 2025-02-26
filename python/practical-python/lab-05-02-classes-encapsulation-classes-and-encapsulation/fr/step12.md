# Exercice 5.6 : Propriétés simples

Les propriétés sont un moyen utile d'ajouter des "attributs calculés" à un objet. Dans `stock.py`, vous avez créé un objet `Stock`. Remarquez qu'il y a une légère incohérence dans la manière dont différents types de données sont extraits de votre objet :

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>>
```

Plus précisément, remarquez comment vous devez ajouter les parenthèses supplémentaires à `cost` car il s'agit d'une méthode.

Vous pouvez éliminer les parenthèses supplémentaires de `cost()` si vous le convertissez en propriété. Prenez votre classe `Stock` et modifiez-la de sorte que le calcul du coût fonctionne comme suit :

```python
>>> ================================ RESTART ================================
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> s.cost
49010.0
>>>
```

Essayez d'appeler `s.cost()` en tant que fonction et observez qu'elle ne fonctionne plus maintenant que `cost` a été défini comme une propriété.

```python
>>> s.cost()
... échoue...
>>>
```

Apporter ces modifications peut probablement casser votre programme `pcost.py` antérieur. Vous devrez peut-être revenir en arrière et éliminer les parenthèses de la méthode `cost()`.
