# Improving Object Representation with `__repr__`

In Python, objects have two string representations:

1. The **string representation** created by `str()` function (called by `print()`) - a human-readable format
2. The **code representation** created by `repr()` function - shows the code needed to recreate the object

Let's look at a concrete example with Python's built-in date class:

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # Uses str()
2008-07-05
>>> d                     # Uses repr()
datetime.date(2008, 7, 5)
```

You can explicitly get the `repr()` string in various ways:

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
```

Now, let's improve our `Stock` class by implementing the `__repr__` method. This special method is called when Python needs the code representation of an object.

Open the file `stock.py` in the editor and add the `__repr__` method to the `Stock` class:

```python
def __repr__(self):
    return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Your complete `Stock` class should now look like this:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares

    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
```

Now let's test our modified class. Open a Python interactive shell by running:

```bash
python3
```

Then try the following commands:

```python
>>> import stock
>>> goog = stock.Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
```

You can also see how it works with a portfolio of stocks:

```python
>>> import reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23), Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
```

The `__repr__` method has made our `Stock` objects much more informative when displayed in the interactive shell or debugger. It now shows the code needed to recreate each object.

Exit the Python interpreter when you're done:

```python
>>> exit()
```
