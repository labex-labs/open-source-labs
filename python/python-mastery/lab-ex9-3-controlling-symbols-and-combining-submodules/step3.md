# Exporting Everything

In the `structly/__init__.py`, define an `__all__` variable that contains all
exported symbols. Once you've done this, you should be able to simplify the
`stock.py` file further:

```python
# stock.py

from structly import *

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
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

As an aside, use of the `from module import *` statement is generally frowned upon
the Python community--especially if you're not sure what you're doing. That said,
there are situations where it often makes sense. For example, if a package defines
a large number of commonly used symbols or constants it might be useful to use it.
