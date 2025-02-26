# Tuples nommés

Dans l'exercice 2.1, vous avez expérimenté avec des objets `namedtuple` dans le module `collections`. Pour vous rafraîchir la mémoire, voici comment ils fonctionnaient :

```python
>>> from collections import namedtuple
>>> Stock = namedtuple('Stock', ['name','shares', 'price'])
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s[1]
100
>>>
```

En réalité, la fonction `namedtuple()` crée du code sous forme de chaîne de caractères et l'exécute à l'aide de `exec()`. Regardez le code et admirez :

```python
>>> import inspect
>>> print(inspect.getsource(namedtuple))
... regardez la sortie...
>>>
```
