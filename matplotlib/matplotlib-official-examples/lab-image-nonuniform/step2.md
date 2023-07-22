# Create Linear and Nonlinear Arrays

We need to create two arrays, one with linear values and another with non-linear values. These arrays will be used to create our NonUniformImage.

```python
# Linear x array for cell centers:
x = np.linspace(-4, 4, 9)

# Highly nonlinear x array:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
