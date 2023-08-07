# Mutable Integers

Python integers are normally immutable. However, suppose you wanted to
make a mutable integer object. Start off by making a class like this:

```python
# mutint.py

class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value
```

Try it out:

```python
>>> a = MutInt(3)
>>> a
<__main__.MutInt object at 0x10e79d408>
>>> a.value
3
>>> a.value = 42
>>> a.value
42
>>> a + 10
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'MutInt' and 'int'
>>>
```

That's all very exciting except that nothing really works with this
new `MutInt` object. Printing is horrible, none of the math
operators work, and it's basically rather useless. Well, except for
the fact that its value is mutable--it does have that.
