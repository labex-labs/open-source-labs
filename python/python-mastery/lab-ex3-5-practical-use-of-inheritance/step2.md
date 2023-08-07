# Defining a generic formatter class

Add the following class definition to the `tableformat.py` file:

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

Now, modify the `print_table()` function so that it accepts a `TableFormatter` instance
and invokes methods on it to produce output:

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

These two classes are meant to be used together. For example:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.TableFormatter()
>>> tableformat.print_table(portfolio, ['name', 'shares', 'price'], formatter)
Traceback (most recent call last):
...
NotImplementedError
>>>
```

For now, it doesn't do much of anything interesting. You'll fix this in the next section.
