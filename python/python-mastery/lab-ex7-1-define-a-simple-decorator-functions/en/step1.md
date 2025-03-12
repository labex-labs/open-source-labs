# Creating Your First Decorator

## What are Decorators?

In Python, decorators are a special syntax that allows you to modify the behavior of functions or methods. A decorator is essentially a function that takes another function as an argument and returns a new function that usually extends or modifies the behavior of the original function.

Decorators are applied using the `@` symbol followed by the decorator name, placed directly above a function definition.

## Creating a Simple Logging Decorator

Let's create a simple decorator that logs information when a function is called. This is a common use case for decorators in real applications.

1. Open the VSCode editor and create a new file named `logcall.py` in the `/home/labex/project` directory.

2. Add the following code to `logcall.py`:

```python
# logcall.py

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Let's understand what this code does:

- `logged` is a decorator function that takes another function (`func`) as an argument
- It prints a message when the decorator is applied to a function
- It defines an inner function `wrapper` that:
  - Prints a message when the decorated function is called
  - Calls the original function with all the arguments
  - Returns the result of the original function
- Finally, it returns the `wrapper` function, which replaces the original function

## Using the Decorator

3. Now, create another file named `sample.py` in the same directory with the following code:

```python
# sample.py

from logcall import logged

@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y
```

The `@logged` syntax tells Python to apply the `logged` decorator to the `add` and `sub` functions.

## Testing the Decorator

4. To test your decorator, open a terminal in VSCode and run the Python interpreter:

```bash
cd /home/labex/project
python3
```

5. In the Python interpreter, import the `sample` module and test the decorated functions:

```python
>>> import sample
Adding logging to add
Adding logging to sub
>>> sample.add(3, 4)
Calling add
7
>>> sample.sub(2, 3)
Calling sub
-1
>>> exit()
```

Notice how the first message ("Adding logging to...") is printed when the module is imported, as that's when the decorator is applied. The second message ("Calling...") is printed each time you call one of the decorated functions.

This simple decorator demonstrates the basic concept - it wraps the original function with additional functionality (logging in this case) without changing the original function's code.
