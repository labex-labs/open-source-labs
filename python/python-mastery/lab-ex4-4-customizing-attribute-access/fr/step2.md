# Proxies

Une classe proxy est une classe qui s'enveloppe autour d'une classe existante et fournit une interface similaire. Définissez la classe suivante qui crée une couche de lecture seule autour d'un objet existant :

```python
>>> class Readonly:
        def __init__(self, obj):
            self.__dict__['_obj'] = obj
        def __setattr__(self, name, value):
            raise AttributeError("Can't set attribute")
        def __getattr__(self, name):
            return getattr(self._obj, name)

>>>
```

Pour utiliser la classe, vous l'enveloppez simplement autour d'une instance existante :

```python
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.1)
>>> p = Readonly(s)
>>> p.name
'GOOG'
>>> p.shares
100
>>> p.cost
49010.0
>>> p.shares = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: Can't set attribute
>>>
```
