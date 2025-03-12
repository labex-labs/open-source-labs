# Understanding `__setattr__` for Attribute Control

In Python, there are special methods that let you customize how attributes of an object are accessed and modified. One such important method is `__setattr__()`. This method comes into play every time you try to assign a value to an attribute of an object. It gives you the ability to have fine - grained control over the attribute assignment process.

## What is `__setattr__`?

The `__setattr__(self, name, value)` method acts as an interceptor for all attribute assignments. When you write a simple assignment statement like `obj.attr = value`, Python doesn't just directly assign the value. Instead, it internally calls `obj.__setattr__("attr", value)`. This mechanism provides you with the power to decide what should happen during the attribute assignment.

Let's now see a practical example of how we can use `__setattr__` to restrict which attributes can be set on a class.

### Step 1: Create a new file

First, open a new file in the WebIDE. You can do this by clicking on the "File" menu and then selecting "New File". Name this file `restricted_stock.py` and save it in the `/home/labex/project` directory. This file will contain the class definition where we'll use `__setattr__` to control attribute assignment.

### Step 2: Add code to `restricted_stock.py`

Add the following code to the `restricted_stock.py` file. This code defines a `RestrictedStock` class.

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

In the `__init__` method, we initialize the object with `name`, `shares`, and `price` attributes. The `__setattr__` method checks if the attribute name being assigned is in the set of allowed attributes (`name`, `shares`, `price`). If it's not, it raises an `AttributeError`. If the attribute is allowed, it uses the parent class's `__setattr__` method to actually set the attribute.

### Step 3: Create a test file

Create a new file called `test_restricted.py` and add the following code to it. This code will test the functionality of the `RestrictedStock` class.

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

In this code, we first import the `RestrictedStock` class. Then we create an instance of the class. We test accessing existing attributes, modifying an existing attribute, and finally, we try to set an invalid attribute to see if the `__setattr__` method works as expected.

### Step 4: Run the test file

Open a terminal in the WebIDE and execute the following commands to run the `test_restricted.py` file:

```bash
cd /home/labex/project
python3 test_restricted.py
```

After running these commands, you should see output similar to this:

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

The `__setattr__` method in our `RestrictedStock` class works in the following steps:

1. It first checks if the attribute name is in the allowed set (`name`, `shares`, `price`).
2. If the attribute name is not in the allowed set, it raises an `AttributeError`. This prevents the assignment of unwanted attributes.
3. If the attribute is allowed, it uses `super().__setattr__()` to actually set the attribute. This ensures that the normal attribute assignment process takes place for the allowed attributes.

This method is more flexible than using `__slots__`, which we saw in previous examples. While `__slots__` can optimize memory usage and restrict attributes, it has limitations when working with inheritance and may conflict with other Python features. Our `__setattr__` approach gives us similar control over attribute assignment without some of those limitations.
