# Exporting Everything from the Package

Now let's take our package organization a step further by defining what symbols should be exported at the package level.

## Adding `__all__` to the Package

When we add an `__all__` list to the package's `__init__.py` file, we can control exactly which symbols are available when someone uses `from structly import *`.

Let's update the `__init__.py` file:

```bash
nano ~/project/structly/__init__.py
```

Add an `__all__` list that includes all the symbols we want to export:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

Save and exit.

## Understanding `import *`

The `from module import *` pattern is generally discouraged in most Python code because:

1. It can pollute your namespace with unexpected symbols
2. It makes it unclear where particular symbols come from
3. It can lead to shadowing issues

However, it's appropriate in specific cases:

- For packages designed to be used as a cohesive whole
- When a package defines a clear interface via `__all__`
- For interactive use (like in a Python REPL)

## Testing with Import \*

Let's create another test file to verify that we can import everything at once:

```bash
nano ~/project/test_import_all.py
```

Add this content:

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

Save and exit. Now run the test:

```bash
cd ~/project
python test_import_all.py
```

You should see confirmation that all symbols were successfully imported.
