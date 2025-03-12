# Using Dynamic Imports

In programming, imports are used to bring in code from other modules so that we can use their functionality. However, sometimes having imports in the middle of a file can make the code a bit messy and hard to understand. In this part, we'll learn how to use dynamic imports to solve this problem. Dynamic imports are a powerful feature that allows us to load modules at runtime, which means we only load a module when we actually need it.

First, we need to remove the import statements that are currently placed after the `TableFormatter` class. These imports are static imports, which are loaded when the program starts. To do this, open the `tableformat/formatter.py` file in the WebIDE. Once you've opened the file, find and delete the following lines:

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

If you try to run the program now by executing the following command in the terminal:

```bash
python3 stock.py
```

The program will fail. The reason is that the formatters won't be registered in the `_formats` dictionary. You'll see an error message about an unknown format. This is because the program can't find the formatter classes it needs to work properly.

To fix this issue, we'll modify the `create_formatter` function. The goal is to dynamically import the required module when it's needed. Update the function as shown below:

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

The most important line in this function is:

```python
__import__(f'{__package__}.formats.{name}')
```

This line dynamically imports the module based on the format name. When the module is imported, its subclass of `TableFormatter` automatically registers itself. This is thanks to the `__init_subclass__` method we added earlier. This method is a special Python method that gets called when a subclass is created, and in our case, it's used to register the formatter class.

After making these changes, save the file. Then, run the program again using the following command:

```bash
python3 stock.py
```

The program should now work correctly, even though we've removed the static imports. To verify that the dynamic import is working as expected, we'll clear the `_formats` dictionary and then call the `create_formatter` function. Run the following command in the terminal:

```bash
python3 -c "from structly.tableformat.formatter import TableFormatter, create_formatter; TableFormatter._formats.clear(); print('Before:', TableFormatter._formats); create_formatter('text'); print('After:', TableFormatter._formats)"
```

You should see output similar to this:

```
Before: {}
After: {'text': <class 'structly.tableformat.formats.text.TextTableFormatter'>}
```

This output confirms that the dynamic import is loading the module and registering the formatter class when needed.

By using dynamic imports and class registration, we've created a cleaner and more maintainable code structure. Here are the benefits:

1. All imports are now at the top of the file, which follows Python conventions. This makes the code easier to read and understand.
2. We've eliminated circular imports. Circular imports can cause problems in a program, such as infinite loops or hard-to-debug errors.
3. The code is more flexible. Now, we can add new formatters without modifying the `create_formatter` function. This is very useful in a real-world scenario where new features might be added over time.

This pattern of using dynamic imports and class registration is commonly used in plugin systems and frameworks. In these systems, components need to be loaded dynamically based on the user's needs or the program's requirements.
