# Module Splitting

The file `structly/tableformat.py` contains code for creating tables in different
formats. Specifically:

- A `TableFormatter` base class.
- A `TextTableFormatter` class.
- A `CSVTableFormatter` class.
- A `HTMLTableFormatter` class.

Instead of having all of these classes in a single `.py`
file, maybe it would make sense to move each concrete formatter to
its own file. To do this, we're going to split the `tableformat.py`
file into parts. Follow these instructions carefully:

First, remove the `structly/__pycache__` directory.

```
% cd structly
% rm -rf __pycache__
```

Next, create the directory `structly/tableformat`. This directory
must have exactly the same name as the module it is replacing
(`tableformat.py`).

```bash
mkdir tableformat
```

Move the original `tableformat.py` file into the new
`tableformat` directory and rename it to `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

In the `tableformat` directory, split the
`tableformat.py` code into the following files and directories:

- `formatter.py` - Contains the `TableFormatter` base class, mixins, and various functions.
- `formats/text.py` - Contains the `TextTableFormatter` class.
- `formats/csv.py` - Contains the `CSVTableFormatter` class.
- `formats/html.py` - Contains the `HTMLTableFormatter` class.

Add an `__init__.py` file to the `tableformat/` and `tableformat/formats`
directories. Have the `tableformat/__init__.py` export the same
symbols that the original `tableformat.py` file exported.

After you have made all of these changes, you should have a package
structure that looks like this:

```
structly/
      __init__.py
      validate.py
      reader.py
      structure.py
      tableformat/
           __init__.py
           formatter.py
           formats/
               __init__.py
               text.py
               csv.py
               html.py
```

To users, everything should work exactly as it did before. For example, your
prior `stock.py` file should work:

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

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
