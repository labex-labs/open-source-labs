# Préparation des données

Dans cette étape, nous préparons les données pour l'entraînement et les tests. Nous utilisons la fonction `load_digits` de `sklearn.datasets` pour obtenir l'ensemble de données. Nous générons ensuite artificiellement plus de données étiquetées en perturbant les données d'entraînement avec des décalages linéaires de 1 pixel dans chaque direction. Nous échellons les données entre 0 et 1.

```python
import numpy as np
from scipy.ndimage import convolve
from sklearn import datasets
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split

def nudge_dataset(X, Y):
    """
    Cette fonction produit un ensemble de données 5 fois plus grand que l'original,
    en déplaçant les images 8x8 de X d'un pixel vers la gauche, la droite, le bas ou le haut
    """
    direction_vectors = [
        [[0, 1, 0], [0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [1, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0], [0, 1, 0]],
    ]

    def shift(x, w):
        return convolve(x.reshape((8, 8)), mode="constant", weights=w).ravel()

    X = np.concatenate(
        [X] + [np.apply_along_axis(shift, 1, X, vector) for vector in direction_vectors]
    )
    Y = np.concatenate([Y for _ in range(5)], axis=0)
    return X, Y

X, y = datasets.load_digits(return_X_y=True)
X = np.asarray(X, "float32")
X, Y = nudge_dataset(X, y)
X = minmax_scale(X, feature_range=(0, 1))  # Mise à l'échelle de 0 à 1

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```
