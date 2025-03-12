# Exporting Everything from the Package

In Python, package organization is crucial for managing code effectively. Now, we're going to take our package organization a step further. We'll define which symbols should be exported at the package level. Exporting symbols means making certain functions, classes, or variables available to other parts of your code or to other developers who might use your package.

## Adding `__all__` to the Package

When you're working with Python packages, you might want to control which symbols are accessible when someone uses the `from structly import *` statement. This is where the `__all__` list comes in handy. By adding an `__all__` list to the package's `__init__.py` file, you can precisely control which symbols are available when someone uses the `from structly import *` statement.

First, let's create or update the `__init__.py` file. We'll use the `touch` command to create the file if it doesn't exist.

```bash
touch ~/project/structly/__init__.py
```

Now, open the `__init__.py` file and add an `__all__` list. This list should include all the symbols we want to export. The symbols are grouped based on where they come from, such as the `structure`, `reader`, and `tableformat` modules.

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

After adding the code, save the file and exit the editor.

## Understanding `import *`

The `from module import *` pattern is generally not recommended in most Python code. There are several reasons for this:

1. It can pollute your namespace with unexpected symbols. This means that you might end up with variables or functions in your current namespace that you didn't expect, which can lead to naming conflicts.
2. It makes it unclear where particular symbols come from. When you use `import *`, it's hard to tell which module a symbol is coming from, which can make your code harder to understand and maintain.
3. It can lead to shadowing issues. Shadowing occurs when a local variable or function has the same name as a variable or function from another module, which can cause unexpected behavior.

However, there are specific cases where using `import *` is appropriate:

- For packages designed to be used as a cohesive whole. If a package is meant to be used as a single unit, then using `import *` can make it easier to access all the necessary symbols.
- When a package defines a clear interface via `__all__`. By using the `__all__` list, you can control which symbols are exported, making it safer to use `import *`.
- For interactive use, like in a Python REPL (Read-Eval-Print Loop). In an interactive environment, it can be convenient to import all symbols at once.

## Testing with Import \*

To verify that we can import all the symbols at once, let's create another test file. We'll use the `touch` command to create the file.

```bash
touch ~/project/test_import_all.py
```

Now, open the `test_import_all.py` file and add the following content. This code imports all the symbols from the `structly` package and then tests if some of the important symbols are available.

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

Save the file and exit the editor. Now, let's run the test. First, navigate to the project directory using the `cd` command, and then run the Python script.

```bash
cd ~/project
python test_import_all.py
```

If everything is set up correctly, you should see confirmation that all symbols were successfully imported.
