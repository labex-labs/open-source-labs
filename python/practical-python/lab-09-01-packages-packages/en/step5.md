# Problem: Imports

Imports between files in the same package _must now include the package name in the import_. Remember the structure.

```code
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

Modified import example.

```python
from porty import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

All imports are _absolute_, not relative.

```python
import fileparse    # BREAKS. fileparse not found

...
```
