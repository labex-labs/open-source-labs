# Crear matrices lineales y no lineales

Necesitamos crear dos matrices, una con valores lineales y otra con valores no lineales. Estas matrices se usarán para crear nuestra NonUniformImage.

```python
# Matriz x lineal para los centros de las celdas:
x = np.linspace(-4, 4, 9)

# Matriz x altamente no lineal:
x2 = x**3

y = np.linspace(-4, 4, 9)

z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
```
