# Making a Package

In previous exercises, you created the following files that were related to type-checked structures, reading data, and making tables:

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

Your task is to take all of these files and move them into a package called `structly`. To do that, follow these steps:

- Make a directory called `structly`
- Make an empty file `__init__.py` and put it in the `structly` directory
- Move the files `structure.py`, `validate.py`, `reader.py`, and `tableformat.py` into the `structly` directory.
- Fix any import statements between modules (specifically, the `structure` module depends on `validate`).

Once you've done that, modify the `stock.py` program so that it looks exactly like this and that it works:

```python
# stock.py

from structly.structure import Structure

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
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
