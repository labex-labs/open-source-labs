# Définissez une fonction pour créer un cube RGB

Dans cette étape, nous allons définir une fonction `make_cube()` pour créer un cube RGB à partir des canaux R, G et B obtenus dans l'étape précédente. La fonction retournera les cubes R, G et B, ainsi que l'image RGB.

```python
def make_cube(r, g, b):
    # Obtenez la forme de R
    ny, nx = r.shape

    # Créez les cubes R, G et B
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Combinez les cubes R, G et B pour créer l'image RGB
    RGB = R + G + B

    return R, G, B, RGB
```
