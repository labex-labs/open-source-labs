# A Context Manager

In [Exercise 3.5](ex3_5.md), you made it possible for users to make
nicely formatted tables. For example:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

One issue with the code is that all tables are printed to standard out
(`sys.stdout`). Suppose you wanted to redirect the output to a file
or some other location. In the big picture, you might modify all of
the table formatting code to allow a different output file. However,
in a pinch, you could also solve this with a context manager.

Define the following context manager:

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

This context manager works by making a temporary patch to `sys.stdout` to cause
all output to redirect to a different file. On exit, the patch is reverted.
Try it out:

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # Inspect the file
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
>>>
```
