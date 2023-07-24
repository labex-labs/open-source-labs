# Create data

Create an array of values between 0 and 15 in increments of 0.01, and convert them to radians using the radians function from the basic_units package.

```python
from basic_units import radians
x = [val*radians for val in np.arange(0, 15, 0.01)]
```
