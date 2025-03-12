# Implementing Subclass Registration

Instead of directly importing formatter classes, we can use a registration pattern where subclasses register themselves with their parent class. This is a common way to avoid circular imports.

First, let's explore how we can identify the module name of a class:

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

You should see output like:

```
structly.tableformat.formats.text
text
```

This shows that we can extract the name of the module from the class itself, which we'll use in our registration pattern.

Now, let's modify the `TableFormatter` class in `tableformat/formatter.py` to add a registration mechanism. Open the file in the WebIDE and add the following code:

```python
class TableFormatter(ABC):
    _formats = { }  # Dictionary to store registered formatters

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

The `__init_subclass__` method is called whenever a subclass of `TableFormatter` is created. It extracts the module name and registers the class in the `_formats` dictionary using the module name as a key.

Next, modify the `create_formatter` function to use the registration dictionary:

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

Save the file and test if the program still works:

```bash
python3 stock.py
```

You should see the program running correctly. Let's inspect the contents of the `_formats` dictionary to understand how the registration works:

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

You should see output showing the registered formatters:

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

This confirms that our subclasses are being registered correctly. However, we still have the imports in the middle of the file. In the next step, we'll fix that with dynamic imports.
