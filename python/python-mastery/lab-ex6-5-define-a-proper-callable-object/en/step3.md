# Implementing Type Validation with Function Annotations

Python allows you to add type annotations to function parameters. For example:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Here, `x: int` and `y: int` indicate that `x` and `y` should be integers, and `-> int` indicates that the function returns an integer. These annotations are stored in the function's `__annotations__` attribute.

We'll now enhance our `ValidatedFunction` class to use these annotations for validation. We'll need to use Python's `inspect` module to help us match function arguments with their parameter names.

Modify the `ValidatedFunction` class in `validate.py`:

```bash
code /home/labex/project/validate.py
```

Replace the `ValidatedFunction` class with this improved version:

```python
import inspect

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)

    def __call__(self, *args, **kwargs):
        # Bind the arguments to the function parameters
        bound = self.signature.bind(*args, **kwargs)

        # Validate each argument against its annotation
        for name, val in bound.arguments.items():
            if name in self.func.__annotations__:
                # Get the validator class from the annotation
                validator = self.func.__annotations__[name]
                # Apply the validation
                validator.check(val)

        # Call the function with the validated arguments
        return self.func(*args, **kwargs)
```

This enhanced version:

1. Uses `inspect.signature()` to get information about the function's parameters
2. Uses the signature's `bind()` method to match the provided arguments to their parameter names
3. Checks each argument against its annotation (if it has one)
4. Calls the function with the validated arguments

Now let's test this with annotations that use our validator classes:

```bash
code /home/labex/project/test_validation.py
```

Add the following code:

```python
from validate import ValidatedFunction, Integer, String

def greet(name: String, times: Integer):
    return name * times

# Wrap the greet function with ValidatedFunction
validated_greet = ValidatedFunction(greet)

# Valid call
try:
    result = validated_greet("Hello ", 3)
    print(f"Valid call result: {result}")
except TypeError as e:
    print(f"Unexpected error: {e}")

# Invalid call - wrong type for 'name'
try:
    result = validated_greet(123, 3)
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for name: {e}")

# Invalid call - wrong type for 'times'
try:
    result = validated_greet("Hello ", "3")
    print(f"Invalid call unexpectedly succeeded: {result}")
except TypeError as e:
    print(f"Expected error for times: {e}")
```

Run the test file:

```bash
python3 /home/labex/project/test_validation.py
```

You should see output similar to:

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

This demonstrates that our `ValidatedFunction` callable object is now enforcing type validation based on the function annotations!

The annotations (`name: String, times: Integer`) specify that `name` should be validated with the `String` class and `times` with the `Integer` class. When we call the function with invalid types, our validator classes detect the error and raise a `TypeError`.
