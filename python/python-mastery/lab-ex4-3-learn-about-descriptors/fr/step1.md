# Descripteurs en action

Plus tôt, vous avez créé une classe `Stock` qui utilisait des slots, des propriétés et d'autres fonctionnalités. Toutes ces fonctionnalités sont implémentées à l'aide du protocole descripteur. Regardez-le en action en essayant cet expériment simple.

Tout d'abord, créez un objet stock et essayez de rechercher quelques attributs :

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

Maintenant, remarquez que ces attributs sont dans le dictionnaire de la classe.

```python
>>> Stock.__dict__.keys()
['sell', '__module__', '__weakref__', 'price', '_price','shares', '_shares',
'__slots__', 'cost', '__repr__', '__doc__', '__init__']
>>>
```

Essayez ces étapes qui illustrent comment les descripteurs obtiennent et définissent des valeurs sur une instance :

```python
>>> q = Stock.__dict__['shares']
>>> q.__get__(s)
100
>>> q.__set__(s,75)
>>> s.shares
75
>>> q.__set__(s, '75')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "stock.py", line 23, in shares
    raise TypeError('Expected an integer')
TypeError: Expected an integer
>>>
```

L'exécution de `__get__()` et `__set__()` se produit automatiquement chaque fois que vous accédez à des instances.
