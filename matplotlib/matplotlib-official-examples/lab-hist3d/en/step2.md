# Generate Data

Next, we will generate some random 2D data to use for the histogram. We will use NumPy's `random.rand()` function to generate 100 random values for both the x and y variables.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

x, y = np.random.rand(2, 100) * 4
```
