# Create data for the surface plot

In this step, we will create data for the surface plot. We will create a meshgrid of X and Y values, calculate the radial distance R, and calculate the Z value based on the R value using `np.sin()`.

```python
# Create data for the surface plot
X = np.arange(-5, 5, 0.25)
xlen = len(X)
Y = np.arange(-5, 5, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
```
