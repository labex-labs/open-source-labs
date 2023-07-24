# Create Data for Visualization

Next, we will create a 2D grid that we will use for visualization. We can create a grid using the `meshgrid` function in NumPy. The `meshgrid` function creates a grid of points given two vectors, `x` and `y`, which represent the coordinates of the grid points. We will create a grid of 5x5 points using the following code block:

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
