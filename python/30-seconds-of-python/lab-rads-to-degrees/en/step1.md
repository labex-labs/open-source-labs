# Radians to Degrees

Write a Python function called `rads_to_degrees` that takes a single argument `rad`, which is a float representing an angle in radians. The function should return the angle in degrees as a float. You can use the following formula to convert an angle from radians to degrees:

```
degrees = radians * (180 / pi)
```

where `pi` is a constant value representing the ratio of the circumference of a circle to its diameter, which is approximately equal to 3.14159.

Your function should import the `pi` constant from the `math` module.

```python
from math import pi

def rads_to_degrees(rad):
  return (rad * 180.0) / pi
```

```python
from math import pi

rads_to_degrees(pi / 2) # 90.0
```
