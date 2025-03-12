# Class Variables and Inheritance

In this step, we're going to explore how class variables interact with inheritance and how they can serve as a mechanism for customization. In Python, inheritance allows a subclass to inherit attributes and methods from a base class. Class variables are variables that belong to the class itself, not to any specific instance of the class. Understanding how these work together is crucial for creating flexible and maintainable code.

## Class Variables in Inheritance

When a subclass inherits from a base class, it automatically gets access to the base class's class variables. However, a subclass has the ability to override these class variables. By doing so, the subclass can change its behavior without affecting the base class. This is a very powerful feature as it allows you to customize the behavior of a subclass according to your specific needs.

## Creating a Specialized Stock Class

Let's create a subclass of the `Stock` class. We'll call it `DStock`, which stands for Decimal Stock. The main difference between `DStock` and the regular `Stock` class is that `DStock` will use the `Decimal` type for price values instead of `float`. In financial calculations, precision is extremely important, and the `Decimal` type provides more accurate decimal arithmetic compared to `float`.

To create this subclass, we'll create a new file named `decimal_stock.py`. Here's the code you need to put in this file:

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

After you've created the `decimal_stock.py` file with the above code, you need to run it to see the results. Open your terminal and follow these steps:

```bash
cd ~/project
python decimal_stock.py
```

You should see output similar to this:

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

From this example, we can draw several important conclusions:

1. The `DStock` class inherits all the methods from the `Stock` class, such as the `cost()` method, without having to redefine them. This is one of the main advantages of inheritance, as it saves you from writing redundant code.
2. By simply overriding the `types` class variable, we've changed how data is converted when creating new instances of `DStock`. This shows how class variables can be used to customize the behavior of a subclass.
3. The base class, `Stock`, remains unchanged and still works with `float` values. This means that the changes we made to the subclass don't affect the base class, which is a good design principle.
4. The `from_row()` class method works correctly with both the `Stock` and `DStock` classes. This demonstrates the power of inheritance, as the same method can be used with different subclasses.

This example clearly shows how class variables can be used as a configuration mechanism. Subclasses can override these variables to customize their behavior without having to rewrite the methods.

## Design Discussion

Let's consider an alternative approach where we place the type conversions in the `__init__` method:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = str(name)
        self.shares = int(shares)
        self.price = float(price)
```

With this approach, we can create a `Stock` object from a row of data like this:

```python
row = ['AA', '100', '32.20']
s = Stock(*row)
```

Although this approach might seem simpler at first glance, it has several drawbacks:

1. It combines two different concerns: object initialization and data conversion. This makes the code harder to understand and maintain.
2. The `__init__` method becomes less flexible because it always converts the inputs, even if they're already in the correct type.
3. It restricts how subclasses can customize the conversion process. Subclasses would have a harder time changing the conversion logic if it's embedded in the `__init__` method.
4. The code becomes more brittle. If any of the conversions fail, the object can't be created, which can lead to errors in your program.

On the other hand, the class method approach separates these concerns. This makes the code more maintainable and flexible, as each part of the code has a single responsibility.
