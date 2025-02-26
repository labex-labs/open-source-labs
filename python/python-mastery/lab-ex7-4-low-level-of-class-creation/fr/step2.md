# Structures typées

Dans le fichier `structure.py`, définissez la fonction suivante :

```python
# structure.py

...
def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
```

Cette fonction est quelque peu similaire à la fonction `namedtuple()` dans la mesure où elle crée une classe. Essayez-la :

```python
>>> from validate import String, PositiveInteger, PositiveFloat
>>> from structure import typed_structure
>>> Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

Vous pouvez commencer à ressentir les tensions dans votre cerveau à présent.
