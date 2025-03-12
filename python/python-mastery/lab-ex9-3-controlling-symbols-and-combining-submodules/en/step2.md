# Controlling Exported Symbols with `__all__`

In Python, you can control which symbols (functions, classes, variables) are exported from a module when someone uses `from module import *`. This is done using the `__all__` variable.

## What is `__all__`?

The `__all__` variable is a list of strings defining what symbols a module exports when `from module import *` is used. If `__all__` is not defined, `import *` imports all symbols that don't begin with an underscore.

## Modifying Each Submodule

Let's add the `__all__` variable to each submodule in the `structly` package:

1. First, let's modify `structure.py`:

```bash
touch ~/project/structly/structure.py
```

Add this line near the top of the file (after imports):

```python
__all__ = ['Structure']
```

Save and exit.

2. Next, let's modify `reader.py`:

```bash
touch ~/project/structly/reader.py
```

Look through the file to identify all the `read_csv_as_*` functions. Then add an `__all__` list with all these function names. It should look something like:

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

(The actual function names may vary; include all `read_csv_as_*` functions you find in the file.)

Save and exit.

3. Now, let's modify `tableformat.py`:

```bash
touch ~/project/structly/tableformat.py
```

Add this line near the top of the file:

```python
__all__ = ['create_formatter', 'print_table']
```

Save and exit.

## Unified Imports in `__init__.py`

Now that each module defines what it exports, let's update the `__init__.py` file to import all of these symbols:

```bash
touch ~/project/structly/__init__.py
```

Change the content to:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

Save and exit.

## Testing Our Changes

Let's create a simple test file to verify that our changes work:

```bash
touch ~/project/test_structly.py
```

Add this content:

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

Save and exit. Now let's run this test:

```bash
cd ~/project
python test_structly.py
```

You should see the message "Successfully imported all required symbols!" if everything is working correctly.
