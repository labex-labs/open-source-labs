# Generate Data

Next, we will generate the data that we will use to create the wireframe plot. In this lab, we will use the `np.meshgrid()` function to create the X, Y, and Z coordinates.

```python
# Generate data
X, Y = np.meshgrid(np.arange(-5, 5, 0.25), np.arange(-5, 5, 0.25))
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
