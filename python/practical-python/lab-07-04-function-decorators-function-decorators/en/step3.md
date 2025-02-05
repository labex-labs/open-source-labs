# Code that makes logging

Perhaps you can make a function that makes functions with logging added to them. A wrapper.

```python
def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Now use it.

```python
def add(x, y):
    return x + y

logged_add = logged(add)
```

What happens when you call the function returned by `logged`?

```python
logged_add(3, 4)      # You see the logging message appear
```

This example illustrates the process of creating a so-called _wrapper function_.

A wrapper is a function that wraps around another function with some extra bits of processing, but otherwise works in the exact same way as the original function.

```python
>>> logged_add(3, 4)
Calling add   # Extra output. Added by the wrapper
7
>>>
```

_Note: The `logged()` function creates the wrapper and returns it as a result._
