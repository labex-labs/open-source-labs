# Creating Decorators with Arguments

So far, we've been using the `@logged` decorator, which always prints a fixed message. But what if you want to customize the message format? In this section, we'll learn how to create a new decorator that can accept arguments, giving you more flexibility in how you use decorators.

## Understanding Parameterized Decorators

A parameterized decorator is a special type of function. Instead of directly modifying another function, it returns a decorator. The general structure of a parameterized decorator looks like this:

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

When you use `@decorator_with_args(value1, value2)` in your code, Python first calls `decorator_with_args(value1, value2)`. This call returns the actual decorator, which is then applied to the function that follows the `@` syntax. This two - step process is key to how parameterized decorators work.

## Creating the logformat Decorator

Let's create a `@logformat(fmt)` decorator that takes a format string as an argument. This will allow us to customize the logging message.

1. Open `logcall.py` in the WebIDE and add the new decorator. The code below shows how to define both the existing `logged` decorator and the new `logformat` decorator:

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

In the `logformat` decorator, the outer function `logformat` takes a format string `fmt` as an argument. It then returns the `decorator` function, which is the actual decorator that modifies the target function.

2. Now, let's test our new decorator by modifying `sample.py`. The following code shows how to use both the `logged` and `logformat` decorators on different functions:

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

Here, the `add` and `sub` functions use the `logged` decorator, while the `mul` function uses the `logformat` decorator with a custom format string.

3. Run the updated `sample.py` to see the results. Open your terminal and run the following command:

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

This output shows that the `logged` decorator prints the function name as expected, and the `logformat` decorator uses the custom format string to print the file name and function name.

## Redefining the logged Decorator Using logformat

Now that we have a more flexible `logformat` decorator, we can redefine our original `logged` decorator using it. This will help us reuse code and maintain a consistent logging format.

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

Here, we use a lambda function to define the `logged` decorator in terms of the `logformat` decorator. The lambda function takes a function `func` and applies the `logformat` decorator with a specific format string.

2. Test that the redefined `logged` decorator still works. Open your terminal and run the following command:

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

This shows that the redefined `logged` decorator works as expected, and we've successfully reused the `logformat` decorator to achieve a consistent logging format.
