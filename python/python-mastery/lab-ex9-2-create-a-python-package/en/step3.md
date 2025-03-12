# Fixing Import Statements

Now that we've moved our files into the `structly` package, we need to update the import statements in each file to reflect the new package structure.

The most important file to update is `structure.py`, as it imports from `validate.py`. Since both files are now in the same package, we need to update the import statement.

Open the `structly/structure.py` file in the editor:

```bash
# Click on structly/structure.py in the file explorer or run:
code structly/structure.py
```

Change the first line from:

```python
from validate import validate_type, PositiveInteger, PositiveFloat, String
```

to:

```python
from .validate import validate_type, PositiveInteger, PositiveFloat, String
```

The dot (`.`) before `validate` tells Python to look for the `validate` module in the same package as the current module. This is called a relative import.

Save the file after making the change.

Let's also check our other files to see if they need updates:

1. `structly/reader.py` - This file doesn't import from any of our modules, so no changes are needed.
2. `structly/tableformat.py` - This file doesn't import from any of our modules, so no changes are needed.
3. `structly/validate.py` - This file doesn't import from any of our modules, so no changes are needed.

In real-world scenarios, you might have more complex dependencies between your modules. Always ensure that imports are properly updated when moving files into a package structure.
