# Set the random seed and generate the data

In this step, we will set the random seed and generate the data. We will generate 100 data points from a normal distribution with a mean of 200 and a standard deviation of 25.

```python
np.random.seed(19680801)
mu = 200
sigma = 25
data = np.random.normal(mu, sigma, size=100)
```
