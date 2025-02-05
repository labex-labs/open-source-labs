# Set up histogram function to fixed bins

We will set up a histogram function with fixed bins using `numpy.histogram`. We will create 20 bins ranging from -3 to 3.

```python
edges = np.linspace(-3, 3, 20, endpoint=True)
hist_func = partial(np.histogram, bins=edges)
```
