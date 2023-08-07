# Making a lot of classes

There are other situations where direct usage of the `type()` constructor might be advantageous. Consider this bit of code:

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

Wow is the last part of that annoying and repetitive. Change it to use a table of desired type classes like this:

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

Now, if you want to have more type classes, you just add them to the table:

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

Admit it, that's kind of cool and saves a lot of typing (at the keyboard).
