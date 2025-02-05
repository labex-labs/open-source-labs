# Add Noise to Data

In this step, we will add some noise to the data to make it more realistic. We will use NumPy's `normal` function to generate random numbers with a mean of 0.0 and a standard deviation of 0.3.

```python
# Add noise to the data
nse = np.random.normal(0.0, 0.3, t.shape) * s
```
