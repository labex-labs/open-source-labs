# A Real Decorator

In [Exercise 6.6](ex6_6.md), you created a callable class `ValidatedFunction` that
enforced type annotations. Rewrite this class as a decorator function called `validated`.
It should allow you to write code like this:

```python
from validate import Integer, validated

@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y
```

Here's how the decorated functions should work:

```python
>>> add(2, 3)
5
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>

>>> pow(2, 3)
8
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
```

Your decorator should try to patch up the exceptions so that they
show more useful information as shown. Also, the `@validated`
decorator should work in classes (you don't need to do anything special).

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
```

Note: This part doesn't involve a lot of code, but there are a lot of low-level
fiddly bits. The solution will look almost the same as for Exercise 6.6. Don't
be shy about looking at solution code though.
