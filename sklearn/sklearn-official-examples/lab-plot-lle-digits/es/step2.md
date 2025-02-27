# Graficar la función de incrustación

Definiremos una función auxiliar para graficar la incrustación. La función toma los datos de incrustación y el título para la gráfica como entrada. La función graficará cada dígito en la incrustación y mostrará una caja de anotación para un grupo de dígitos.

```python
import numpy as np
from matplotlib import offsetbox
from sklearn.preprocessing import MinMaxScaler

def plot_embedding(X, title):
    _, ax = plt.subplots()
    X = MinMaxScaler().fit_transform(X)

    for digit in digits.target_names:
        ax.scatter(
            *X[y == digit].T,
            marker=f"${digit}$",
            s=60,
            color=plt.cm.Dark2(digit),
            alpha=0.425,
            zorder=2,
        )
    shown_images = np.array([[1.0, 1.0]])  # solo algo grande
    for i in range(X.shape[0]):
        # graficar cada dígito en la incrustación
        # mostrar una caja de anotación para un grupo de dígitos
        dist = np.sum((X[i] - shown_images) ** 2, 1)
        if np.min(dist) < 4e-3:
            # no mostrar puntos que estén demasiado cerca
            continue
        shown_images = np.concatenate([shown_images, [X[i]]], axis=0)
        imagebox = offsetbox.AnnotationBbox(
            offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r), X[i]
        )
        imagebox.set(zorder=1)
        ax.add_artist(imagebox)

    ax.set_title(title)
    ax.axis("off")
```
