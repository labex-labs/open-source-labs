# Calcular el potencial eléctrico de un dipolo

```python
def dipole_potential(x, y):
    """El potencial eléctrico del dipolo V, en la posición *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

Explicación:

- `dipole_potential` es una función que calcula el potencial eléctrico del dipolo.
- `V` es una matriz de potenciales eléctricos del dipolo.
