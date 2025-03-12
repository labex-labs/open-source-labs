# Understanding Class Variables and Class Methods

In this first step, we will explore the concepts of class variables and class methods in Python, and examine how instances of our `Stock` class are currently created.

## What are Class Variables?

Class variables are variables that are shared among all instances of a class. Unlike instance variables that are unique to each instance, class variables are defined at the class level and accessible by all instances of that class.

## What are Class Methods?

Class methods are methods that operate on the class itself rather than on instances of the class. They are bound to the class and not the instance. Class methods are defined using the `@classmethod` decorator and take the class (`cls`) as their first parameter instead of the instance (`self`).

## Current Approach to Creating Stock Instances

Let's first see how we currently create instances of the `Stock` class. Open the file `stock.py` in the editor to observe the current implementation:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price
```

Instances of this class are typically created in one of these ways:

1. Direct initialization with values:

   ```python
   s = Stock('GOOG', 100, 490.1)
   ```

2. Creating from data read from a CSV file:
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```

Notice that when creating a `Stock` instance from CSV data, we need to manually convert the string values to the appropriate types.

Let's try this out. Create a new Python file called `test_stock.py` in the `~/project` directory with the following content:

```python
# test_stock.py
from stock import Stock
import csv

# Method 1: Direct creation
s1 = Stock('GOOG', 100, 490.1)
print(f"Stock: {s1.name}, Shares: {s1.shares}, Price: {s1.price}")
print(f"Cost: {s1.cost()}")

# Method 2: Creation from CSV row
with open('portfolio.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)  # Skip the header
    row = next(rows)      # Get the first data row
    s2 = Stock(row[0], int(row[1]), float(row[2]))
    print(f"\nStock from CSV: {s2.name}, Shares: {s2.shares}, Price: {s2.price}")
    print(f"Cost: {s2.cost()}")
```

Run this file to see the results:

```bash
cd ~/project
python test_stock.py
```

You should see output similar to:

```
Stock: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0

Stock from CSV: AA, Shares: 100, Price: 32.2
Cost: 3220.0
```

This manual conversion works, but it requires us to know the exact format of the data and perform conversions each time. In the next step, we'll create a more elegant solution using class methods.
