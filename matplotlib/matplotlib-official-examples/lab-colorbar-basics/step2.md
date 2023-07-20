# Generate Data

We generate some sample data to plot, using `numpy`'s `mgrid` function.

```python
# setup some generic data
N = 37
x, y = np.mgrid[:N, :N]
Z = (np.cos(x*0.2) + np.sin(y*0.3))
```
