# `from` module import

This picks selected symbols out of a module and makes them available locally.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

This allows parts of a module to be used without having to type the module prefix. It's useful for frequently used names.
