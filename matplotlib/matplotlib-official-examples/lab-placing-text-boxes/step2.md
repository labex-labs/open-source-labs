# Create data

For this example, we will create a random dataset using `numpy.random.randn()`.

```python
np.random.seed(19680801)
x = 30*np.random.randn(10000)
mu = x.mean()
median = np.median(x)
sigma = x.std()
```
