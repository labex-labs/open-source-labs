# Du Validateur au Descripteur

Dans l'exercice précédent, vous avez écrit une série de classes qui pouvaient effectuer des vérifications. Par exemple :

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError('Expected %s' % cls.expected_type)
TypeError: expected <class 'int'>
>>> PositiveInteger.check(-10)
```

Vous pouvez étendre cela aux descripteurs en apportant une modification simple à la classe de base `Validator`. Modifiez-la comme suit :

```python
# validate.py

class Validator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

Remarque : L'absence de la méthode `__get__()` dans le descripteur signifie que Python utilisera son implantation par défaut de la recherche d'attribut. Cela nécessite que le nom fourni corresponde au nom utilisé dans le dictionnaire d'instance.

Aucune autre modification n'est nécessaire. Maintenant, essayez de modifier la classe `Stock` pour utiliser les validateurs comme descripteurs comme ceci :

```python
class Stock:
    name   = String('name')
    shares = PositiveInteger('shares')
    price  = PositiveFloat('price')

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Vous constaterez que votre classe fonctionne de la même manière que précédemment, nécessite beaucoup moins de code et vous offre toutes les vérifications souhaitées :

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.shares = 75
>>> s.shares = '75'
... TypeError...
>>> s.shares = -50
... ValueError...
>>>
```

C'est assez génial. Les descripteurs vous ont permis de simplifier considérablement l'implémentation de la classe `Stock`. C'est le véritable pouvoir des descripteurs - vous avez un contrôle bas niveau sur le point et pouvez l'utiliser pour faire des choses incroyables.
