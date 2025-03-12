# Implementing Alternative Constructors with Class Methods

In this step, we're going to learn how to implement an alternative constructor using a class method. This will allow us to create `Stock` objects from CSV row data in a more elegant way.

## What is an Alternative Constructor?

In Python, an alternative constructor is a useful pattern. Usually, we create objects using the standard `__init__` method. However, an alternative constructor gives us an additional way to create objects. Class methods are very suitable for implementing alternative constructors because they can access the class itself.

## Implementing the from_row() Class Method

We'll add a class variable `types` and a class method `from_row()` to our `Stock` class. This will simplify the process of creating `Stock` instances from CSV data.

Let's modify the `stock.py` file by adding the highlighted code:

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

Now, let's understand what's happening in this code step by step:

1. We defined a class variable `types`. It's a tuple that contains type conversion functions `(str, int, float)`. These functions will be used to convert the data from the CSV row to the appropriate types.
2. We added a class method `from_row()`. The `@classmethod` decorator marks this method as a class method.
3. The first parameter of this method is `cls`, which is a reference to the class itself. In normal methods, we use `self` to refer to an instance of the class, but here we use `cls` because it's a class method.
4. The `zip()` function is used to pair each type conversion function in `types` with the corresponding value in the `row` list.
5. We use a list comprehension to apply each conversion function to the corresponding value in the `row` list. This way, we convert the string data from the CSV row to the appropriate types.
6. Finally, we create a new instance of the `Stock` class using the converted values and return it.

## Testing the Alternative Constructor

Now, we'll create a new file called `test_class_method.py` to test our new class method. This will help us verify that the alternative constructor works as expected.

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

To see the results, run the following commands in your terminal:

```bash
cd ~/project
python test_class_method.py
```

You should see output similar to this:

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

Notice that now we can create `Stock` instances directly from string data without having to manually perform type conversions outside the class. This makes our code cleaner and ensures that the responsibility for data conversion is handled within the class itself.
