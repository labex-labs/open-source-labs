# Comparaciones

Un problema es que las comparaciones todavía no funcionan. Por ejemplo:

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
False
>>> a == 3
False
>>>
```

Puedes corregir esto agregando un método `__eq__()`. Métodos adicionales como `__lt__()`, `__le__()`, `__gt__()`, `__ge__()` se pueden usar para implementar otras comparaciones. Por ejemplo:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

Prueba:

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
True
>>> c = MutInt(4)
>>> a < c
True
>>> a <= c
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<=' not supported between instances of 'MutInt' and 'MutInt'
>>>
```

La razón por la que el operador `<=` está fallando es que no se proporcionó un método `__le__()`. Podrías codificarlo por separado, pero una forma más fácil de obtenerlo es usar el decorador `@total_ordering`:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

 ...

    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented
```

`@total_ordering` completa los métodos de comparación faltantes para ti siempre y cuando proporciones mínimamente un operador de igualdad y una de las otras relaciones.
