# Creating Your First Decorator

## What are Decorators?

In Python, decorators are a special syntax that can be quite useful for beginners. They allow you to modify the behavior of functions or methods. Think of a decorator as a function that takes another function as an input. It then returns a new function. This new function often extends or changes the behavior of the original function.

Decorators are applied using the `@` symbol. You place this symbol followed by the decorator name directly above a function definition. This is a simple way to tell Python that you want to use the decorator on that particular function.

## Creating a Simple Logging Decorator

Let's create a simple decorator that logs information when a function is called. Logging is a common task in real - world applications, and using a decorator for this is a great way to understand how they work.

1. First, open the VSCode editor. In the `/home/labex/project` directory, create a new file named `logcall.py`. This file will hold our decorator function.

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

Let's break down what this code does:

- The `logged` function is our decorator. It takes another function, which we call `func`, as an argument. This `func` is the function that we want to add logging to.
- When the decorator is applied to a function, it prints a message. This message tells us that logging is being added to the function with the given name.
- Inside the `logged` function, we define an inner function called `wrapper`. This `wrapper` function is what will replace the original function.
  - When the decorated function is called, the `wrapper` function prints a message saying that the function is being called.
  - It then calls the original function (`func`) with all the arguments that were passed to it. The `*args` and `**kwargs` are used to accept any number of positional and keyword arguments.
  - Finally, it returns the result of the original function.
- The `logged` function returns the `wrapper` function. This `wrapper` function will now be used instead of the original function, adding the logging functionality.

## Using the Decorator

3. Now, in the same directory (`/home/labex/project`), create another file named `sample.py` with the following code:

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

The `@logged` syntax is very important here. It tells Python to apply the `logged` decorator to the `add` and `sub` functions. So, whenever these functions are called, the logging functionality added by the decorator will be executed.

## Testing the Decorator

4. To test your decorator, open a terminal in VSCode. First, change the directory to the project directory using the following command:

```bash
cd /home/labex/project
```

Then, start the Python interpreter:

```bash
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

Notice that when you import the `sample` module, the messages "Adding logging to..." are printed. This is because the decorator is applied when the module is imported. Each time you call one of the decorated functions, the "Calling..." message is printed. This shows that the decorator is working as expected.

This simple decorator demonstrates the basic concept of decorators. It wraps the original function with additional functionality (logging in this case) without changing the original function's code. This is a powerful feature in Python that you can use in many different scenarios.
