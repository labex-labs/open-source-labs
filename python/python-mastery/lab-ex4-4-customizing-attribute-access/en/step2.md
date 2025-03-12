# Creating Read-Only Objects with Proxies

In this step, we're going to explore proxy classes, a very useful pattern in Python. Proxy classes let you take an existing object and change how it behaves without altering its original code. This is like putting a special wrapper around an object to add new features or restrictions.

## What is a Proxy?

A proxy is an object that stands between you and another object. It has the same set of functions and properties as the original object, but it can do extra things. For example, it can control who can access the object, keep a record of actions (logging), or add other useful features.

Let's create a read - only proxy. This kind of proxy will stop you from changing the attributes of an object.

### Step 1: Create the Read - Only Proxy Class

First, we need to create a Python file that defines our read - only proxy.

1. Navigate to the `/home/labex/project` directory.
2. Create a new file named `readonly_proxy.py` in this directory.
3. Open the `readonly_proxy.py` file and add the following code:

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

In this code, the `ReadonlyProxy` class is defined. The `__init__` method stores the object we want to wrap. We use `self.__dict__` to store it directly to avoid calling the `__setattr__` method. The `__getattr__` method is used when we try to access an attribute of the proxy. It simply passes the request to the wrapped object. The `__setattr__` method is called when we try to change an attribute. It raises an error to prevent any changes.

### Step 2: Create a Test File

Now, we'll create a test file to see how our read - only proxy works.

1. Create a new file named `test_readonly.py` in the same `/home/labex/project` directory.
2. Add the following code to the `test_readonly.py` file:

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

In this test code, we first create a normal `Stock` object and print its information. Then we modify one of its attributes and print the updated information. Next, we create a read - only proxy for the `Stock` object and print its information. Finally, we try to modify the read - only proxy and expect to get an error.

### Step 3: Run the Test Script

After creating the proxy class and the test file, we need to run the test script to see the results.

1. Open a terminal and navigate to the `/home/labex/project` directory using the following command:

```bash
cd /home/labex/project
```

2. Run the test script using the following command:

```bash
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

The `ReadonlyProxy` class uses two special methods to achieve its read - only functionality:

1. `__getattr__(self, name)`: This method is called when Python can't find an attribute in the normal way. In our `ReadonlyProxy` class, we use the `getattr()` function to pass the attribute access request to the wrapped object. So, when you try to access an attribute of the proxy, it will actually get the attribute from the wrapped object.

2. `__setattr__(self, name, value)`: This method is called when you try to assign a value to an attribute. In our implementation, we raise an `AttributeError` to stop any changes from being made to the proxy's attributes.

3. In the `__init__` method, we directly modify `self.__dict__` to store the wrapped object. This is important because if we used the normal way to assign the object, it would call the `__setattr__` method, which would raise an error.

This proxy pattern allows us to add a read - only layer around any existing object without changing its original class. The proxy object acts just like the wrapped object, but it won't let you make any modifications.
