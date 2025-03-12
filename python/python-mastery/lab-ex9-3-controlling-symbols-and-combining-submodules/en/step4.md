# Module Splitting for Better Code Organization

As your Python projects grow, you might find that a single module file becomes quite large and contains multiple related but distinct components. When this happens, it's a good practice to split the module into a package with submodules. This approach makes your code more organized, easier to maintain, and more scalable.

## Understanding the Current Structure

The `tableformat.py` module is a good example of a large module. It contains several formatter classes, each responsible for formatting data in a different way:

- `TableFormatter` (base class): This is the base class for all the other formatter classes. It defines the basic structure and methods that the other classes will inherit and implement.
- `TextTableFormatter`: This class formats data in plain text.
- `CSVTableFormatter`: This class formats data in CSV (Comma-Separated Values) format.
- `HTMLTableFormatter`: This class formats data in HTML (Hypertext Markup Language) format.

We'll reorganize this module into a package structure with separate files for each formatter type. This will make the code more modular and easier to manage.

## Step 1: Clean Up Cache Files

Before we start reorganizing the code, it's a good idea to clean up any Python cache files. These files are created by Python to speed up the execution of your code, but they can sometimes cause issues when you're making changes to your code.

```bash
cd ~/project/structly
rm -rf __pycache__
```

In the above commands, `cd ~/project/structly` changes the current directory to the `structly` directory in your project. `rm -rf __pycache__` deletes the `__pycache__` directory and all its contents. The `-r` option stands for recursive, which means it will delete all the files and subdirectories inside the `__pycache__` directory. The `-f` option stands for force, which means it will delete the files without asking for confirmation.

## Step 2: Create the New Package Structure

Now, let's create a new directory structure for our package. We'll create a directory named `tableformat` and a subdirectory named `formats` inside it.

```bash
mkdir -p tableformat/formats
```

The `mkdir` command is used to create directories. The `-p` option stands for parents, which means it will create all the necessary parent directories if they don't exist. So, if the `tableformat` directory doesn't exist, it will be created first, and then the `formats` directory will be created inside it.

## Step 3: Move and Rename the Original File

Next, we'll move the original `tableformat.py` file into the new structure and rename it to `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

The `mv` command is used to move or rename files. In this case, we're moving the `tableformat.py` file to the `tableformat` directory and renaming it to `formatter.py`.

## Step 4: Split the Code into Separate Files

Now we need to create files for each formatter and move the relevant code into them.

### 1. Create the base formatter file

```bash
touch tableformat/formatter.py
```

The `touch` command is used to create an empty file. In this case, we're creating a file named `formatter.py` in the `tableformat` directory.

We'll keep the `TableFormatter` base class and any general utility functions like `print_table` and `create_formatter` in this file. The file should look something like:

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

The `__all__` variable is used to specify which symbols should be imported when you use `from module import *`. In this case, we're specifying that only the `TableFormatter`, `print_table`, and `create_formatter` symbols should be imported.

The `TableFormatter` class is the base class for all the other formatter classes. It defines two methods, `headings` and `row`, which are meant to be implemented by the subclasses.

The `print_table` function is a utility function that takes a list of objects, a list of column names, and a formatter object, and prints the data in a formatted table.

The `create_formatter` function is a factory function that takes a format name as an argument and returns an appropriate formatter object.

Save and exit the file after making these changes.

### 2. Create the text formatter

```bash
touch tableformat/formats/text.py
```

We'll add only the `TextTableFormatter` class to this file.

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

The `__all__` variable specifies that only the `TextTableFormatter` symbol should be imported when you use `from module import *`.

The `from ..formatter import TableFormatter` statement imports the `TableFormatter` class from the `formatter.py` file in the parent directory.

The `TextTableFormatter` class inherits from the `TableFormatter` class and implements the `headings` and `row` methods to format the data in plain text.

Save and exit the file after making these changes.

### 3. Create the CSV formatter

```bash
touch tableformat/formats/csv.py
```

We'll add only the `CSVTableFormatter` class to this file.

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

Similar to the previous steps, we're specifying the `__all__` variable, importing the `TableFormatter` class, and implementing the `headings` and `row` methods to format the data in CSV format.

Save and exit the file after making these changes.

### 4. Create the HTML formatter

```bash
touch tableformat/formats/html.py
```

We'll add only the `HTMLTableFormatter` class to this file.

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

Again, we're specifying the `__all__` variable, importing the `TableFormatter` class, and implementing the `headings` and `row` methods to format the data in HTML format.

Save and exit the file after making these changes.

## Step 5: Create Package Initialization Files

In Python, `__init__.py` files are used to mark directories as Python packages. We need to create `__init__.py` files in both the `tableformat` and `formats` directories.

### 1. Create one for the `tableformat` package

```bash
touch tableformat/__init__.py
```

Add this content to the file:

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

This statement imports all the symbols from the `formatter.py` file and makes them available when you import the `tableformat` package.

Save and exit the file after making these changes.

### 2. Create one for the `formats` package

```bash
touch tableformat/formats/__init__.py
```

You can leave this file empty or add a simple docstring:

```python
'''
Format implementations for different output formats.
'''
```

The docstring provides a brief description of what the `formats` package does.

Save and exit the file after making these changes.

## Step 6: Test the New Structure

Let's create a simple test to verify that our changes work correctly.

```bash
cd ~/project
touch test_tableformat.py
```

Add this content to the `test_tableformat.py` file:

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

This test code imports the necessary functions and classes from the `structly` package, creates formatters of each type, defines some test data, and then tests each formatter by printing the data in the corresponding format.

Save and exit the file after making these changes. Now run the test:

```bash
python test_tableformat.py
```

You should see the same data formatted in three different ways (text, CSV, and HTML). If you see the expected output, it means that your code reorganization was successful.
