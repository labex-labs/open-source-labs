# Preparação dos Dados

Nesta etapa, preparamos os dados para treino e teste. Usamos a função `load_digits` de `sklearn.datasets` para obter o conjunto de dados. Em seguida, geramos artificialmente mais dados rotulados perturbando os dados de treino com deslocamentos lineares de 1 pixel em cada direção. Escalamos os dados entre 0 e 1.

```python
import numpy as np
from scipy.ndimage import convolve
from sklearn import datasets
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split

def nudge_dataset(X, Y):
    """
    Isto produz um conjunto de dados 5 vezes maior que o original,
    deslocando as imagens 8x8 em X para a esquerda, direita, baixo, cima por 1px
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
X = minmax_scale(X, feature_range=(0, 1))  # Escala de 0 a 1

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
```
