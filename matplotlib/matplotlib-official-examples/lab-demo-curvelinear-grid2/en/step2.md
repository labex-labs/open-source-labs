# Define Transformation Functions

The second step is to define the transformation functions. In this example, we will use the `tr` function to transform the x-axis values and leave the y-axis values unchanged. The `inv_tr` function will be used to invert the transformation.

```python
def tr(x, y):
    return np.sign(x)*abs(x)**.5, y

def inv_tr(x, y):
    return np.sign(x)*x**2, y
```
