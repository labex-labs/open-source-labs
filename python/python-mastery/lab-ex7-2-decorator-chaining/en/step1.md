# Preserving Function Metadata in Decorators

When you use a decorator to wrap a function, the original function's metadata (like name, documentation string, and annotations) is lost by default. Let's verify this issue first.

Open your terminal in the WebIDE and run the following Python commands:

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

You'll see output similar to this:

```
<function wrapper at 0x...>
None
```

Notice that the function name appears as `wrapper` instead of `add`, and the docstring is `None` instead of `'Adds two things'`. This is a problem when using introspection tools or generating documentation.

## Fixing the Problem with functools.wraps

Python's `functools` module provides a `wraps` decorator that can help preserve function metadata. Let's modify our `logged` decorator:

1. Open the `logcall.py` file in the WebIDE:

```bash
cd ~/project
```

2. Update the `logged` decorator in `logcall.py` with the following code:

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. The `@wraps(func)` decorator copies all metadata from the original function to the wrapper function.

4. Let's test our improved decorator:

```bash
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

Now you should see:

```
<function add at 0x...>
Adds two things
```

Great! The function name and docstring are preserved.

## Fixing the validate.py Decorator

Now, let's apply the same fix to the `validated` decorator in `validate.py`:

1. Open `validate.py` in the WebIDE

2. Update the `validated` decorator with the `@wraps` decorator:

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
```

3. Let's test that our `validated` decorator now preserves metadata:

```bash
python3 -c "from validate import validated, Integer; @validated
def multiply(x: Integer, y: Integer) -> Integer:
    'Multiplies two integers'
    return x * y
    
print(multiply)
print(multiply.__doc__)"
```

You should see:

```
<function multiply at 0x...>
Multiplies two integers
```

Now both decorators properly preserve the metadata of the functions they decorate.
