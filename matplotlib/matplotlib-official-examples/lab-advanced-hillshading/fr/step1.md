# Affichage d'une barre de couleur pour un graphique ombré

Dans cette étape, vous allez apprendre à afficher une barre de couleur numérique correcte pour un graphique ombré.

```python
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LightSource, Normalize

def display_colorbar():
    """Afficher une barre de couleur numérique correcte pour un graphique ombré."""
    y, x = np.mgrid[-4:2:200j, -4:2:200j]
    z = 10 * np.cos(x**2 + y**2)

    cmap = plt.cm.copper
    ls = LightSource(315, 45)
    rgb = ls.shade(z, cmap)

    fig, ax = plt.subplots()
    ax.imshow(rgb, interpolation='bilinear')

    # Utiliser un artiste proxy pour la barre de couleur...
    im = ax.imshow(z, cmap=cmap)
    im.remove()
    fig.colorbar(im, ax=ax)

    ax.set_title('Utilisation d\'une barre de couleur avec un graphique ombré', size='x-large')
```
