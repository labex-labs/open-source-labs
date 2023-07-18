# Generate Data

We will generate some random data to use in our examples. We will use the NumPy function `random.lognormal()` to generate log-normal data with a mean of 1.5 and a standard deviation of 1.75. We will generate 37 samples of 4 variables, and we will store them in the `data` variable. We will also create a list of labels for each variable.

```python
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
```
