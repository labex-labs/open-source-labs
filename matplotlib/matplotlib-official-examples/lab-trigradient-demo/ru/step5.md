# Вычислите электрическое поле

```python
tci = CubicTriInterpolator(triang, -V)

(Ex, Ey) = tci.gradient(triang.x, triang.y)
E_norm = np.sqrt(Ex**2 + Ey**2)
```

Пояснение:

- `CubicTriInterpolator` - класс, который интерполирует данные с использованием кубического полинома.
- `tci` - экземпляр класса `CubicTriInterpolator`.
- `(Ex, Ey)` - электрическое поле.
- `E_norm` - нормализованное электрическое поле.
