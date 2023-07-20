# Frame Hacking

One complaint about the last part is that the `__init__()` function
now looks pretty weird with that call to `locals()` inserted into it.
You can get around that though if you're willing to do a bit of stack
frame hacking. Try this variant of the `_init()` function:

```python
>>> import sys
>>> def _init():
        locs = sys._getframe(1).f_locals   # Get callers local variables
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)
>>>
```

In this code, the local variables are extracted from the stack frame of the caller.
Here is a modified class definition:

```python
>>> class Stock:
        def __init__(self, name, shares, price):
            _init()

>>> s = Stock('GOOG', 100, 490.1)
>>> s.name
'GOOG'
>>> s.shares
100
>>>
```

At this point, you're probably feeling rather disturbed. Yes, you just wrote a function that reached
into the stack frame of another function and examined its local variables.
