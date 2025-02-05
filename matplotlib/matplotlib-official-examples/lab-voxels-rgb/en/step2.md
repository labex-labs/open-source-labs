# Defining the Coordinates and Colors

Next, we need to define the coordinates and colors for the plot. In this example, we will use the `np.indices` function to create a 17x17x17 grid of values for the RGB colors.

```python
r, g, b = np.indices((17, 17, 17)) / 16.0
```

We will also define a function `midpoints` to find the midpoints between the values in the grid. This will be used later to create the sphere.

```python
def midpoints(x):
    sl = ()
    for _ in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
