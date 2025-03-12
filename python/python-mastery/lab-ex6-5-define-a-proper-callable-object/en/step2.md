# Creating a Basic Callable Object

In Python, a callable object is an object that can be used just like a function. You can think of it as something that you can "call" by putting parentheses after it, similar to how you call a regular function. To make a class in Python act like a callable object, we need to implement a special method called `__call__`. This method gets automatically invoked when you use the object with parentheses, just like when you call a function.

Let's start by modifying the `validate.py` file. We're going to add a new class called `ValidatedFunction` to this file, and this class will be our callable object. To open the file in the code editor, run the following command in the terminal:

```bash
code /home/labex/project/validate.py
```

Once the file is open, scroll to the end of it and add the following code:

```python
class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Calling', self.func)
        result = self.func(*args, **kwargs)
        return result
```

Let's break down what this code does. The `ValidatedFunction` class has an `__init__` method, which is the constructor. When you create an instance of this class, you pass a function to it. This function is then stored as an attribute of the instance, named `self.func`.

The `__call__` method is the key part that makes this class callable. When you call an instance of the `ValidatedFunction` class, this `__call__` method gets executed. Here's what it does step by step:

1. It prints a message that tells you which function is being called. This is useful for debugging and understanding what's going on.
2. It calls the function that was stored in `self.func` with the arguments that you passed when you called the instance. The `*args` and `**kwargs` allow you to pass any number of positional and keyword arguments.
3. It returns the result of the function call.

Now, let's test this `ValidatedFunction` class. We'll create a new file called `test_callable.py` to write our test code. To open this new file in the code editor, run the following command:

```bash
code /home/labex/project/test_callable.py
```

Add the following code to the `test_callable.py` file:

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

In this code, we first import the `ValidatedFunction` class from the `validate.py` file. Then we define a simple function called `add` that takes two numbers and returns their sum.

We create an instance of the `ValidatedFunction` class, passing the `add` function to it. This "wraps" the `add` function inside the `ValidatedFunction` instance.

We then call the wrapped function twice, once with the arguments `2` and `3`, and then with `10` and `20`. Each time we call the wrapped function, the `__call__` method of the `ValidatedFunction` class is invoked, which in turn calls the original `add` function.

To run the test code, execute the following command in the terminal:

```bash
python3 /home/labex/project/test_callable.py
```

You should see output similar to this:

```
Calling <function add at 0x7f2d1c3a9940>
Result: 5
Calling <function add at 0x7f2d1c3a9940>
Result: 30
```

This output shows that our callable object is working as expected. When we call `validated_add(2, 3)`, it's actually calling the `__call__` method of the `ValidatedFunction` class, which then calls the original `add` function.

Right now, our `ValidatedFunction` class just prints a message and passes the call to the original function. In the next step, we'll improve this class to perform type validation based on the function's annotations.
