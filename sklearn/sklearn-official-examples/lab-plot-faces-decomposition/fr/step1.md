# Préparation du jeu de données

Tout d'abord, nous chargeons et prétraitons le jeu de données Olivetti faces. Nous centrons les données pour avoir une moyenne nulle, à la fois globalement (en se concentrant sur une caractéristique et en centrant toutes les échantillons) et localement (en se concentrant sur un échantillon et en centrant toutes les caractéristiques). Nous définissons également une fonction de base pour tracer la galerie de visages.

```python
# Chargement et prétraitement du jeu de données Olivetti faces.

import logging

from numpy.random import RandomState
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn import cluster
from sklearn import decomposition

rng = RandomState(0)

# Afficher les journaux de progression sur la sortie standard
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
n_samples, n_features = faces.shape

# Centrage global (en se concentrant sur une caractéristique, en centrant toutes les échantillons)
faces_centered = faces - faces.mean(axis=0)

# Centrage local (en se concentrant sur un échantillon, en centrant toutes les caractéristiques)
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

print("Le jeu de données contient %d visages" % n_samples)

# Définir une fonction de base pour tracer la galerie de visages.

n_row, n_col = 2, 3
n_components = n_row * n_col
image_shape = (64, 64)


def plot_gallery(title, images, n_col=n_col, n_row=n_row, cmap=plt.cm.gray):
    fig, axs = plt.subplots(
        nrows=n_row,
        ncols=n_col,
        figsize=(2.0 * n_col, 2.3 * n_row),
        facecolor="white",
        constrained_layout=True,
    )
    fig.set_constrained_layout_pads(w_pad=0.01, h_pad=0.02, hspace=0, wspace=0)
    fig.set_edgecolor("black")
    fig.suptitle(title, size=16)
    for ax, vec in zip(axs.flat, images):
        vmax = max(vec.max(), -vec.min())
        im = ax.imshow(
            vec.reshape(image_shape),
            cmap=cmap,
            interpolation="nearest",
            vmin=-vmax,
            vmax=vmax,
        )
        ax.axis("off")

    fig.colorbar(im, ax=axs, orientation="horizontal", shrink=0.99, aspect=40, pad=0.01)
    plt.show()


# Regardons notre données. La couleur grise indique des valeurs négatives,
# le blanc indique des valeurs positives.

plot_gallery("Visages du jeu de données", faces_centered[:n_components])
```
