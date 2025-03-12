# Creating a Context Manager

A context manager is an object that defines the methods `__enter__` and `__exit__`. It's designed to be used with the `with` statement to set up a context for a block of code and clean up when the block exits.

In this step, we'll create a context manager that temporarily redirects standard output (`sys.stdout`) to a file. This is useful when you want to capture output that would normally go to the console.

Create a new file called `redirect.py` with the following code:

```bash
touch /home/labex/project/redirect.py
```

Open the file in the editor and add this code:

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

Let's understand what this context manager does:

1. `__init__`: Stores the file object we want to redirect output to
2. `__enter__`:
   - Saves the current `sys.stdout`
   - Replaces `sys.stdout` with our file
   - Returns the file object
3. `__exit__`:
   - Restores the original `sys.stdout`
   - Takes three parameters (exception type, value, and traceback) that are needed for the context manager protocol

Now, let's test this context manager to redirect the table output to a file:

```bash
python3
```

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Perfect! Our context manager successfully redirected the table output to the file `out.txt`.

Context managers are a powerful Python feature that helps you manage resources properly. They're commonly used for:

- File operations
- Database connections
- Locks in threaded programs
- Temporarily changing environment settings

This pattern ensures that resources are properly cleaned up even if exceptions occur within the `with` block.

Exit the Python interpreter when you're done:

```python
>>> exit()
```
