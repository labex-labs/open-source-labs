# Math Operators

You can make an object work with various math operators if you implement the
appropriate methods for it. However, it's your responsibility to
recognize other types of data and implement the appropriate conversion
code. Modify the `MutInt` class by giving it an `__add__()` method
as follows:

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

With this change, you should find that you can add both integers and
mutable integers. The result is a `MutInt` instance. Adding
other kinds of numbers results in an error:

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

One problem with the code is that it doesn't work when the order of operands
is reversed. Consider:

```python
>>> a + 10
MutInt(13)
>>> 10 + a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'MutInt'
>>>
```

This is occurring because the `int` type has no knowledge of `MutInt`
and it's confused. This can be fixed by adding an `__radd__()` method. This
method is called if the first attempt to call `__add__()` didn't work with the
provided object.

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

    __radd__ = __add__    # Reversed operands
```

With this change, you'll find that addition works:

```python
>>> a = MutInt(3)
>>> a + 10
MutInt(13)
>>> 10 + a
MutInt(13)
>>>
```

Since our integer is mutable, you can also make it recognize the in-place
add-update operator `+=` by implementing the `__iadd__()` method:

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

This allows for interesting uses like this:

```python
>>> a = MutInt(3)
>>> b = a
>>> a += 10
>>> a
MutInt(13)
>>> b                 # Notice that b also changes
MutInt(13)
>>>
```

That might seem kind of strange that `b` also changes, but there are subtle features like
this with built-in Python objects. For example:

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
>>> d                  # Explain difference from lists
(1, 2, 3)
>>>
```
