# Crear un kernel personalizado

En este paso, crearemos un kernel personalizado. El kernel personalizado será el producto punto de dos matrices. Crearemos una matriz M con los valores [[2, 0], [0, 1.0]]. Luego multiplicaremos las matrices X e Y por M y tomaremos su producto punto.

```python
def my_kernel(X, Y):
    """
    Creamos un kernel personalizado:

                 (2  0)
    k(X, Y) = X  (    ) Y.T
                 (0  1)
    """
    M = np.array([[2, 0], [0, 1.0]])
    return np.dot(np.dot(X, M), Y.T)
```
