# Creando muchas clases

Hay otras situaciones en las que el uso directo del constructor `type()` puede ser ventajoso. Considere este trozo de código:

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

Uf, la última parte es molesta y repetitiva. Cambiemoslo para usar una tabla de clases de tipos deseados como esta:

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

Ahora, si desea tener más clases de tipos, simplemente las agrega a la tabla:

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

Admitanlo, eso es genial y ahorra mucho teclear (en el teclado).
