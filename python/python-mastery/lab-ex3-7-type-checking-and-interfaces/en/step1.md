# Interfaces and type checking

Modify the `print_table()` function so that it checks if the supplied formatter instance inherits from `TableFormatter`. If not, raise a `TypeError`.

Your new code should catch situations like this:

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: Expected a TableFormatter
>>>
```

Adding a check like this might add some degree of safety to the program. However you should still be aware that type-checking is rather weak in Python. There is no guarantee that the object passed as a formatter will work correctly even if it happens to inherit from the proper base class. This next part addresses that issue.
