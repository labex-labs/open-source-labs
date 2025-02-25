# Crear matrices enmascaradas

En este paso, crearemos tres matrices enmascaradas: una para valores mayores que un cierto umbral, una para valores menores que un cierto umbral y una para valores entre dos umbrales.

```python
upper = 0.77
lower = -0.77

supper = np.ma.masked_where(s < upper, s)
slower = np.ma.masked_where(s > lower, s)
smiddle = np.ma.masked_where((s < lower) | (s > upper), s)
```
