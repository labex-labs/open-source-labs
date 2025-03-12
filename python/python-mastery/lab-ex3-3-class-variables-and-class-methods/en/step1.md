# Understanding Class Variables and Class Methods

In this first step, we're going to dive into the concepts of class variables and class methods in Python. These are important concepts that will help you write more efficient and organized code. Before we start working with class variables and class methods, let's first take a look at how instances of our `Stock` class are currently created. This will give us a baseline understanding and show us where we can make improvements.

## What are Class Variables?

Class variables are a special type of variables in Python. They are shared among all instances of a class. To understand this better, let's compare them with instance variables. Instance variables are unique to each instance of a class. For example, if you have multiple instances of a class, each instance can have its own value for an instance variable. On the other hand, class variables are defined at the class level. This means that all instances of that class can access and share the same value of the class variable.

## What are Class Methods?

Class methods are methods that work on the class itself, not on individual instances of the class. They are bound to the class, which means they can be called directly on the class without creating an instance. To define a class method in Python, we use the `@classmethod` decorator. And instead of taking the instance (`self`) as the first parameter, class methods take the class (`cls`) as their first parameter. This allows them to operate on class-level data and perform actions related to the class as a whole.

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

   Here, we're directly creating an instance of the `Stock` class by providing the values for the `name`, `shares`, and `price` attributes. This is a straightforward way to create an instance when you know the values upfront.

2. Creating from data read from a CSV file:
   ```python
   import csv
   with open('portfolio.csv') as f:
       rows = csv.reader(f)
       headers = next(rows)  # Skip the header
       row = next(rows)      # Get the first data row
       s = Stock(row[0], int(row[1]), float(row[2]))
   ```
   When we read data from a CSV file, the values are initially in string format. So, when creating a `Stock` instance from CSV data, we need to manually convert the string values to the appropriate types. For example, the `shares` value needs to be converted to an integer, and the `price` value needs to be converted to a float.

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

This manual conversion works, but it has some drawbacks. We need to know the exact format of the data, and we have to perform the conversions each time we create an instance from CSV data. This can be error-prone and time-consuming. In the next step, we'll create a more elegant solution using class methods.
