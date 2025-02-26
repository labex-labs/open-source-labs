# Application de règles de validation

En utilisant des propriétés et des attributs privés, modifiez l'attribut `shares` de la classe `Stock` de sorte qu'il ne puisse être attribué qu'une valeur entière non négative. De plus, modifiez l'attribut `price` de sorte qu'il ne puisse être attribué qu'une valeur flottante non négative.

Le nouvel objet devrait fonctionner presque exactement comme l'ancien, sauf pour les vérifications supplémentaires de type et de valeur.

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.shares = 50          # OK
>>> s.shares = '50'
Traceback (most recent call last):
...
TypeError: Expected integer
>>> s.shares = -10
Traceback (most recent call last):
...
ValueError: shares must be >= 0

>>> s.price = 123.45       # OK
>>> s.price = '123.45'
Traceback (most recent call last):
...
TypeError: Expected float
>>> s.price = -10.0
Traceback (most recent call last):
...
ValueError: price must be >= 0
>>>
```
