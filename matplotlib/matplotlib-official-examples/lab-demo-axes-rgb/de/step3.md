# Definieren einer Funktion zum Erstellen eines RGB-Würfels

In diesem Schritt definieren wir eine Funktion `make_cube()`, um einen RGB-Würfel aus den im vorherigen Schritt erhaltenen R-, G- und B-Kanälen zu erstellen. Die Funktion wird die R-, G- und B-Würfel sowie das RGB-Bild zurückgeben.

```python
def make_cube(r, g, b):
    # Holen Sie sich die Form von R
    ny, nx = r.shape

    # Erstellen Sie die R-, G- und B-Würfel
    R = np.zeros((ny, nx, 3))
    R[:, :, 0] = r
    G = np.zeros_like(R)
    G[:, :, 1] = g
    B = np.zeros_like(R)
    B[:, :, 2] = b

    # Verbinden Sie die R-, G- und B-Würfel, um das RGB-Bild zu erstellen
    RGB = R + G + B

    return R, G, B, RGB
```
