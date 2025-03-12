# Creating a Basic Callable Object

A callable object in Python is an object that can be called like a function. To make a class callable, we need to implement the special `__call__` method, which is invoked when the object is called with parentheses.

Let's modify the `validate.py` file to add a `ValidatedFunction` class that will be a callable object:

```bash
code /home/labex/project/validate.py
```

Add the following code at the end of the file:

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

This class takes a function in its constructor and stores it as `self.func`. The `__call__` method is invoked when an instance of this class is called, and it:

1. Prints a message indicating which function is being called
2. Calls the stored function with the provided arguments
3. Returns the result of the function call

Let's test this class by creating a new file called `test_callable.py`:

```bash
code /home/labex/project/test_callable.py
```

Add the following code:

```python
from validate import ValidatedFunction

def add(x, y):
    return x + y

# Wrap the add function with ValidatedFunction
validated_add = ValidatedFunction(add)

# Call the wrapped function
result = validated_add(2, 3)
print(f"Result: {result}")

# Try another call
result = validated_add(10, 20)
print(f"Result: {result}")
```

Run the test file:

```bash
python3 /home/labex/project/test_callable.py
```

You should see output similar to:

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

This output shows that our callable object is working! When we call `validated_add(2, 3)`, it's actually invoking the `__call__` method of our `ValidatedFunction` class, which then calls the original `add` function.

The current implementation just prints a message and forwards the call to the original function. In the next step, we'll enhance this to perform type validation based on function annotations.
