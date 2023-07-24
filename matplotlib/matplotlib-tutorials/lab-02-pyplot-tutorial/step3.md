# Plotting Multiple Lines

We can also plot multiple lines with different styles in one function call using arrays. Let's plot three lines: a dashed red line, blue squares, and green triangles:

```python
import numpy as np

t = np.arange(0., 5., 0.2)

plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

Explanation:

- We use the `numpy` module to create an array `t` with evenly sampled time values.
- The `plot` function is called with three pairs of `x` and `y` values, followed by the format strings `'r--'` (dashed red line), `'bs'` (blue squares), and `'g^'` (green triangles).
