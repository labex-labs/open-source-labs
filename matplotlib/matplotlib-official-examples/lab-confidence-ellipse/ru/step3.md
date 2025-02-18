# Определение функции `get_correlated_dataset`

Нам также нужна функция для генерации двумерного набора данных с заданным средним значением, размерами и корреляцией.

```python
def get_correlated_dataset(n, dependency, mu, scale):
    """
    Creates a random two-dimensional dataset with the specified
    two-dimensional mean (mu) and dimensions (scale).
    The correlation can be controlled by the param 'dependency',
    a 2x2 matrix.
    """
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # return x and y of the new, correlated dataset
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
```
