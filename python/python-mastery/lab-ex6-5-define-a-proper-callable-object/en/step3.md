# Implementing Type Validation with Function Annotations

In Python, you have the ability to add type annotations to function parameters. These annotations serve as a way to indicate the expected data types of the parameters and the return value of a function. They don't enforce the types at runtime by default, but they can be used for validation purposes.

Let's take a look at an example:

```python
def add(x: int, y: int) -> int:
    return x + y
```

In this code, `x: int` and `y: int` tell us that the parameters `x` and `y` should be integers. The `-> int` at the end indicates that the function `add` returns an integer. These type annotations are stored in the function's `__annotations__` attribute, which is a dictionary that maps parameter names to their annotated types.

Now, we're going to enhance our `ValidatedFunction` class to use these type annotations for validation. To do this, we'll need to use Python's `inspect` module. This module provides useful functions to get information about live objects such as modules, classes, methods, functions, etc. In our case, we'll use it to match the function arguments with their corresponding parameter names.

First, we need to modify the `ValidatedFunction` class in the `validate.py` file. You can open this file using the following command:

```bash
code /home/labex/project/validate.py
```

Replace the existing `ValidatedFunction` class with the following improved version:

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

Here's what this enhanced version does:

1. It uses `inspect.signature()` to obtain information about the function's parameters, such as their names, default values, and annotated types.
2. The signature's `bind()` method is used to match the provided arguments to their corresponding parameter names. This helps us associate each argument with its correct parameter in the function.
3. It checks each argument against its type annotation (if one exists). If an annotation is found, it retrieves the validator class from the annotation and applies the validation using the `check()` method.
4. Finally, it calls the original function with the validated arguments.

Now, let's test this enhanced `ValidatedFunction` class with some functions that use our validator classes in their type annotations. Open the `test_validation.py` file using the following command:

```bash
code /home/labex/project/test_validation.py
```

Add the following code to the file:

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

In this code, we define a `greet` function with type annotations `name: String` and `times: Integer`. This means that the `name` parameter should be validated using the `String` class, and the `times` parameter should be validated using the `Integer` class. We then wrap the `greet` function with our `ValidatedFunction` class to enable type validation.

We perform three test cases: a valid call, an invalid call with the wrong type for `name`, and an invalid call with the wrong type for `times`. Each call is wrapped in a `try-except` block to catch any `TypeError` exceptions that may be raised during validation.

To run the test file, use the following command:

```bash
python3 /home/labex/project/test_validation.py
```

You should see output similar to the following:

```
Valid call result: Hello Hello Hello
Expected error for name: Expected <class 'str'>
Expected error for times: Expected <class 'int'>
```

This output demonstrates that our `ValidatedFunction` callable object is now enforcing type validation based on the function annotations. When we pass arguments of the wrong type, the validator classes detect the error and raise a `TypeError`. This way, we can ensure that the functions are called with the correct data types, which helps prevent bugs and makes our code more robust.
