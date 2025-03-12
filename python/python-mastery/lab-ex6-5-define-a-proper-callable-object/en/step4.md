# Challenge: Using a Callable Object as a Method

When a callable object is used as a method in a class, it introduces a special challenge. Let's explore this by creating a `Stock` class with a method that uses our validator:

```bash
code /home/labex/project/stock.py
```

Add the following code:

```python
from validate import ValidatedFunction, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: Integer):
        self.shares -= nshares

    # Try to use ValidatedFunction
    sell = ValidatedFunction(sell)
```

Let's test this class:

```bash
code /home/labex/project/test_stock.py
```

Add the following code:

```python
from stock import Stock

try:
    # Create a stock
    s = Stock('GOOG', 100, 490.1)

    # Get the initial cost
    print(f"Initial shares: {s.shares}")
    print(f"Initial cost: ${s.cost}")

    # Try to sell some shares
    s.sell(10)

    # Check the updated cost
    print(f"After selling, shares: {s.shares}")
    print(f"After selling, cost: ${s.cost}")

except Exception as e:
    print(f"Error: {e}")
```

Run the test file:

```bash
python3 /home/labex/project/test_stock.py
```

You'll likely see an error similar to:

```
Error: missing a required argument: 'nshares'
```

This error occurs because when a method is called, Python automatically passes the instance (`self`) as the first argument. However, our `ValidatedFunction` doesn't account for this.

**Understanding the Problem**

When you define a method inside a class and then replace it with a `ValidatedFunction`, you're wrapping the original method. The issue is that when Python calls a method like `s.sell(10)`, it's actually doing something like `Stock.sell(s, 10)` behind the scenes.

But our wrapped method doesn't automatically handle the `self` parameter correctly, because it doesn't know it's being used as a method.

**Fixing the Problem**

One way to fix this is to modify the `ValidatedFunction` class to handle methods properly. Add the following code to the end of the `validate.py` file:

```python
class ValidatedMethod:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __get__(self, instance, owner):
        # This method is called when the attribute is accessed as a method
        if instance is None:
            return self

        # Return a callable that binds 'self' to the instance
        def method_wrapper(*args, **kwargs):
            return self(instance, *args, **kwargs)

        return method_wrapper

    def __call__(self, instance, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(instance, *args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(instance, *args, **kwargs)
```

Now, modify the `Stock` class to use `ValidatedMethod` instead:

```bash
code /home/labex/project/stock.py
```

Update the `Stock` class:

```python
from validate import ValidatedMethod, Integer

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @ValidatedMethod
    def sell(self, nshares: Integer):
        self.shares -= nshares
```

The `ValidatedMethod` class acts as a descriptor that knows how to handle method calls properly. The `__get__` method is called when the attribute is accessed, and it returns a callable that correctly passes the instance as the first argument.

Run the test file again:

```bash
python3 /home/labex/project/test_stock.py
```

Now you should see output similar to:

```
Initial shares: 100
Initial cost: $49010.0
After selling, shares: 90
After selling, cost: $44109.0
```

This challenge highlighted an important aspect of callable objects: they need special handling when used as methods in a class. By implementing the descriptor protocol with `__get__`, we can create callable objects that work correctly both as standalone functions and as methods.
