# Simplified Data Structures

In earlier exercises, you defined a class representing a stock like
this:

```python
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

Focus on the `__init__()` method---isn't that a lot of
code to type each time you want to populate a structure? What if you
had to define dozens of such structures in your program?

In a file `structure.py`, define a base class
`Structure` that allows the user to define simple
data structures as follows:

```python
class Stock(Structure):
    _fields = ('name','shares','price')

class Date(Structure):
    _fields = ('year', 'month', 'day')
```

The `Structure` class should define an `__init__()`
method that takes any number of arguments and which looks for the
presence of a `_fields` class variable. Have the method
populate the instance from the attribute names in `_fields`
and values passed to `__init__()`.

Here is some sample code to test your implementation:

```python
>>> s = Stock('GOOG',100,490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s = Stock('AA',50)
Traceback (most recent call last):
...
TypeError: Expected 3 arguments
>>>
```
