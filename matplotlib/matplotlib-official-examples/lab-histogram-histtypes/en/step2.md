# Generate random data

We will generate two sets of random data using NumPy's `random.normal` function. These sets will be used to create histograms with different styles.

```python
np.random.seed(19680801)

mu_x = 200
sigma_x = 25
x = np.random.normal(mu_x, sigma_x, size=100)

mu_w = 200
sigma_w = 10
w = np.random.normal(mu_w, sigma_w, size=100)
```
