# Calcular o campo elétrico

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Explicação:

- `CubicTriInterpolator` é uma classe que interpola dados usando um polinômio cúbico.
- `tci` é uma instância da classe `CubicTriInterpolator`.
- `(Ex, Ey)` é o campo elétrico.
- `E_norm` é o campo elétrico normalizado.
