# Creating a Type Enforcement Decorator with Arguments

In the previous steps, we learned about the `@validated` decorator. This decorator is used to enforce type annotations in Python functions. Type annotations are a way to specify the expected types of function arguments and return values. Now, we're going to take it a step further. We'll create a more flexible decorator that can accept type specifications as arguments. This means we can define the types we want for each argument and the return value in a more explicit way.

## Understanding the Goal

Our goal is to create an `@enforce()` decorator. This decorator will allow us to specify type constraints using keyword arguments. Here's an example of how it will work:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

In this example, we're using the `@enforce` decorator to specify that the `x` and `y` arguments of the `add` function should be of type `Integer`, and the return value should also be of type `Integer`. This decorator will behave similarly to our previous `@validated` decorator, but it gives us more control over the type specifications.

## Creating the enforce Decorator

1. First, open the `validate.py` file in the WebIDE. We'll add our new decorator to this file. Here's the code we'll add:

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

Let's break down what this code does. The `Integer` class is used to define a custom type. The `validated` decorator checks the types of function arguments and the return value based on the function's type annotations. The `enforce` decorator is the new one we're creating. It takes keyword arguments that specify the types for each argument and the return value. Inside the `wrapper` function of the `enforce` decorator, we check if the types of the arguments and the return value match the specified types. If not, we raise a `TypeError`.

2. Now, let's test our new `@enforce` decorator. We'll run some test cases to see if it works as expected. Here's the code to run the tests:

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

In this test code, we first define an `add` function with the `@enforce` decorator. We then call the `add` function with valid arguments, which should work without any errors. Next, we call the `add` function with an invalid argument, which should raise a `TypeError`. Finally, we define a `bad_add` function that returns a value of the wrong type, which should also raise a `TypeError`.

When you run this test code, you should see output similar to the following:

```
5
Error: Expected x to be Integer
Error: Expected return value to be Integer
```

This output shows that our `@enforce` decorator is working correctly. It raises a `TypeError` when the types of the arguments or the return value don't match the specified types.

## Comparing the Two Approaches

Both the `@validated` and `@enforce` decorators achieve the same goal of enforcing type constraints, but they do it in different ways.

1. The `@validated` decorator uses Python's built-in type annotations. Here's an example:

   ```python
   @validated
   def add(x: Integer, y: Integer) -> Integer:
       return x + y
   ```

   With this approach, we specify the types directly in the function definition using type annotations. This is a built-in feature of Python, and it provides better support in Integrated Development Environments (IDEs). IDEs can use these type annotations to provide code completion, type checking, and other helpful features.

2. The `@enforce` decorator, on the other hand, uses keyword arguments to specify the types. Here's an example:

   ```python
   @enforce(x=Integer, y=Integer, return_=Integer)
   def add(x, y):
       return x + y
   ```

   This approach is more explicit because we're directly passing the type specifications as arguments to the decorator. It can be useful when working with libraries that rely on other annotation systems.

Each approach has its own advantages. Type annotations are a native part of Python and offer better IDE support, while the `@enforce` approach gives us more flexibility and explicitness. You can choose the approach that best suits your needs depending on the project you're working on.
