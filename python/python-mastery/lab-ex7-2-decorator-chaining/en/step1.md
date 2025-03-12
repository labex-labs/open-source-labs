# Preserving Function Metadata in Decorators

In Python, decorators are a powerful tool that allows you to modify the behavior of functions. However, when you use a decorator to wrap a function, there's a little problem. By default, the original function's metadata, such as its name, documentation string (docstring), and annotations, gets lost. Metadata is important because it helps in introspection (examining the code's structure) and generating documentation. Let's first verify this issue.

Open your terminal in the WebIDE. We'll run some Python commands to see what happens when we use a decorator. The following commands will create a simple function `add` wrapped with a decorator and then print the function and its docstring.

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def add(x,y):
    'Adds two things'
    return x+y
    
print(add)
print(add.__doc__)"
```

When you run these commands, you'll see output similar to this:

```
<function wrapper at 0x...>
None
```

Notice that instead of showing the function name as `add`, it shows `wrapper`. And the docstring, which should be `'Adds two things'`, is `None`. This can be a big problem when you're using tools that rely on this metadata, like introspection tools or documentation generators.

## Fixing the Problem with functools.wraps

Python's `functools` module comes to the rescue. It provides a `wraps` decorator that can help us preserve the function metadata. Let's see how we can modify our `logged` decorator to use `wraps`.

1. First, open the `logcall.py` file in the WebIDE. You can navigate to the project directory using the following command in the terminal:

```bash
cd ~/project
```

2. Now, update the `logged` decorator in `logcall.py` with the following code. The `@wraps(func)` decorator is the key here. It copies all the metadata from the original function `func` to the wrapper function.

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper
```

3. The `@wraps(func)` decorator does an important job. It takes all the metadata (like the name, docstring, and annotations) from the original function `func` and attaches it to the `wrapper` function. This way, when we use the decorated function, it will have the correct metadata.

4. Let's test our improved decorator. Run the following commands in the terminal:

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

Great! The function name and docstring are preserved. This means that our decorator is now working as expected, and the metadata of the original function is intact.

## Fixing the validate.py Decorator

Now, let's apply the same fix to the `validated` decorator in `validate.py`. This decorator is used to validate the types of function arguments and the return value based on the function's annotations.

1. Open `validate.py` in the WebIDE.

2. Update the `validated` decorator with the `@wraps` decorator. The following code shows how to do it. The `@wraps(func)` decorator is added to the `wrapper` function inside the `validated` decorator to preserve the metadata.

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

3. Let's test that our `validated` decorator now preserves metadata. Run the following commands in the terminal:

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
<function multiply at 0......>
Multiplies two integers
```

Now both decorators, `logged` and `validated`, properly preserve the metadata of the functions they decorate. This ensures that when you use these decorators, the functions will still have their original names, docstrings, and annotations, which is very useful for code readability and maintainability.
