# Understanding `__setattr__` for Attribute Control

Python provides special methods that allow you to customize how attributes are accessed and modified. One of these methods is `__setattr__()`, which is called whenever an attribute assignment is attempted on an object.

## What is `__setattr__`?

The `__setattr__(self, name, value)` method intercepts all attribute assignments. When you write `obj.attr = value`, Python internally calls `obj.__setattr__("attr", value)`. This gives you the power to control what happens during attribute assignment.

Let's see how we can use `__setattr__` to restrict which attributes can be set on a class:

1. Open a new file in the WebIDE by clicking on the "File" menu and selecting "New File". Name it `restricted_stock.py` and save it in the `/home/labex/project` directory.

2. Add the following code to `restricted_stock.py`:

```python
class RestrictedStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __setattr__(self, name, value):
        # Only allow specific attributes
        if name not in {'name', 'shares', 'price'}:
            raise AttributeError(f'Cannot set attribute {name}')

        # If attribute is allowed, set it using the parent method
        super().__setattr__(name, value)
```

3. Create a new file called `test_restricted.py` with the following code:

```python
from restricted_stock import RestrictedStock

# Create a new stock
stock = RestrictedStock('GOOG', 100, 490.1)

# Test accessing existing attributes
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")

# Test modifying an existing attribute
print("\nChanging shares to 75...")
stock.shares = 75
print(f"New shares value: {stock.shares}")

# Test setting an invalid attribute
try:
    print("\nTrying to set an invalid attribute 'share'...")
    stock.share = 50
except AttributeError as e:
    print(f"Error: {e}")
```

4. Run the `test_restricted.py` file by opening a terminal in the WebIDE and executing:

```bash
cd /home/labex/project
python3 test_restricted.py
```

You should see output similar to this:

```
Name: GOOG
Shares: 100
Price: 490.1

Changing shares to 75...
New shares value: 75

Trying to set an invalid attribute 'share'...
Error: Cannot set attribute share
```

## How It Works

The `__setattr__` method in our `RestrictedStock` class:

1. Checks if the attribute name is in the allowed set (`name`, `shares`, `price`)
2. If not, it raises an `AttributeError`
3. If the attribute is allowed, it uses `super().__setattr__()` to actually set the attribute

This method is more flexible than using `__slots__`, which we saw in previous examples. While `__slots__` optimizes memory usage and restricts attributes, it has limitations when working with inheritance and may conflict with other Python features.

Our `__setattr__` approach gives us similar control without some of those limitations.
