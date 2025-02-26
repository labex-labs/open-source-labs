# Exercice 4.2 : Ajout de méthodes

Avec les classes, vous pouvez attacher des fonctions à vos objets. Ce sont appelées des méthodes et sont des fonctions qui opèrent sur les données stockées à l'intérieur d'un objet. Ajoutez une méthode `cost()` et `sell()` à votre objet `Stock`. Elles devraient fonctionner comme ceci :

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.10)
>>> s.cost()
49010.0
>>> s.shares
100
>>> s.sell(25)
>>> s.shares
75
>>> s.cost()
36757.5
>>>
```
