# Subclass Registration

Try the following experiment and observe:

```python
>>> from structly.tableformat.formats.text import TextTableFormatter
>>> TextTableFormatter.__module__
'structly.tableformat.formats.text'
>>> TextTableFormatter.__module__.split('.')[-1]
'text'
>>>
```

Modify the `TableFormatter` base class by adding a dictionary and an `__init_subclass__()` method:

```python
class TableFormatter(ABC):
    _formats = { }

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

This makes the parent class track all of its subclasses. Check it out:

```python
>>> from structly.tableformat.formatter import TableFormatter
>>> TableFormatter._formats
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>,
 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>,
 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
>>>
```

Modify the `create_formatter()` function to look up the class in this dictionary instead:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Run the `stock.py` program. Make sure it still works after you've made these changes. Just a note that all of the import statements are still there. You've mainly just cleaned up the code a bit and eliminated the hard-wired class names.
