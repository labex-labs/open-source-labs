# Crea un verificador de valores

En el Ejercicio 3.4, agregaste algunas propiedades a la clase `Stock` que verifican los atributos para diferentes tipos y valores (por ejemplo, las acciones tenían que ser un número entero positivo). Vamos a jugar un poco con esa idea. Comienza creando un archivo `validate.py` y definiendo la siguiente clase base:

```python
# validate.py
class Validator:
    @classmethod
    def check(cls, value):
        return value
```

Ahora, vamos a crear algunas clases para la verificación de tipos:

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

Aquí está cómo se usan estas clases (Nota: el uso de `@classmethod` nos permite evitar el paso extra de crear instancias que realmente no necesitamos):

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

Podrías usar los validadores en una función. Por ejemplo:

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

Ahora, crea algunas clases más para diferentes tipos de verificación de dominio:

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

¿Adónde va todo esto? Comencemos a componer clases juntas con herencia múltiple como si fueran bloques de juguete:

```python
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

Esencialmente, estás tomando validadores existentes y los estás combinando en nuevos. ¡Loca! Sin embargo, usemoslos ahora para validar algunas cosas:

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

En este punto, tu cabeza probablemente se haya estallado completamente. Sin embargo, el problema de combinar diferentes fragmentos de código es uno que surge en los programas del mundo real. La herencia múltiple cooperativa es una de las herramientas que se pueden usar para organizarlo.
