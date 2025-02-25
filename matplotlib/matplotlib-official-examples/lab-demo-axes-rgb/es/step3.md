# Definir una función para crear un cubo RGB

En este paso, definiremos una función `make_cube()` para crear un cubo RGB a partir de los canales R, G y B obtenidos en el paso anterior. La función devolverá los cubos R, G y B, así como la imagen RGB.

```python
def make_cube(r, g, b):
    # Obtener la forma de R
    ny, nx = r.shape

    # Crear los cubos R, G y B
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Combinar los cubos R, G y B para crear la imagen RGB
    RGB = R + G + B

    return R, G, B, RGB
```
