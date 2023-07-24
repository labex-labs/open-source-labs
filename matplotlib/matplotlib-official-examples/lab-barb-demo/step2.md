# Create Data

Next, we will create the data that will be used to generate the wind barb plot. We will create a uniform grid of 5x5 and a vector field using the meshgrid and multiplication functions.

```python
x = np.linspace(-5, 5, 5)
X, Y = np.meshgrid(x, x)
U, V = 12 * X, 12 * Y
```
