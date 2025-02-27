# Datenvorbereitung

In diesem Schritt bereiten wir die Daten für das Training und die Tests vor. Wir verwenden die Funktion `load_digits` aus `sklearn.datasets`, um den Datensatz zu erhalten. Anschließend erzeugen wir künstlich mehr markierte Daten, indem wir die Trainingsdaten um eine lineare Verschiebung von 1 Pixel in jeder Richtung stören. Wir skalieren die Daten zwischen 0 und 1.

```python
import numpy as np
from scipy.ndimage import convolve
from sklearn import datasets
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split

def nudge_dataset(X, Y):
    """
    Dies erzeugt einen Datensatz, der 5-mal größer als der ursprüngliche ist,
    indem die 8x8-Bilder in X um 1 Pixel nach links, rechts, unten, oben verschoben werden
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
X = minmax_scale(X, feature_range=(0, 1))  # 0-1 Skalierung

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```
