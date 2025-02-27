# Convertir la Imagen a Puntos Flotantes y Redimensionar

Convertiremos la imagen a puntos flotantes y la redimensionaremos en una matriz numpy bidimensional para que pueda ser procesada por el algoritmo K-Means.

```python
# Convertir a puntos flotantes en lugar de la codificación entera de 8 bits por defecto.
china = np.array(china, dtype=np.float64) / 255

# Obtener las dimensiones de la imagen
w, h, d = original_shape = tuple(china.shape)
assert d == 3

# Redimensionar la imagen en una matriz numpy bidimensional
image_array = np.reshape(china, (w * h, d))
```
