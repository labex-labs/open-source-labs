# Preparación del conjunto de datos

Primero, cargamos y preprocesamos el conjunto de datos de caras Olivetti. Centramos los datos para que tengan media cero, tanto globalmente (centrando todos los datos en una característica) como localmente (centrando todas las características en una muestra). También definimos una función base para representar la galería de caras.

```python
# Carga y preprocesamiento del conjunto de datos de caras Olivetti.

import logging

from numpy.random import RandomState
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn import cluster
from sklearn import decomposition

rng = RandomState(0)

# Muestra los registros de progreso en la salida estándar
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
n_samples, n_features = faces.shape

# Centrado global (centrando todos los datos en una característica)
faces_centered = faces - faces.mean(axis=0)

# Centrado local (centrando todas las características en una muestra)
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

print("El conjunto de datos consta de %d caras" % n_samples)

# Define una función base para representar la galería de caras.

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


# Echemos un vistazo a nuestros datos. El color gris indica valores negativos,
# el blanco indica valores positivos.

plot_gallery("Caras del conjunto de datos", faces_centered[:n_components])
```
