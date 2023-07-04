# Generate random data

We generate random data using NumPy's `np.random.uniform` method. We generate `npts = 200` data points with x and y values between -2 and 2. We also calculate the z values using the function `z = x * np.exp(-x**2 - y**2)`.

```python
np.random.seed(19680801)
npts = 200
x = np.random.uniform(-2, 2, npts)
y = np.random.uniform(-2, 2, npts)
z = x * np.exp(-x**2 - y**2)
```
