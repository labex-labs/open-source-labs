# Generate Data

Next, we will generate some data to use for our regression. We will create a non-linear monotonic trend with homoscedastic uniform noise.

```python
n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50, 50, size=(n,)) + 50.0 * np.log1p(np.arange(n))
```


