# Математические операторы

Вы можете заставить объект работать с различными математическими операторами, если реализуете для него соответствующие методы. Однако, вам необходимо самостоятельно распознавать другие типы данных и реализовать соответствующий код преобразования. Измените класс `MutInt`, добавив метод `__add__()` следующим образом:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented
```

После этого изменения вы должны увидеть, что можно складывать как целые числа, так и изменяемые целые числа. Результатом будет экземпляр `MutInt`. Сложение других типов чисел приводит к ошибке:

```python
>>> a = MutInt(3)
>>> b = a + 10
>>> b
MutInt(13)
>>> b.value = 23
>>> c = a + b
>>> c
MutInt(26)
>>> a + 3.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'float'
>>>
```

Одна проблема с этим кодом заключается в том, что он не работает, когда порядок операндов наоборот. Например:

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'MutInt'
>>>
```

Это происходит потому, что тип `int` не знает о `MutInt` и запутывается. Это можно исправить, добавив метод `__radd__()`. Этот метод вызывается, если первый вызов `__add__()` не сработал с предоставленным объектом.

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__    # Перевернутые операнды
```

После этого изменения вы увидите, что сложение работает:

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

Поскольку наш целый тип изменяемый, вы также можете заставить его распознавать оператор in-place сложения-обновления `+=`, реализовав метод `__iadd__()`:

```python
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

  ...

    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented
```

Это позволяет использовать его интересным способом, например:

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # Обратите внимание, что b также меняется
MutInt(13)
>>>
```

Может показаться странным, что `b` также меняется, но у встроенных объектов Python есть такие неожиданные особенности. Например:

```python
>>> a = [1,2,3]
>>> b = a
>>> a += [4,5]
>>> a
[1, 2, 3, 4, 5]
>>> b
[1, 2, 3, 4, 5]

>>> c = (1,2,3)
>>> d = c
>>> c += (4,5)
>>> c
(1, 2, 3, 4, 5)
>>> d                  # Объясните разницу с списками
(1, 2, 3)
>>>
```
