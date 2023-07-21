# Generate random data

In this step, we will generate random data for our scatter plot. We will be generating 50 data points for each variable using the NumPy library.

```python
np.random.seed(19680801)

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
```
