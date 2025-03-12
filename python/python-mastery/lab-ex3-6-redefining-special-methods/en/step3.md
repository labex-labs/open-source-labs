# Creating a Context Manager

A context manager is a special type of object in Python. In Python, objects can have different methods that define their behavior. A context manager specifically defines two important methods: `__enter__` and `__exit__`. These methods work together with the `with` statement. The `with` statement is used to set up a specific context for a block of code. Think of it as creating a little environment where certain things happen, and when the block of code is finished, the context manager takes care of cleaning up.

In this step, we're going to create a context manager that has a very useful function. It will temporarily redirect the standard output (`sys.stdout`). Standard output is where the normal output of your Python program goes, usually the console. By redirecting it, we can send the output to a file instead. This is handy when you want to save the output that would otherwise just be displayed on the console.

First, we need to create a new file to write our context manager code. We'll name this file `redirect.py`. You can create it using the following command in the terminal:

```bash
touch /home/labex/project/redirect.py
```

Now that the file is created, open it in an editor. Once it's open, add the following Python code to the file:

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

Let's break down what this context manager does:

1. `__init__`: This is the initialization method. When we create an instance of the `redirect_stdout` class, we pass in a file object. This method stores that file object in the instance variable `self.out_file`. So, it remembers where we want to redirect the output to.
2. `__enter__`:
   - First, it saves the current `sys.stdout`. This is important because we need to restore it later.
   - Then, it replaces the current `sys.stdout` with our file object. From this point on, any output that would normally go to the console will go to the file instead.
   - Finally, it returns the file object. This is useful because we might want to use the file object inside the `with` block.
3. `__exit__`:
   - This method restores the original `sys.stdout`. So, after the `with` block is finished, the output will go back to the console as normal.
   - It takes three parameters: exception type (`ty`), exception value (`val`), and traceback (`tb`). These parameters are required by the context manager protocol. They are used to handle any exceptions that might occur inside the `with` block.

Now, let's test our context manager. We'll use it to redirect the output of a table to a file. First, start the Python interpreter:

```bash
python3
```

Then, run the following Python code in the interpreter:

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

Great! Our context manager worked as expected. It successfully redirected the table output to the file `out.txt`.

Context managers are a very powerful feature in Python. They help you manage resources properly. Here are some common use cases for context managers:

- File operations: When you open a file, a context manager can make sure the file is closed properly, even if an error occurs.
- Database connections: It can ensure that the database connection is closed after you're done using it.
- Locks in threaded programs: Context managers can handle locking and unlocking resources in a safe way.
- Temporarily changing environment settings: You can change some settings for a block of code and then restore them automatically.

This pattern is very important because it ensures that resources are properly cleaned up, even if an exception occurs inside the `with` block.

When you're done testing, you can exit the Python interpreter:

```python
>>> exit()
```
