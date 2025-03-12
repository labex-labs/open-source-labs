# Creating Decorators with Arguments

So far, our `@logged` decorator always prints a fixed message. What if we want to customize the message format? Let's create a new decorator that accepts arguments.

## Understanding Parameterized Decorators

A parameterized decorator is essentially a function that returns a decorator. The general structure is:

```python
def decorator_with_args(arg1, arg2, ...):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use arg1, arg2, ... here
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return actual_decorator
```

When you use `@decorator_with_args(value1, value2)`, Python first calls `decorator_with_args(value1, value2)` to get the actual decorator, then applies that decorator to the function.

## Creating the logformat Decorator

Let's create a `@logformat(fmt)` decorator that accepts a format string as an argument:

1. Open `logcall.py` in the WebIDE and add the new decorator:

```python
from functools import wraps

def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

2. Now, let's test our new decorator by modifying `sample.py`:

```python
from logcall import logged, logformat

@logged
def add(x, y):
    "Adds two numbers"
    return x + y

@logged
def sub(x, y):
    "Subtracts y from x"
    return x - y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x, y):
    "Multiplies two numbers"
    return x * y
```

3. Run the updated `sample.py` to see the results:

```bash
cd ~/project
python3 -c "import sample; print(sample.add(2, 3)); print(sample.mul(2, 3))"
```

You should see output similar to:

```
Calling add
5
sample.py:mul
6
```

## Redefining the logged Decorator Using logformat

Now that we have a more flexible `logformat` decorator, we can redefine our original `logged` decorator using it:

1. Update `logcall.py` with the following code:

```python
from functools import wraps

def logformat(fmt):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Define logged using logformat
logged = lambda func: logformat("Calling {func.__name__}")(func)
```

2. Test that the redefined `logged` decorator still works:

```bash
cd ~/project
python3 -c "from logcall import logged; @logged
def greet(name):
    return f'Hello, {name}'
    
print(greet('World'))"
```

You should see:

```
Calling greet
Hello, World
```

This approach allows us to reuse code and maintain a consistent logging format across different decorators.
