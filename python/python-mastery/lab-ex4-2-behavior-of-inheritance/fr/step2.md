# Créez un vérificateur de valeurs

Dans l'exercice 3.4, vous avez ajouté quelques propriétés à la classe `Stock` qui vérifiaient les attributs pour différents types et valeurs (par exemple, les actions devaient être un entier positif). Jouons un peu avec cette idée. Commencez par créer un fichier `validate.py` et définir la classe de base suivante :

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

Maintenant, créons quelques classes pour la vérification de type :

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

Voici comment utiliser ces classes (Remarque : l'utilisation de `@classmethod` nous permet d'éviter l'étape supplémentaire de créer des instances que nous n'avons pas vraiment besoin) :

```python
>>> Integer.check(10)
10
>>> Integer.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>> String.check('10')
'10'
>>>
```

Vous pouvez utiliser les validateurs dans une fonction. Par exemple :

```python
>>> def add(x, y):
        Integer.check(x)
        Integer.check(y)
        return x + y

>>> add(2, 2)
4
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
  File "validate.py", line 11, in check
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>>
```

Maintenant, créons quelques autres classes pour différentes vérifications de domaine :

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)
```

Où allons-nous avec tout cela? Commençons à composer des classes ensemble avec l'héritage multiple comme des blocs de construction :

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Essentiellement, vous prenez des validateurs existants et les composez ensemble pour en créer de nouveaux. Folie! Cependant, utilisons-les maintenant pour valider quelques choses :

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError(f'Expected {cls.expected_type}')
TypeError: Expected <class 'int'>
>>> PositiveInteger.check(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Expected >= 0')
ValueError: Must be >= 0


>>> NonEmptyString.check('hello')
'hello'
>>> NonEmptyString.check('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Must be non-empty')
ValueError: Must be non-empty
>>>
```

À ce stade, votre tête est probablement complètement éclatée. Cependant, le problème de la composition de différents morceaux de code ensemble est un problème qui se pose dans les programmes du monde réel. L'héritage multiple coopératif est l'un des outils qui peut être utilisé pour l'organiser.
