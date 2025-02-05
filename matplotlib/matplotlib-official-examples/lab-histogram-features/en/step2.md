# Generate sample data

In this step, we will generate sample data using numpy. We will generate random data from a normal distribution with a mean of 100 and standard deviation of 15.

```python
np.random.seed(19680801)
mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(437)
```
