# Slots vs. setattr

Dans les exercices précédents, `__slots__` a été utilisé pour lister les attributs d'instance sur une classe. Le principal but des slots est d'optimiser l'utilisation de la mémoire. Un effet secondaire est qu'il limite strictement les attributs autorisés à ceux qui sont listés. Un inconvénient des slots est qu'ils interagissent souvent étrangement avec d'autres parties de Python (par exemple, les classes utilisant des slots ne peuvent pas être utilisées avec l'héritage multiple). Pour cette raison, vous ne devriez vraiment pas utiliser de slots sauf dans des cas spéciaux.

Si vous vouliez vraiment limiter l'ensemble des attributs autorisés, une autre manière de le faire serait de définir une méthode `__setattr__()`. Essayez cet exemple :

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        def __setattr__(self, name, value):
            if name not in { 'name','shares', 'price' }:
                raise AttributeError('No attribute %s' % name)
            super().__setattr__(name, value)

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares = 75
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __setattr__
AttributeError: No attribute share
>>>
```

Dans cet exemple, il n'y a pas de slots, mais la méthode `__setattr__()` restreint toujours les attributs à ceux d'un ensemble prédéfini. Vous devriez probablement réfléchir à la manière dont cette approche pourrait interagir avec l'héritage (par exemple, si les sous-classes voulaient ajouter de nouveaux attributs, elles devraient probablement redéfinir `__setattr__()` pour qu'elle fonctionne).
