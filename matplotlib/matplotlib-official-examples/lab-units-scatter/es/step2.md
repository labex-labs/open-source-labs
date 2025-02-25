# Crear matriz enmascarada

En este paso, crearemos una matriz enmascarada y aplicaremos la máscara a los datos.

```python
# create masked array
data = (1, 2, 3, 4, 5, 6, 7, 8)
mask = (1, 0, 1, 0, 0, 0, 1, 0)
xsecs = secs * np.ma.MaskedArray(data, mask, float)
```
