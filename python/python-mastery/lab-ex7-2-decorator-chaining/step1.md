# Copying Metadata

When a function gets wrapped by a decorator, you often lose
information about the name of the function, documentation strings, and
other details. Verify this:

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function wrapper at 0x4439b0>
>>> help(add)
... look at the output ...
>>>
```

Fix the definition of the `logged` decorator so that it copies
function metadata properly. To do this, use the `@wraps(func)`
decorator as shown in the notes.

After you're done, make sure the decorator preserves the function name
and doc string.

```python
>>> @logged
    def add(x,y):
        'Adds two things'
        return x+y

>>> add
<function add at 0x4439b0>
>>> add.__doc__
'Adds two things'
>>>
```

Fix the `@validated` decorator you wrote earlier so that it also preserves
metadata using `@wraps(func)`.
