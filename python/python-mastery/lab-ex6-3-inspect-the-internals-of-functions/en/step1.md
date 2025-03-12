# Exploring Function Attributes

In Python, functions are first-class objects, which means they have attributes just like any other object. These attributes can provide valuable information about the function itself.

Let's start by opening a Python interactive shell to explore function attributes:

```bash
cd ~/project
python3
```

Now, define a simple function that adds two numbers:

```python
def add(x, y):
    'Adds two things'
    return x + y
```

## Using dir() to Inspect Function Attributes

The `dir()` function in Python returns a list of all attributes and methods of an object. Let's use it to see what attributes our function has:

```python
dir(add)
```

You should see output similar to:

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

## Accessing Basic Function Information

Let's examine some of the basic function attributes:

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

Output:

```
add
__main__
Adds two things
```

These attributes tell us:

- `__name__`: The name of the function
- `__module__`: The module where the function is defined
- `__doc__`: The function's documentation string (docstring)

## Examining Function Code

The `__code__` attribute contains information about the function implementation, including its bytecode and other details:

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

Output:

```
('x', 'y')
2
```

This shows:

- `co_varnames`: A tuple of local variable names used by the function
- `co_argcount`: The number of arguments the function expects

Try exploring more attributes of the `__code__` object:

```python
dir(add.__code__)
```

This will display all attributes of the code object, which contains low-level details about the function's implementation.
