# Create data for ellipses

We create data for our ellipses in the form of arrays of x-coordinates, y-coordinates, width, height and angle.

```python
x = np.arange(10)
y = np.arange(15)
X, Y = np.meshgrid(x, y)

XY = np.column_stack((X.ravel(), Y.ravel()))

ww = X / 10.0
hh = Y / 15.0
aa = X * 9
```
