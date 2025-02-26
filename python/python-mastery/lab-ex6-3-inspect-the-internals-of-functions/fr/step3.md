# Mettre tout ça ensemble

Dans l'exercice 6.1, vous avez créé une classe `Structure` qui définissait une `__init__()`, une `__setattr__()` et une `__repr__()` généralisées. Cette classe nécessitait qu'un utilisateur définisse une variable de classe `_fields` comme ceci :

```python
class Stock(Structure):
    _fields = ('name','shares','price')
```

Le problème de cette classe est que la fonction `__init__()` n'avait pas une signature d'arguments utile pour l'aide et le passage d'arguments nommés. Dans l'exercice 6.2, vous avez fait un tour astucieux impliquant une fonction spéciale `self._init()`. Par exemple :

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')
    def __init__(self, name, shares, price):
        self._init()
  ...
```

Cela donnait une signature utile, mais maintenant la classe est juste bizarre car l'utilisateur doit fournir à la fois la variable `_fields` et la méthode `__init__()`.

Votre tâche est d'éliminer la variable `_fields` en utilisant certaines techniques d'inspection de fonctions. Tout d'abord, remarquez que vous pouvez obtenir la signature d'arguments de `Stock` comme suit :

```python
>>> import inspect
>>> sig = inspect.signature(Stock)
>>> tuple(sig.parameters)
('name','shares', 'price')
>>>
```

Peut-être pourriez-vous définir la variable `_fields` à partir de la signature d'arguments de `__init__()`. Ajoutez une méthode de classe `set_fields(cls)` à `Structure` qui inspecte la fonction `__init__()` et définit la variable `_fields` en conséquence. Vous devriez utiliser votre nouvelle fonction comme ceci :

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

  ...

Stock.set_fields()
```

La classe résultante devrait fonctionner de la même manière que précédemment :

```python
>>> s = Stock(name='GOOG', shares=100, price=490.1)
>>> s
Stock('GOOG',100,490.1)
>>> s.shares = 50
>>> s.share = 50
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "structure.py", line 12, in __setattr__
    raise AttributeError('No attribute %s' % name)
AttributeError: No attribute share
>>>
```

Vérifiez à nouveau la classe `Stock` légèrement modifiée avec vos tests unitaires. Il y aura toujours des échecs, mais rien ne devrait changer par rapport à l'exercice précédent.

À ce stade, tout est encore un peu "bidouillé", mais vous progressez. Vous avez une classe de structure `Stock` avec une fonction `__init__()` utile, une chaîne de représentation utile et la méthode `__setattr__()` restreint l'ensemble des noms d'attributs. L'étape supplémentaire consistant à devoir invoquer `set_fields()` est un peu étrange, mais on y reviendra.
