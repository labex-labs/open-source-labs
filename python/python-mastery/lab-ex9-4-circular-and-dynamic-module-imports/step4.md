# Dynamic Imports

You're now ready for the final frontier. Delete the following import statements altogether:

```python
# formatter.py
...

from .formats.text import TextTableFormatter     # DELETE
from .formats.csv import CSVTableFormatter       # DELETE
from .formats.html import HTMLTableFormatter     # DELETE
...
```

Run your `stock.py` code again--it should fail with an error. It knows nothing about the text formatter. Fix it by adding this tiny fragment of code to `create_formatter()`:

```python
def create_formatter(name, column_formats=None, upper_headers=False):
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')
    ...
```

This code attempts a dynamic import of a formatter module if nothing is known about the name. The import alone (if it works) will register the class with the `_formats` dictionary and everything will just work. Magic!

Try running the `stock.py` code and make sure it works afterwards.
