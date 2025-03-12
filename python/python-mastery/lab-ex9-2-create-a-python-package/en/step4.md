# Updating and Testing the stock.py Program

Now that we've created our package and fixed the internal imports, we need to update the `stock.py` file to use our new package structure.

Open the `stock.py` file in the editor:

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

The current imports in `stock.py` are based on the old structure where all files were in the same directory. We need to update them to import from the `structly` package.

Update the `stock.py` file to look exactly like this:

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

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

The key changes are:

1. Changed `from structure import Structure, String, PositiveInteger, PositiveFloat` to `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`
2. Changed `from reader import read_csv_as_instances` to `from structly.reader import read_csv_as_instances`
3. Changed `from tableformat import create_formatter, print_table` to `from structly.tableformat import create_formatter, print_table`

Save the file after making these changes.

Now, let's test our updated code to ensure everything works correctly:

```bash
python stock.py
```

You should see the following output:

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

If you see this output, congratulations! You have successfully created a Python package and updated your code to use it.
