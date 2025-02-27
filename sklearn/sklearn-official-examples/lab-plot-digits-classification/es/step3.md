# Preparar el conjunto de datos

Necesitamos aplanar las imágenes para convertir cada matriz bidimensional de valores de escala de grises de forma `(8, 8)` en forma `(64,)`. Esto nos dará un conjunto de datos de forma `(n_muestras, n_características)`, donde `n_muestras` es el número de imágenes y `n_características` es el número total de píxeles en cada imagen.

```python
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
```
