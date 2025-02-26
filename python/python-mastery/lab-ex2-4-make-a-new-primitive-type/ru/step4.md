# Сравнения

Одна проблема заключается в том, что сравнения по-прежнему не работают. Например:

```python
>>> a = MutInt(3)
>>> b = MutInt(3)
>>> a == b
False
>>> a == 3
False
>>>
```

Вы можете это исправить, добавив метод `__eq__()`. Дополнительные методы, такие как `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`, могут быть использованы для реализации других сравнений. Например:

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

Попробуйте:

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

Причина, по которой оператор `<=` не работает, заключается в том, что метод `__le__()` не был предоставлен. Вы можете написать его отдельно, но проще получить его с помощью декоратора `@total_ordering`:

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

`@total_ordering` заполняет отсутствующие методы сравнения для вас, если только вы минимально предоставите оператор равенства и одну из других отношений.
