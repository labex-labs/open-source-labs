# Création d'une fonction `__init__()`

Dans l'exercice 6.3, vous avez écrit du code qui inspectait la signature de la méthode `__init__()` pour définir les noms d'attributs dans une variable de classe `_fields`. Par exemple :

```python
class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

Stock.set_fields()
```

Au lieu d'inspecter la méthode `__init__()`, écrivez une méthode de classe `create_init(cls)` qui crée une méthode `__init__()` à partir de la valeur de `_fields`. Utilisez la fonction `exec()` pour faire cela comme indiqué ci-dessus. Voici comment un utilisateur l'utilisera :

```python
class Stock(Structure):
    _fields = ('name','shares', 'price')

Stock.create_init()
```

La classe résultante devrait fonctionner exactement de la même manière qu'auparavant :

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

Modifiez la classe `Stock` en cours pour utiliser la fonction `create_init()` comme indiqué. Vérifiez avec vos tests unitaires comme auparavant.

Pendant que vous y êtes, supprimez les méthodes `_init()` et `set_fields()` de la classe `Structure` - cette approche était un peu étrange.
