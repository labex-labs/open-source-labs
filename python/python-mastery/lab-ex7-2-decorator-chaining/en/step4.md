# Creating a Type Enforcement Decorator with Arguments

In the previous steps, we worked with the `@validated` decorator that enforces type annotations. Now, let's create a more flexible decorator that accepts type specifications as arguments.

## Understanding the Goal

We want to create an `@enforce()` decorator that allows us to specify type constraints as keyword arguments:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

This should behave the same as our previous `@validated` decorator, but with more explicit type specifications.

## Creating the enforce Decorator

1. Open `validate.py` in the WebIDE and add the new decorator:

```python
from functools import wraps

class Integer:
    @classmethod
    def __instancecheck__(cls, x):
        return isinstance(x, int)

def validated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get function annotations
        annotations = func.__annotations__
        # Check arguments against annotations
        for arg_name, arg_value in zip(func.__code__.co_varnames, args):
            if arg_name in annotations and not isinstance(arg_value, annotations[arg_name]):
                raise TypeError(f'Expected {arg_name} to be {annotations[arg_name].__name__}')

        # Run the function and get the result
        result = func(*args, **kwargs)

        # Check the return value
        if 'return' in annotations and not isinstance(result, annotations['return']):
            raise TypeError(f'Expected return value to be {annotations["return"].__name__}')

        return result
    return wrapper

def enforce(**type_specs):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Check argument types
            for arg_name, arg_value in zip(func.__code__.co_varnames, args):
                if arg_name in type_specs and not isinstance(arg_value, type_specs[arg_name]):
                    raise TypeError(f'Expected {arg_name} to be {type_specs[arg_name].__name__}')

            # Run the function and get the result
            result = func(*args, **kwargs)

            # Check the return value
            if 'return_' in type_specs and not isinstance(result, type_specs['return_']):
                raise TypeError(f'Expected return value to be {type_specs["return_"].__name__}')

            return result
        return wrapper
    return decorator
```

2. Let's test our new `@enforce` decorator:

```bash
cd ~/project
python3 -c "from validate import enforce, Integer

@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

# This should work
print(add(2, 3))

# This should raise a TypeError
try:
    print(add('2', 3))
except TypeError as e:
    print(f'Error: {e}')

# This should raise a TypeError
try:
    @enforce(x=Integer, y=Integer, return_=Integer)
    def bad_add(x, y):
        return str(x + y)
    print(bad_add(2, 3))
except TypeError as e:
    print(f'Error: {e}')"
```

You should see output similar to:

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

## Comparing the Two Approaches

Both decorators achieve the same goal, but in different ways:

1. `@validated` uses Python's built-in type annotations:

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

2. `@enforce` uses keyword arguments to specify types:
   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

Each approach has its advantages:

- Type annotations are built into Python and provide better IDE support
- The `@enforce` approach is more explicit and can be used with libraries that depend on other annotation systems
