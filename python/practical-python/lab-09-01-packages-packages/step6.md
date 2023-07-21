# Relative Imports

Instead of directly using the package name,
you can use `.` to refer to the current package.

```python
# report.py
from . import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Syntax:

```python
from . import modname
```

This makes it easy to rename the package.
