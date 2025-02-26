# Создание множества классов

В других ситуациях прямой вызов конструктора `type()` может быть полезен. Возьмите этот кусок кода:

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

Уфф, последняя часть выглядит ужасно раздражающей и повторяющейся. Переделайте ее, используя таблицу классов с желаемыми типами, вот так:

```python
# validate.py
...

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str) ]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)
```

Теперь, если вы хотите добавить еще классов типов, просто добавьте их в таблицу:

```python
_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String', str) ]
```

Примите承认吧, это довольно круто и экономит много нажатий клавиш.
