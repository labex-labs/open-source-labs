# Préparation

Dans l'exercice 4.3, vous avez créé une série de classes `Validator` pour effectuer différents types de vérifications de type et de valeur. Par exemple :

```python
>>> from validate import Integer
>>> Integer.check(1)
>>> Integer.check('hello')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 21, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

Vous pouvez utiliser les validateurs dans des fonctions comme ceci :

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>>
```

Dans cet exercice, nous allons aller un pas plus loin.
