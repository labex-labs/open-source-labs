# Preparação do Conjunto de Dados

Primeiro, carregamos e pré-processamos o conjunto de dados de rostos Olivetti. Centralizamos os dados para ter média zero, tanto globalmente (foco em um recurso, centralizando todas as amostras) quanto localmente (foco em uma amostra, centralizando todos os recursos). Também definimos uma função base para plotar a galeria de rostos.

```python
# Carregamento e pré-processamento do conjunto de dados de rostos Olivetti.

import logging

from numpy.random import RandomState
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn import cluster
from sklearn import decomposition

rng = RandomState(0)

# Exibir logs de progresso no stdout
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)
n_samples, n_features = faces.shape

# Centralização global (foco em um recurso, centralizando todas as amostras)
faces_centered = faces - faces.mean(axis=0)

# Centralização local (foco em uma amostra, centralizando todos os recursos)
faces_centered -= faces_centered.mean(axis=1).reshape(n_samples, -1)

print("O conjunto de dados consiste em %d rostos" % n_samples)

# Definir uma função base para plotar a galeria de rostos.

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


# Vamos dar uma olhada nos nossos dados. A cor cinza indica valores negativos,
# branco indica valores positivos.

plot_gallery("Rostos do conjunto de dados", faces_centered[:n_components])
```
