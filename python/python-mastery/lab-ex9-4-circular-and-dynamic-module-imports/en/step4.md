# Using Dynamic Imports

Now we'll implement dynamic imports to eliminate the imports in the middle of the file. Dynamic imports allow us to load modules at runtime, only when we need them.

First, let's remove the import statements that are currently after the `TableFormatter` class. Open `tableformat/formatter.py` in the WebIDE and delete the following lines:

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

If you try to run the program now, it will fail because the formatters won't be registered in the `_formats` dictionary:

```bash
python3 stock.py
```

You should see an error message about an unknown format.

To fix this, we'll modify the `create_formatter` function to dynamically import the required module when needed. Update the function as follows:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

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

The key line here is:

```python
__import__(f'{__package__}.formats.{name}')
```

This dynamically imports the module based on the format name. When the module is imported, its subclass of `TableFormatter` automatically registers itself thanks to the `__init_subclass__` method we added earlier.

Save the file and run the program again:

```bash
python3 stock.py
```

The program should work correctly even though we've removed the static imports. Let's verify that the dynamic import is working by clearing the `_formats` dictionary and then calling `create_formatter`:

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

You should see output like:

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

This confirms that the dynamic import is loading the module and registering the formatter class when needed.

By using dynamic imports and class registration, we've created a cleaner, more maintainable code structure:

1. All imports are now at the top of the file (following Python conventions)
2. We've eliminated circular imports
3. The code is more flexible, as formatters can be added without modifying the `create_formatter` function

This pattern is commonly used in plugin systems and frameworks where components need to be loaded dynamically.
