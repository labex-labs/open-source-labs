# Implementing Alternative Constructors with Class Methods

In this step, we'll implement an alternative constructor using a class method to create `Stock` objects from CSV row data more elegantly.

## What is an Alternative Constructor?

An alternative constructor is a common pattern in Python that provides an additional way to create objects besides the standard `__init__` method. Class methods are perfect for implementing alternative constructors since they have access to the class itself.

## Implementing the from_row() Class Method

Let's add a class variable `types` and a class method `from_row()` to our `Stock` class to simplify creating `Stock` instances from CSV data.

Modify the `stock.py` file by adding the highlighted code:

```python
# stock.py

class Stock:
    types = (str, int, float)  # Type conversions to apply to CSV data

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    @classmethod
    def from_row(cls, row):
        """
        Create a Stock instance from a row of CSV data.

        Args:
            row: A list of strings [name, shares, price]

        Returns:
            A new Stock instance
        """
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

# The rest of the file remains unchanged
```

Let's break down what's happening in this code:

1. We defined a class variable `types` which is a tuple of type conversion functions `(str, int, float)`.
2. We added a class method `from_row()` marked with the `@classmethod` decorator.
3. The method takes a class reference `cls` as its first parameter (instead of `self`).
4. It uses the `zip()` function to pair each type conversion function with the corresponding value in the row.
5. It applies each conversion function to the corresponding value using a list comprehension.
6. Finally, it creates and returns a new instance of the class using the converted values.

## Testing the Alternative Constructor

Now let's create a new file called `test_class_method.py` to test our new class method:

```python
# test_class_method.py
from stock import Stock

# Test the from_row() class method
row = ['AA', '100', '32.20']
s = Stock.from_row(row)

print(f"Stock: {s.name}")
print(f"Shares: {s.shares}")
print(f"Price: {s.price}")
print(f"Cost: {s.cost()}")

# Try with a different row
row2 = ['GOOG', '50', '1120.50']
s2 = Stock.from_row(row2)

print(f"\nStock: {s2.name}")
print(f"Shares: {s2.shares}")
print(f"Price: {s2.price}")
print(f"Cost: {s2.cost()}")
```

Run this file to see the results:

```bash
cd ~/project
python test_class_method.py
```

You should see output similar to:

```
Stock: AA
Shares: 100
Price: 32.2
Cost: 3220.0

Stock: GOOG
Shares: 50
Price: 1120.5
Cost: 56025.0
```

Notice how we can now create `Stock` instances directly from string data without having to manually perform type conversions outside the class. This makes our code cleaner and places the responsibility for data conversion where it belongs - in the class itself.
