# Building a Validation Decorator

In this step, we're going to create a more practical decorator. A decorator in Python is a special type of function that can modify another function's behavior. The decorator we'll create will validate function arguments based on type annotations. Type annotations are a way to specify the expected data types of a function's arguments and return value. This is a common use case in real - world applications because it helps ensure that functions receive the correct input types, which can prevent many bugs.

## Understanding the Validation Classes

We've already created a file called `validate.py` for you, and it contains some validation classes. Validation classes are used to check if a value meets certain criteria. To see what's inside this file, you need to open it in the VSCode editor. You can do this by running the following commands in the terminal:

```bash
cd /home/labex/project
code validate.py
```

The file has three classes:

1. `Validator` - This is a base class. A base class provides a general framework or structure that other classes can inherit from. In this case, it provides the basic structure for validation.
2. `Integer` - This validator class is used to make sure that a value is an integer. If you pass a non - integer value to a function that uses this validator, it will raise an error.
3. `PositiveInteger` - This validator class ensures that a value is a positive integer. So, if you pass a negative integer or zero, it will also raise an error.

## Adding the Validation Decorator

Now, we're going to add a decorator function named `validated` to the `validate.py` file. This decorator will perform several important tasks:

1. It will inspect a function's type annotations. Type annotations are like little notes that tell us what kind of data the function expects.
2. It will validate the arguments passed to the function against these type annotations. This means it will check if the values passed to the function are of the correct type.
3. It will also validate the return value of the function against its annotation. So, it makes sure that the function returns the type of data it's supposed to.
4. If the validation fails, it will raise informative error messages. These messages will tell you exactly what went wrong, like which argument had the wrong type.

Add the following code to the end of the `validate.py` file:

```python
# Add to validate.py

import inspect
import functools

def validated(func):
    sig = inspect.signature(func)

    print(f'Validating {func.__name__} {sig}')

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Bind arguments to the signature
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Validate each argument
        for name, value in bound.arguments.items():
            if name in sig.parameters:
                param = sig.parameters[name]
                if param.annotation != inspect.Parameter.empty:
                    try:
                        # Create an instance of the validator and validate the value
                        if isinstance(param.annotation, type) and issubclass(param.annotation, Validator):
                            validator = param.annotation()
                            bound.arguments[name] = validator.validate(value)
                    except Exception as e:
                        errors.append(f'    {name}: {e}')

        # If validation errors, raise an exception
        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        # Call the function
        result = func(*bound.args, **bound.kwargs)

        # Validate the return value
        if sig.return_annotation != inspect.Signature.empty:
            try:
                if isinstance(sig.return_annotation, type) and issubclass(sig.return_annotation, Validator):
                    validator = sig.return_annotation()
                    result = validator.validate(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None

        return result

    return wrapper
```

This code uses Python's `inspect` module. The `inspect` module allows us to get information about live objects, like functions. Here, we use it to examine the function's signature and validate arguments based on type annotations. We also use `functools.wraps`. This is a helper function that preserves the original function's metadata, such as its name and docstring. Metadata is like extra information about the function that helps us understand what it does.

## Testing the Validation Decorator

Let's create a file to test our validation decorator. We'll create a new file called `test_validate.py` and add the following code to it:

```python
# test_validate.py

from validate import Integer, PositiveInteger, validated

@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y

@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x ** y

# Test with a class
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

Now, we'll test our decorator in the Python interpreter. First, navigate to the project directory and start the Python interpreter by running these commands in the terminal:

```bash
cd /home/labex/project
python3
```

Then, in the Python interpreter, we can run the following code to test our decorator:

```python
>>> from test_validate import add, pow, Stock
Validating add (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating pow (x: validate.Integer, y: validate.Integer) -> validate.Integer
Validating sell (self, nshares: validate.PositiveInteger) -> <class 'inspect._empty'>
>>>
>>> # Test with valid inputs
>>> add(2, 3)
5
>>>
>>> # Test with invalid inputs
>>> add('2', '3')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    x: Expected <class 'int'>
    y: Expected <class 'int'>
>>>
>>> # Test valid power
>>> pow(2, 3)
8
>>>
>>> # Test with negative exponent (produces non - integer result)
>>> pow(2, -1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 83, in wrapper
    raise TypeError(f'Bad return: {e}') from None
TypeError: Bad return: Expected <class 'int'>
>>>
>>> # Test with a class
>>> s = Stock("GOOG", 100, 490.1)
>>> s.sell(50)
>>> s.shares
50
>>>
>>> # Test with invalid shares
>>> s.sell(-10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/labex/project/validate.py", line 75, in wrapper
    raise TypeError('Bad Arguments\n' + '\n'.join(errors))
TypeError: Bad Arguments
    nshares: Expected value > 0
>>> exit()
```

As you can see, our `validated` decorator has successfully enforced type checking on function arguments and return values. This is very useful because it makes our code more robust. Instead of letting type errors propagate deeper into the code and cause hard - to - find bugs, we catch them at the function boundaries.
