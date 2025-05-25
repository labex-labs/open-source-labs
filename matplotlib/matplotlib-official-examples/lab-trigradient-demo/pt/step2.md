# Calcular o potencial elétrico de um dipolo

```python
def dipole_potential(x, y):
    """The electric dipole potential V, at position *x*, *y*."""
    r_sq = x**2 + y**2
    theta = np.arctan2(y, x)
    z = np.cos(theta)/r_sq
    return (np.max(z) - z) / (np.max(z) - np.min(z))

V = dipole_potential(x, y)
```

Explicação:

- `dipole_potential` é uma função que calcula o potencial elétrico do dipolo.
- `V` é um array de potenciais elétricos do dipolo.
