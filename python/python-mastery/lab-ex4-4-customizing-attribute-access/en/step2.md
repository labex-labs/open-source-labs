# Creating Read-Only Objects with Proxies

In this step, we'll learn about proxy classes, a powerful pattern in Python that allows you to wrap an existing object and modify its behavior without changing its original implementation.

## What is a Proxy?

A proxy is an object that acts as an intermediary for another object. The proxy provides the same interface as the original object but can add additional behavior such as access control, logging, or other functionality.

Let's create a read-only proxy that prevents modifications to an object's attributes:

1. Create a new file called `readonly_proxy.py` in the `/home/labex/project` directory with the following code:

```python
class ReadonlyProxy:
    def __init__(self, obj):
        # Store the wrapped object directly in __dict__ to avoid triggering __setattr__
        self.__dict__['_obj'] = obj

    def __getattr__(self, name):
        # Forward attribute access to the wrapped object
        return getattr(self._obj, name)

    def __setattr__(self, name, value):
        # Block all attribute assignments
        raise AttributeError("Cannot modify a read-only object")
```

2. Now create a test file named `test_readonly.py` with the following content:

```python
from stock import Stock
from readonly_proxy import ReadonlyProxy

# Create a normal Stock object
stock = Stock('AAPL', 100, 150.75)
print("Original stock object:")
print(f"Name: {stock.name}")
print(f"Shares: {stock.shares}")
print(f"Price: {stock.price}")
print(f"Cost: {stock.cost}")

# Modify the original stock object
stock.shares = 200
print(f"\nAfter modification - Shares: {stock.shares}")
print(f"After modification - Cost: {stock.cost}")

# Create a read-only proxy around the stock
readonly_stock = ReadonlyProxy(stock)
print("\nRead-only proxy object:")
print(f"Name: {readonly_stock.name}")
print(f"Shares: {readonly_stock.shares}")
print(f"Price: {readonly_stock.price}")
print(f"Cost: {readonly_stock.cost}")

# Try to modify the read-only proxy
try:
    print("\nAttempting to modify the read-only proxy...")
    readonly_stock.shares = 300
except AttributeError as e:
    print(f"Error: {e}")

# Show that the original object is unchanged
print(f"\nOriginal stock shares are still: {stock.shares}")
```

3. Run the test script:

```bash
cd /home/labex/project
python3 test_readonly.py
```

You should see output similar to:

```
Original stock object:
Name: AAPL
Shares: 100
Price: 150.75
Cost: 15075.0

After modification - Shares: 200
After modification - Cost: 30150.0

Read-only proxy object:
Name: AAPL
Shares: 200
Price: 150.75
Cost: 30150.0

Attempting to modify the read-only proxy...
Error: Cannot modify a read-only object

Original stock shares are still: 200
```

## How the Proxy Works

The `ReadonlyProxy` class uses two special methods:

1. `__getattr__(self, name)`: This method is called when an attribute lookup fails (i.e., the attribute isn't found through normal means). Our implementation forwards these lookups to the wrapped object using `getattr()`.

2. `__setattr__(self, name, value)`: This method is called when an attribute assignment is attempted. Our implementation raises an `AttributeError` to prevent any modifications.

3. We directly modify `self.__dict__` in the `__init__` method to store the wrapped object, which avoids triggering our own `__setattr__` method.

This proxy pattern allows us to add a read-only layer around any existing object without modifying its class. The proxy object exhibits all the behaviors of the wrapped object (methods, properties, etc.) but prevents modifications.
