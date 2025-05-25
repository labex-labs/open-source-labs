# Definir uma função para criar um cubo RGB

Nesta etapa, definiremos uma função `make_cube()` para criar um cubo RGB a partir dos canais R, G e B obtidos na etapa anterior. A função retornará os cubos R, G e B, bem como a imagem RGB.

```python
def make_cube(r, g, b):
    # Get the shape of R
    ny, nx = r.shape

    # Create the R, G, and B cubes
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Combine the R, G, and B cubes to create the RGB image
    RGB = R + G + B

    return R, G, B, RGB
```
