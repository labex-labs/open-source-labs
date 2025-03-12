# Challenge: Using a Callable Object as a Method

In Python, when you use a callable object as a method within a class, there's a unique challenge you need to tackle. A callable object is something you can "call" like a function, such as a function itself or an object with a `__call__` method. When used as a class method, it doesn't always work as expected due to how Python passes the instance (`self`) as the first argument.

Let's explore this issue by creating a `Stock` class. This class will represent a stock with attributes like name, number of shares, and price. We'll also use a validator to ensure the data we're working with is correct.

First, open the `stock.py` file to start writing our `Stock` class. You can use the following command to open the file in an editor:

```bash
code /home/labex/project/stock.py
```

Now, add the following code to the `stock.py` file. This code defines the `Stock` class with an `__init__` method to initialize the stock's attributes, a `cost` property to calculate the total cost, and a `sell` method to reduce the number of shares. We'll also try to use the `ValidatedFunction` to validate the input for the `sell` method.

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

After defining the `Stock` class, we need to test it to see if it works as expected. Create a test file named `test_stock.py` and open it using the following command:

```bash
code /home/labex/project/test_stock.py
```

Add the following code to the `test_stock.py` file. This code creates an instance of the `Stock` class, prints the initial number of shares and cost, tries to sell some shares, and then prints the updated number of shares and cost.

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

Now, run the test file using the following command:

```bash
python3 /home/labex/project/test_stock.py
```

You'll likely encounter an error similar to:

```
Error: missing a required argument: 'nshares'
```

This error occurs because when Python calls a method like `s.sell(10)`, it actually calls `Stock.sell(s, 10)` behind the scenes. The `self` parameter represents the instance of the class, and it's automatically passed as the first argument. However, our `ValidatedFunction` doesn't handle this `self` parameter correctly because it doesn't know it's being used as a method.

**Understanding the Problem**

When you define a method inside a class and then replace it with a `ValidatedFunction`, you're essentially wrapping the original method. The problem is that the wrapped method doesn't automatically handle the `self` parameter correctly. It expects the arguments in a way that doesn't account for the instance being passed as the first argument.

**Fixing the Problem**

To fix this issue, we need to modify the way we handle methods. We'll create a new class called `ValidatedMethod` that can handle method calls properly. Add the following code to the end of the `validate.py` file:

```python
import inspect

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

Now, we need to modify the `Stock` class to use `ValidatedMethod` instead of `ValidatedFunction`. Open the `stock.py` file again:

```bash
code /home/labex/project/stock.py
```

Update the `Stock` class as follows:

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

The `ValidatedMethod` class is a descriptor, which is a special type of object in Python that can change how attributes are accessed. The `__get__` method is called when the attribute is accessed as a method. It returns a callable that correctly passes the instance as the first argument.

Run the test file again using the following command:

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

This challenge has shown you an important aspect of callable objects. When using them as methods in a class, they require special handling. By implementing the descriptor protocol with the `__get__` method, we can create callable objects that work correctly both as standalone functions and as methods.
