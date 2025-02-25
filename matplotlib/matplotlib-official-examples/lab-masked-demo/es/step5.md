# Establecer como NaN

Estableceremos como NaN donde y > 0.7. Crearemos una nueva matriz y con valores NaN.

```python
y4 = y.copy()
y4[y3 > 0.7] = np.nan
```
