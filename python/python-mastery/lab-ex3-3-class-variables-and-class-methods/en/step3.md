# Class Variables and Inheritance

In this step, we'll explore how class variables work with inheritance and how they can be used as a customization mechanism.

## Class Variables in Inheritance

When a subclass inherits from a base class, it also inherits the class variables. However, a subclass can override these class variables to change behavior without affecting the base class. This is a powerful way to customize subclass behavior.

## Creating a Specialized Stock Class

Let's create a subclass of `Stock` called `DStock` (Decimal Stock) that uses the `Decimal` type for price values instead of `float`. This can be useful for financial calculations where precision is critical.

Create a new file called `decimal_stock.py` with the following content:

```python
# decimal_stock.py
from decimal import Decimal
from stock import Stock

class DStock(Stock):
    """
    A specialized version of Stock that uses Decimal for prices
    """
    types = (str, int, Decimal)  # Override the types class variable

# Test the subclass
if __name__ == "__main__":
    # Create a DStock from row data
    row = ['AA', '100', '32.20']
    ds = DStock.from_row(row)

    print(f"DStock: {ds.name}")
    print(f"Shares: {ds.shares}")
    print(f"Price: {ds.price} (type: {type(ds.price).__name__})")
    print(f"Cost: {ds.cost()} (type: {type(ds.cost()).__name__})")

    # For comparison, create a regular Stock from the same data
    s = Stock.from_row(row)
    print(f"\nRegular Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price} (type: {type(s.price).__name__})")
    print(f"Cost: {s.cost()} (type: {type(s.cost()).__name__})")
```

Run this file to see the results:

```bash
cd ~/project
python decimal_stock.py
```

You should see output similar to:

```
DStock: AA
Shares: 100
Price: 32.20 (type: Decimal)
Cost: 3220.0 (type: Decimal)

Regular Stock: AA
Shares: 100
Price: 32.2 (type: float)
Cost: 3220.0 (type: float)
```

## Key Points about Class Variables and Inheritance

From this example, we can observe several important points:

1. The `DStock` class inherits all methods from `Stock` (like `cost()`) without having to redefine them.
2. By simply overriding the `types` class variable, we changed how data is converted when creating new instances.
3. The base class (`Stock`) remains unchanged and still works with float values.
4. The `from_row()` class method works correctly with both classes, showing the power of inheritance.

This demonstrates how class variables can be used as a configuration mechanism that subclasses can override to customize behavior, without having to rewrite methods.

## Design Discussion

Consider the alternative approach of placing the type conversions in the `__init__` method:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

With this approach, we could create a Stock from a row as follows:

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

While this approach seems simpler, it has several disadvantages:

1. It mixes two different concerns: object initialization and data conversion.
2. It makes the `__init__` method less flexible - it always converts inputs regardless of whether they're already the correct type.
3. It limits how subclasses can customize the conversion process.
4. It makes the code more brittle - if any conversion fails, the object can't be created.

The class method approach separates these concerns, making the code more maintainable and flexible.
