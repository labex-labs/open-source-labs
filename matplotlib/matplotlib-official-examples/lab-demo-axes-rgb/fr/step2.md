# Définissez une fonction pour obtenir les canaux RGB

Dans cette étape, nous allons définir une fonction `get_rgb()` pour obtenir les canaux R, G et B d'une image. Dans cet exemple, nous utiliserons la fonction `get_sample_data()` du module `cbook` pour obtenir une image d'échantillonnage.

```python
import matplotlib.cbook as cbook

def get_rgb():
    # Obtenez une image d'échantillonnage
    Z = cbook.get_sample_data("axes_grid/bivariate_normal.npy")
    Z[Z < 0] = 0.
    Z = Z / Z.max()

    # Obtenez les canaux R, G et B
    R = Z[:13, :13]
    G = Z[2:, 2:]
    B = Z[:13, 2:]

    return R, G, B
```
