# Exploring Stack Frame Inspection

While our `_init(locals())` approach works, it does require us to explicitly call `locals()` in every `__init__` method. We can make this even cleaner by using stack frame inspection to automatically access the caller's local variables.

Let's explore this technique in the Python interpreter:

```bash
cd ~/project
python3
```

First, we need to import the `sys` module, which provides access to some variables used or maintained by the Python interpreter:

```python
import sys
```

Next, let's define an improved version of our `_init()` function that accesses the caller's frame directly:

```python
def _init():
    # Get the caller's frame (1 level up in the call stack)
    frame = sys._getframe(1)

    # Get the local variables from that frame
    locs = frame.f_locals

    # Extract self and set other variables as attributes
    self = locs.pop('self')
    for name, val in locs.items():
        setattr(self, name, val)
```

Now, let's test this with a new version of our `Stock` class:

```python
class Stock:
    def __init__(self, name, shares, price):
        _init()  # No need to pass locals() anymore!

# Test it
s = Stock('GOOG', 100, 490.1)
print(s.name, s.shares, s.price)

# Also works with keyword arguments
s = Stock(name='AAPL', shares=50, price=125.3)
print(s.name, s.shares, s.price)
```

This approach is even cleaner from the caller's perspective - the `__init__` method no longer needs to explicitly pass `locals()`.

### How Stack Frame Inspection Works

When you call `sys._getframe(1)`, Python returns the frame object representing the caller's execution frame. The argument `1` means "one level up from the current frame" (the calling function).

A frame object contains information about the execution context, including:

- The current function being executed
- The local variables in that function
- The line number currently being executed

By accessing `frame.f_locals`, we get a dictionary of all local variables in the caller's scope, similar to what `locals()` would return if called directly from that scope.

This technique is powerful but should be used carefully. It's generally considered advanced and somewhat "magical" because it reaches outside the normal scope boundaries of Python.

Exit the Python interpreter when you're done experimenting:

```python
exit()
```
