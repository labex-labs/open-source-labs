# Création d'un objet appelable

Dans le fichier `validate.py`, commençons par créer une classe comme ceci :

```python
# validate.py
...

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Appel de', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Testez la classe en l'appliquant à une fonction :

```python
>>> def add(x, y):
        return x + y

>>> add = ValidatedFunction(add)
>>> add(2, 3)
Appel de <function add at 0x1014df598>
5
>>>
```
