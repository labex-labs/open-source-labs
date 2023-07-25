# Generate Data

We will generate 100,000 data points using `numpy.random.standard_normal()` and `numpy.random.standard_normal()`. `standard_normal()` generates random numbers from a standard normal distribution with a mean of 0 and a standard deviation of 1.

```python
np.random.seed(19680801)

n = 100_000
x = np.random.standard_normal(n)
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n)
xlim = x.min(), x.max()
ylim = y.min(), y.max()
```
