# Closures as a code generator

In [Exercise 4.3](ex4_3.md), you developed a collection of descriptor classes that allowed type-checking of object attributes. For example:

```python

class Stock:
    name = String()
    shares = Integer()
    price = Float()
```

This kind of thing can also be implemented using closures. Define a file `typedproperty.py` and put the following code in it:

```python
# typedproperty.py

def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    return value
```

This look pretty wild, but the function is effectively making code. You'd use it in a class definition like this:

```python
from typedproperty import typedproperty

class Stock:
    name = typedproperty('name', str)
    shares = typedproperty('shares', int)
    price = typedproperty('price', float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Verify that this class performs type-checking in the same way as the descriptor code.

Add function `String()`, `Integer()`, and `Float()` to the `typedproperty.py` file so that you can write the following code:

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```
