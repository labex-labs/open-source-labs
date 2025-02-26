# Création de nombreuses classes

Il existe d'autres situations où l'utilisation directe du constructeur `type()` peut être avantageuse. Considérez ce bout de code :

```python
# validate.py
...

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'expected {cls.expected_type}')
        super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
...
```

Wow, la dernière partie est ennuyeuse et répétitive. Modifions-la pour utiliser un tableau de classes de types souhaitées comme ceci :

```python
# validate.py
...

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String','str') ]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)
```

Maintenant, si vous voulez avoir plus de classes de types, vous n'avez qu'à les ajouter au tableau :

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String','str') ]
```

Admettez-le, c'est assez cool et économise beaucoup de frappe (au clavier).
