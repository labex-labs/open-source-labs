# Module Splitting for Better Code Organization

Sometimes a single module file becomes too large and contains multiple related but distinct components. In such cases, it's better to split the module into a package with submodules.

## Understanding the Current Structure

The `tableformat.py` module contains several formatter classes:

- `TableFormatter` (base class)
- `TextTableFormatter`
- `CSVTableFormatter`
- `HTMLTableFormatter`

We'll reorganize this into a package structure with separate files for each formatter type.

## Step 1: Clean Up Cache Files

First, let's clean up any Python cache files to avoid issues:

```bash
cd ~/project/structly
rm -rf __pycache__
```

## Step 2: Create the New Package Structure

Now, let's create a new directory structure:

```bash
mkdir -p tableformat/formats
```

## Step 3: Move and Rename the Original File

Next, move the original file into the new structure:

```bash
mv tableformat.py tableformat/formatter.py
```

## Step 4: Split the Code into Separate Files

Now we need to create files for each formatter:

1. First, let's create the base formatter file:

```bash
touch tableformat/formatter.py
```

Keep the `TableFormatter` base class and any general utility functions like `print_table` and `create_formatter`. The file should look something like:

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

Save and exit.

2. Next, let's create the text formatter:

```bash
touch tableformat/formats/text.py
```

Add only the `TextTableFormatter` class:

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

Save and exit.

3. Create the CSV formatter:

```bash
touch tableformat/formats/csv.py
```

Add only the `CSVTableFormatter` class:

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

Save and exit.

4. Create the HTML formatter:

```bash
touch tableformat/formats/html.py
```

Add only the `HTMLTableFormatter` class:

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

Save and exit.

## Step 5: Create Package Initialization Files

Now we need to create `__init__.py` files in both directories:

1. First, create one for the `tableformat` package:

```bash
touch tableformat/__init__.py
```

Add this content:

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

Save and exit.

2. Next, create one for the `formats` package:

```bash
touch tableformat/formats/__init__.py
```

Leave this file empty or add a simple docstring:

```python
'''
Format implementations for different output formats.
'''
```

Save and exit.

## Step 6: Test the New Structure

Let's create a simple test to verify our changes work correctly:

```bash
cd ~/project
touch test_tableformat.py
```

Add this content:

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

Save and exit. Now run the test:

```bash
python test_tableformat.py
```

You should see the same data formatted in three different ways (text, CSV, and HTML).
