# Ausgabe beheben

Du kannst die Ausgabe beheben, indem du den Objekten Methoden wie `__str__()`, `__repr__()` und `__format__()` angibst. Beispielsweise:

```python
# mint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        return format(self.value, fmt)
```

Teste es:

```python
>>> a = MutInt(3)
>>> print(a)
3
>>> a
MutInt(3)
>>> f'The value is {a:*^10d}'
The value is ****3*****
>>> a.value = 42
>>> a
MutInt(42)
>>>
```
