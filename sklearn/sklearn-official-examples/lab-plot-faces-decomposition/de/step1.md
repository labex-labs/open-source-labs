# Datensatzvorbereitung

Zunächst laden und verarbeiten wir den Olivetti faces dataset. Wir zentrieren die Daten, sodass der Mittelwert null ist, sowohl global (konzentrieren sich auf eine eigenschaft, zentrieren alle samples) als auch lokal (konzentrieren sich auf ein sample, zentrieren alle eigenschaften). Wir definieren auch eine basisfunktion, um die galerie von gesichtern zu plotten.

```python
# Laden und Vorverarbeiten des Olivetti faces dataset.

import logging

from numpy.random import RandomState
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn import cluster
from sklearn import decomposition

rng = RandomState(0)

# Zeige Fortschrittslogs auf der Standardausgabe
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
n_samples, n_features = faces.shape

# Globale Zentrierung (konzentrieren sich auf eine eigenschaft, zentrieren alle samples)
faces_centered = faces - faces.mean(axis=0)

# Lokale Zentrierung (konzentrieren sich auf ein sample, zentrieren alle eigenschaften)
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

print("Datensatz besteht aus %d Gesichtern" % n_samples)

# Definiere eine basisfunktion, um die galerie von gesichtern zu plotten.

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


# Schauen wir uns unsere Daten an. Graue Farbe zeigt negative werte an,
# weiß zeigt positive werte an.

plot_gallery("Gesichter aus dem Datensatz", faces_centered[:n_components])
```
