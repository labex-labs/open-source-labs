# Create Artificial Data

We need to create some artificial data to plot. In this lab, we will plot the log of the frequency (in Hz) against the log of the power (in Watts). We will use the `numpy` library to generate the data.

```python
# Fixing random state for reproducibility
prng = np.random.RandomState(19680801)

# Create artificial data to plot.
# The x data span over several decades to demonstrate several SI prefixes.
xs = np.logspace(1, 9, 100)
ys = (0.8 + 0.4 * prng.uniform(size=100)) * np.log10(xs)**2
```
