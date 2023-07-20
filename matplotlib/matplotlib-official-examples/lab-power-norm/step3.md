# Create Data

In this step, you need to create data using `multivariate_normal()`. This function generates a random sample from a multivariate normal distribution.

```python
data = np.vstack([
    multivariate_normal([10, 10], [[3, 2], [2, 3]], size=100000),
    multivariate_normal([30, 20], [[3, 1], [1, 3]], size=1000)
])
```
