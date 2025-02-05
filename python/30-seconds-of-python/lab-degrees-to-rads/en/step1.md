# Degrees to Radians

Write a function `degrees_to_rads(deg)` that takes an angle in degrees as an argument and returns the angle in radians. Your function should use the following formula to convert degrees to radians:

```
radians = (degrees * pi) / 180.0
```

where `pi` is a constant value representing the ratio of the circumference of a circle to its diameter (approximately 3.14159).

Your function should return the angle in radians rounded to 4 decimal places.

```python
from math import pi

def degrees_to_rads(deg):
  return (deg * pi) / 180.0
```

```python
degrees_to_rads(180) # ~3.1416
```
