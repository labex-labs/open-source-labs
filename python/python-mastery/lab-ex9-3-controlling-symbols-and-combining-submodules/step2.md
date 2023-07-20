# Controlling Exported Symbols

Modify all of the submodules in the `structly` package so that they explicitly
define an `__all__` variable which exports selected symbols. Specifically:

- `structure.py` should export `Structure`
- `reader.py` should export all of the various `read_csv_as_*()` functions
- `tableformat.py` exports `create_formatter()` and `print_table()`

Now, in the `__init__.py` file, unify all of the submodules like this:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

Once you have done this, you should be able to import everything from
a single logical module:

```python
# stock.py

from structly import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly import read_csv_as_instances, create_formatter, print_table
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
