# Your first decorator with arguments

The `@logged` decorator you defined earlier always just prints a simple message with the function name. Suppose that you wanted the user to be able to specify a custom message of some sort.

Define a new decorator `@logformat(fmt)` that accepts a format string as an argument and uses `fmt.format(func=func)` to format a supplied function into a log message:

```python
# sample.py
...
from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y
```

To do this, you need to define a decorator that takes an argument. This is what it should look like when you test it:

```python
>>> import sample
Adding logging to add
Adding logging to sub
Adding logging to mul
>>> sample.add(2,3)
Calling add
5
>>> sample.mul(2,3)
sample.py:mul
6
>>>
```

To further simplify the code, show how you can define the original `@logged` decorator using the the `@logformat` decorator.
