# Create Data

We will create a numpy array `x` containing 500 evenly spaced values between 0 and 3π. We will also create another numpy array `y` containing the sine of the values in `x`. Finally, we will create a numpy array `dydx` containing the first derivative of `y`.

```python
x = np.linspace(0, 3 * np.pi, 500)
y = np.sin(x)
dydx = np.cos(0.5 * (x[:-1] + x[1:]))
```
