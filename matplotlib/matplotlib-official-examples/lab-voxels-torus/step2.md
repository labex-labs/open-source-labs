# Define Midpoints Function

Next, we define a `midpoints` function to calculate the midpoints of an array of coordinates. This function will be used later to calculate the midpoints of `r`, `theta`, and `z`.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
