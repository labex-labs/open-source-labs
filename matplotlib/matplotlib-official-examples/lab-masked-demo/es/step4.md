# Enmascarar puntos

Enmascararemos los puntos donde y > 0.7 usando una matriz enmascarada. Crearemos una nueva matriz y con los valores enmascarados.

```python
y3 = np.ma.masked_where(y > 0.7, y)
```
