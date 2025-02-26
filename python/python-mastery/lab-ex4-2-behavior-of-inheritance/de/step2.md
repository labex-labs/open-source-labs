# Erstellen eines Wertprüfers

In Übung 3.4 haben Sie einigen Eigenschaften zur `Stock`-Klasse hinzugefügt, die Attribute auf verschiedene Typen und Werte überprüfen (z.B. mussten die Anteile eine positive Ganzzahl sein). Spielen wir ein wenig mit dieser Idee. Beginnen Sie, indem Sie eine Datei `validate.py` erstellen und die folgende Basisklasse definieren:

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

Lassen Sie uns nun einige Klassen für die Typüberprüfung erstellen:

```python
class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Erwartet {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str
```

So verwenden Sie diese Klassen (Hinweis: Das Verwenden von `@classmethod` ermöglicht es uns, den zusätzlichen Schritt des Erstellens von Instanzen zu vermeiden, den wir eigentlich nicht benötigen):

```python
>>> Integer.check(10)
10
>>> Integer.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in check
    raise TypeError(f'Erwartet {cls.expected_type}')
TypeError: Erwartet <class 'int'>
>>> String.check('10')
'10'
>>>
```

Sie könnten die Validatoren in einer Funktion verwenden. Beispielsweise:

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
    raise TypeError(f'Erwartet {cls.expected_type}')
TypeError: Erwartet <class 'int'>
>>>
```

Lassen Sie uns nun einige weitere Klassen für verschiedene Arten der Bereichsüberprüfung erstellen:

```python
class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Erwartet >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Muss nicht leer sein')
        return super().check(value)
```

Wohin führt all das? Lassen Sie uns beginnen, Klassen zusammenzusetzen mit Mehrfachvererbung wie mit Spielsteinen:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Im Grunde genommen nehmen Sie vorhandene Validatoren und kombinieren sie zu neuen. Wahnsinn! Lassen Sie uns sie jedoch jetzt verwenden, um einige Dinge zu validieren:

```python
>>> PositiveInteger.check(10)
10
>>> PositiveInteger.check('10')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise TypeError(f'Erwartet {cls.expected_type}')
TypeError: Erwartet <class 'int'>
>>> PositiveInteger.check(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Erwartet >= 0')
ValueError: Muss >= 0 sein


>>> NonEmptyString.check('hello')
'hello'
>>> NonEmptyString.check('')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise ValueError('Muss nicht leer sein')
ValueError: Muss nicht leer sein
>>>
```

Zu diesem Zeitpunkt ist Ihr Kopf wahrscheinlich völlig explodiert. Das Problem des Zusammenfügens unterschiedlicher Codeteile tritt jedoch in Echtzeitprogrammen auf. Kooperative Mehrfachvererbung ist eines der Werkzeuge, mit denen es organisiert werden kann.
