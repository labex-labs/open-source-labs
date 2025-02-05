# Combining both

A function can also accept any number of variable keyword and non-keyword arguments.

```python
def f(*args, **kwargs):
    ...
```

Function call.

```python
f(2, 3, flag=True, mode='fast', header='debug')
```

The arguments are separated into positional and keyword components

```python
def f(*args, **kwargs):
    # args = (2, 3)
    # kwargs -> { 'flag': True, 'mode': 'fast', 'header': 'debug' }
    ...
```

This function takes any combination of positional or keyword arguments. It is sometimes used when writing wrappers or when you want to pass arguments through to another function.
