# Controlling Exported Symbols with `__all__`

In Python, when you use the `from module import *` statement, you might want to control which symbols (functions, classes, variables) are imported from a module. This is where the `__all__` variable comes in handy. The `from module import *` statement is a way to import all the symbols from a module into the current namespace. However, sometimes you don't want to import every single symbol, especially if there are many or if some are meant to be internal to the module. The `__all__` variable allows you to specify exactly which symbols should be imported when using this statement.

## What is `__all__`?

The `__all__` variable is a list of strings. Each string in this list represents a symbol (function, class, or variable) that a module exports when someone uses the `from module import *` statement. If the `__all__` variable is not defined in a module, the `import *` statement will import all symbols that don't begin with an underscore. Symbols starting with an underscore are typically considered private or internal to the module and are not meant to be imported directly.

## Modifying Each Submodule

Now, let's add the `__all__` variable to each submodule in the `structly` package. This will help us control which symbols are exported from each submodule when someone uses the `from module import *` statement.

1. First, let's modify `structure.py`:

```bash
touch ~/project/structly/structure.py
```

This command creates a new file named `structure.py` in the `structly` directory of your project. After creating the file, we need to add the `__all__` variable. Add this line near the top of the file, right after the import statements:

```python
__all__ = ['Structure']
```

This line tells Python that when someone uses `from structure import *`, only the `Structure` symbol will be imported. Save the file and exit the editor.

2. Next, let's modify `reader.py`:

```bash
touch ~/project/structly/reader.py
```

This command creates a new file named `reader.py` in the `structly` directory. Now, look through the file to find all the functions that start with `read_csv_as_`. These functions are the ones we want to export. Then, add an `__all__` list with all these function names. It should look something like this:

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

Note that the actual function names may vary depending on what you find in the file. Make sure to include all the `read_csv_as_*` functions you find. Save the file and exit the editor.

3. Now, let's modify `tableformat.py`:

```bash
touch ~/project/structly/tableformat.py
```

This command creates a new file named `tableformat.py` in the `structly` directory. Add this line near the top of the file:

```python
__all__ = ['create_formatter', 'print_table']
```

This line specifies that when someone uses `from tableformat import *`, only the `create_formatter` and `print_table` symbols will be imported. Save the file and exit the editor.

## Unified Imports in `__init__.py`

Now that each module defines what it exports, we can update the `__init__.py` file to import all of these symbols. The `__init__.py` file is a special file in Python packages. It is executed when the package is imported, and it can be used to initialize the package and import symbols from submodules.

```bash
touch ~/project/structly/__init__.py
```

This command creates a new `__init__.py` file in the `structly` directory. Change the content of the file to:

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

These lines import all the exported symbols from the `structure`, `reader`, and `tableformat` submodules. The dot (`.`) before the module names indicates that these are relative imports, meaning they are imports from within the same package. Save the file and exit the editor.

## Testing Our Changes

Let's create a simple test file to verify that our changes work. This test file will try to import the symbols we specified in the `__all__` variables and print a success message if the imports are successful.

```bash
touch ~/project/test_structly.py
```

This command creates a new file named `test_structly.py` in the project directory. Add this content to the file:

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

These lines try to import the `Structure` class, the `read_csv_as_instances` function, and the `create_formatter` and `print_table` functions from the `structly` package. If the imports are successful, the program will print the message "Successfully imported all required symbols!". Save the file and exit the editor. Now let's run this test:

```bash
cd ~/project
python test_structly.py
```

The `cd ~/project` command changes the current working directory to the project directory. The `python test_structly.py` command runs the `test_structly.py` script. If everything is working correctly, you should see the message "Successfully imported all required symbols!" printed on the screen.
