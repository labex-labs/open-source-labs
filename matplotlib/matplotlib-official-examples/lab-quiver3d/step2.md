# Create the Grid

Next, we will create a grid of points on which we will display the vector field. In this example, we will create a meshgrid of points using NumPy's `meshgrid` function. The `arange` function is used to create an array of evenly spaced points within a specified interval.

```python
x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.2),
                      np.arange(-0.8, 1, 0.8))
```
