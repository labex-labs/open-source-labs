# Calculer le potentiel électrique d'un dipôle

```python
def dipole_potential(x, y):
    """Le potentiel du dipôle électrique V, à la position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

Explication :

- `dipole_potential` est une fonction qui calcule le potentiel du dipôle électrique.
- `V` est un tableau de potentiels du dipôle électrique.
