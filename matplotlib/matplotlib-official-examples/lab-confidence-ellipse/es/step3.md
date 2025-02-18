# Definir la función `get_correlated_dataset`

También necesitamos una función para generar un conjunto de datos bidimensional con una media, dimensiones y correlación especificadas.

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    Crea un conjunto de datos bidimensional aleatorio con la media bidimensional (mu) y dimensiones (scale) especificadas.
    La correlación se puede controlar mediante el parámetro 'dependency',
    una matriz 2x2.
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # Devuelve x e y del nuevo conjunto de datos correlacionado
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```
