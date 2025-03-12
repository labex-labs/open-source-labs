# Implementing Subclass Registration

In programming, circular imports can be a tricky problem. Instead of directly importing formatter classes, we can use a registration pattern. In this pattern, subclasses register themselves with their parent class. This is a common and effective way to avoid circular imports.

First, let's understand how we can find out the module name of a class. The module name is important because we'll use it in our registration pattern. To do this, we'll run a Python command in the terminal.

```bash
cd ~/project/structly
python3 -c "from structly.tableformat.formats.text import TextTableFormatter; print(TextTableFormatter.__module__); print(TextTableFormatter.__module__.split('.')[-1])"
```

When you run this command, you'll see output like this:

```
structly.tableformat.formats.text
text
```

This output shows that we can extract the name of the module from the class itself. We'll use this module name later to register the subclasses.

Now, let's modify the `TableFormatter` class in the `tableformat/formatter.py` file to add a registration mechanism. Open this file in the WebIDE. We'll add some code to the `TableFormatter` class. This code will help us register the subclasses automatically.

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

The `__init_subclass__` method is a special method in Python. It gets called whenever a subclass of `TableFormatter` is created. In this method, we extract the module name of the subclass and use it as a key to register the subclass in the `_formats` dictionary.

Next, we need to modify the `create_formatter` function to use the registration dictionary. This function is responsible for creating the appropriate formatter based on the given name.

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

After making these changes, save the file. Then, let's test if the program still works. We'll run the `stock.py` script.

```bash
python3 stock.py
```

If the program runs correctly, it means our changes haven't broken anything. Now, let's take a look at the contents of the `_formats` dictionary to see how the registration works.

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter; print(TableFormatter._formats)"
```

You should see output like this:

```
{'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>, 'csv': <class 'structly.tableformat.formats.csv.CSVTableFormatter'>, 'html': <class 'structly.tableformat.formats.html.HTMLTableFormatter'>}
```

This output confirms that our subclasses are being registered correctly in the `_formats` dictionary. However, we still have some imports in the middle of the file. In the next step, we'll fix this issue using dynamic imports.
