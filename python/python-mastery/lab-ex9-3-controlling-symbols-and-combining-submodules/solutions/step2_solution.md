# Step 2 Solution

```python
# structure.py

__all__ = ['Structure']
...
```

```python
# reader.py

__all__ = [ 'read_csv_as_dicts',
            'read_csv_as_instances' ]
...
```

```python
# tableformat.py

__all__ = ['create_formatter', 'print_table']
...
```

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

__all__ = [ *structure.__all__,
        *reader.__all__,
        *tableformat.__all__ ]
```

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
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
