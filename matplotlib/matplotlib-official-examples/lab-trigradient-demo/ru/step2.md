# Вычислите электрический потенциал диполя

```python
def dipole_potential(x, y):
    """The electric dipole potential V, at position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

Пояснение:

- `dipole_potential` - функция, которая вычисляет электрический потенциал диполя.
- `V` - массив электрических потенциалов диполя.
