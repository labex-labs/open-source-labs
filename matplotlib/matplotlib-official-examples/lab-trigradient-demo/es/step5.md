# Calcular el campo eléctrico

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Explicación:

- `CubicTriInterpolator` es una clase que interpola datos utilizando un polinomio cúbico.
- `tci` es una instancia de la clase `CubicTriInterpolator`.
- `(Ex, Ey)` es el campo eléctrico.
- `E_norm` es el campo eléctrico normalizado.
