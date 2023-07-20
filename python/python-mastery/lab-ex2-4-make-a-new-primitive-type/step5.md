# Conversions

Your new primitive type is almost complete. You might want to give it
the ability to work with some common conversions. For example:

```python
>>> a = MutInt(3)
>>> int(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: int() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>> float(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: float() argument must be a string, a bytes-like object or a number, not 'MutInt'
>>>
```

You can give your class an `__int__()` and `__float__()` method to fix this:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    ...

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)
```

Now, you can properly convert:

```python
>>> a = MutInt(3)
>>> int(a)
3
>>> float(a)
3.0
>>>
```

As a general rule, Python never automatically converts data though. Thus, even though you
gave the class an `__int__()` method, `MutInt` is still not going to work in all
situations when an integer might be expected. For example, indexing:

```python
>>> names = ['Dave', 'Guido', 'Paula', 'Thomas', 'Lewis']
>>> a = MutInt(1)
>>> names[a]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not MutInt
>>>
```

This can be fixed by giving `MutInt` an `__index__()` method that produces an integer.
Modify the class like this:

```python
from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    ...

    def __int__(self):
        return self.value

    __index__ = __int__     # Make indexing work
```

**Discussion**

Making a new primitive datatype is actually one of the most complicated
programming tasks in Python. There are a lot of edge cases and low-level
issues to worry about--especially with regard to how your type interacts
with other Python types. Probably the key thing to keep in mind is that
you can customize almost every aspect of how an object interacts with the
rest of Python if you know the underlying protocols. If you're going to
do this, it's advisable to look at the existing code for something similar
to what you're trying to make.
