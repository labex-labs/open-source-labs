# Using Shortcut Functions

The `numpy.lib.npyio` module provides shortcut functions derived from `numpy.genfromtxt`. These functions have different default values and return either a standard NumPy array or a masked array.

```python
from numpy.lib.npyio import recfromtxt

recfromtxt(StringIO(data), delimiter=",")
```
