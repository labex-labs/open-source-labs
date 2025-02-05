# Compute the electrical field

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Explanation:

- `CubicTriInterpolator` is a class that interpolates data using a cubic polynomial.
- `tci` is an instance of the `CubicTriInterpolator` class.
- `(Ex, Ey)` is the electrical field.
- `E_norm` is the normalized electrical field.
