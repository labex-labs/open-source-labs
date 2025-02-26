# Intrusion dans la pile d'appels

Une critique concernant la dernière partie est que la fonction `__init__()` semble maintenant assez étrange avec cet appel à `locals()` inséré dedans. Cependant, vous pouvez contourner ce problème si vous êtes prêt à faire un peu d'intrusion dans la pile d'appels. Essayez cette variante de la fonction `_init()` :

```python
>>> import sys
>>> def _init():
        locs = sys._getframe(1).f_locals   # Récupérer les variables locales de l'appelant
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
>>>
```

Dans ce code, les variables locales sont extraites de la pile d'appels de l'appelant. Voici une définition de classe modifiée :

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            _init()

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

À ce stade, vous êtes probablement assez troublé. Oui, vous venez d'écrire une fonction qui a pénétré dans la pile d'appels d'une autre fonction et a examiné ses variables locales.
