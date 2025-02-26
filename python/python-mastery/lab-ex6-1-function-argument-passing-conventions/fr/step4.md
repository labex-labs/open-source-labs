# Restriction des noms d'attributs

Donnez à la classe `Structure` une méthode `__setattr__()` qui limite l'ensemble des attributs autorisés à ceux figurant dans la variable `_fields`. Cependant, elle devrait toujours autoriser tout attribut "privé" (par exemple, un nom commençant par `_`) à être défini.

Par exemple :

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 13, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>> s._shares = 100     # Attribut privé. C'est OK
>>>
```
