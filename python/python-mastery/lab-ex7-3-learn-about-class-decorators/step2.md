# Using Class Decorators to Fill in Details

An annoying aspect of the above code is there are extra details such as
`_fields` variable and the final step of `Stock.create_init()`. A lot
of this could be packaged into a class decorator instead.

In the file `structure.py`, make a class decorator `@validate_attributes`
that examines the class body for instances of Validators and fills in
the `_fields` variable. For example:

```python
# structure.py

from validate import Validator

def validate_attributes(cls):
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)
    cls._fields = [val.name for val in validators]
    return cls
```

This code relies on the fact that class dictionaries are ordered
starting in Python 3.6. Thus, it will encounter the different
`Validator` descriptors in the order that they're listed. Using this
order, you can then fill in the `_fields` variable. This allows
you to write code like this:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```

Once you've got this working, modify the `@validate_attributes`
decorator to additionally perform the final step of calling
`Stock.create_init()`. This will reduce the class to the
following:

```python
# stock.py

from structure import Structure, validate_attributes
from validate import String, PositiveInteger, PositiveFloat

@validate_attributes
class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```
