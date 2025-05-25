# Ajustar Modelos de Regressão Isotónica e Linear

Agora, ajustaremos os modelos de regressão isotónica e linear aos dados gerados.

```python
ir = IsotonicRegression(out_of_bounds="clip")
y_ = ir.fit_transform(x, y)

lr = LinearRegression()
lr.fit(x[:, np.newaxis], y)  # x precisa ser 2D para LinearRegression
```
