# Creating Data

The next step is to create the data for the 3D surface. We need to define `u`, `v`, `x`, `y`, and `z`. These variables will represent the angles and coordinates required to plot the surface. The `linspace()` function from NumPy is used to create the angles, and the `outer()` function is used to create the coordinates.

```python
# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))
```
