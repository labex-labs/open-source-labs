# Mascareando los datos

En este paso, mascarearemos algunos de los valores de `z` utilizando una máscara booleana. Creamos una matriz `mask` utilizando la función `np.zeros_like()` y luego establecemos algunos de los valores en `True` para mascarearlos.

```python
# Mask various z values.
mask = np.zeros_like(z, dtype=bool)
mask[2, 3:5] = True
mask[3:5, 4] = True
mask[7, 2] = True
mask[5, 0] = True
mask[0, 6] = True
z = np.ma.array(z, mask=mask)
```
