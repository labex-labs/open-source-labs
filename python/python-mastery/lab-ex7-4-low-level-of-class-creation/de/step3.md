# Viele Klassen erstellen

Es gibt andere Situationen, in denen die direkte Verwendung des `type()`-Konstruktors vorteilhaft sein kann. Betrachten Sie diesen Codeausschnitt:

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

Wow, der letzte Teil ist wirklich lästig und repetitiv. Ändern Sie es, um eine Tabelle von gewünschten Typklassen zu verwenden, wie folgt:

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

Jetzt können Sie einfach weitere Typklassen hinzufügen, indem Sie sie zur Tabelle hinzufügen:

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

Gestatten Sie sich zugeben, dass das ziemlich cool ist und eine Menge Tipparbeit (am Tastatur) spart.
