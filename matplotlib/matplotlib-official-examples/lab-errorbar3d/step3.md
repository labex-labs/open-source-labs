# Generate Data for the Plot

We generate the data for our plot by creating a parametric curve. A parametric curve is a set of equations that describe the x, y, and z coordinates as a function of a parameter. We use NumPy's `arange` function to create an array of values from 0 to 2π. We then use these values to calculate the x, y, and z coordinates using trigonometric functions.

```python
t = np.arange(0, 2*np.pi+.1, 0.01)
x, y, z = np.sin(t), np.cos(3*t), np.sin(5*t)
```
