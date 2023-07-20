# Class variables and inheritance

Class variables such as `types` are sometimes used as a customization mechanism
when inheritance is used. For example, in the `Stock` class, the types can be
easily changed in a subclass. Try this example which changes the `price` attribute
to a `Decimal` instance (which is often better suited to financial calculations):

```python
>>> from decimal import Decimal
>>> class DStock(Stock):
        types = (str, int, Decimal)

>>> row = ['AA', '100', '32.20']
>>> s = DStock.from_row(row)
>>> s.price
Decimal('32.20')
>>> s.cost()
Decimal('3220.0')
>>>
```

**Design Discussion**

The problem being addressed in this exercise concerns the conversion of data read
from a file. Would it make sense to perform these conversions in the `__init__()`
method of the `Stock` class instead? For example:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

By doing this, you would convert a row of data as follows:

```python
>>> row = ['AA', '100', '32.20']
>>> s = Stock(*row)
>>> s.name
'AA'
>>> s.shares
100
>>> s.price
32.2
>>>
```

Is this good or bad? What are your thoughts? On the whole, I think
it's a questionable design since it mixes two different things
together--the creation of an instance and the conversion of data.
Plus, the implicit conversions in `__init__()` limit flexibility and
might introduce weird bugs if a user isn't paying careful attention.
