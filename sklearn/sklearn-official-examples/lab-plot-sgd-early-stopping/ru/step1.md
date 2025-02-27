# Загрузка необходимых библиотек и датасета MNIST

Первым шагом является загрузка необходимых библиотек и датасета. Мы будем использовать библиотеки `pandas`, `numpy`, `matplotlib` и `scikit-learn`. Также мы будем использовать функцию `fetch_openml` из scikit-learn для загрузки датасета MNIST.

```python
import time
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils import shuffle

# Загрузка датасета MNIST
def load_mnist(n_samples=None, class_0="0", class_1="8"):
    """Загрузка MNIST, выбор двух классов, перемешивание и возврат только n_samples."""
    # Загрузка данных из http://openml.org/d/554
    mnist = fetch_openml("mnist_784", version=1, as_frame=False, parser="pandas")

    # выбираем только два класса для бинарной классификации
    mask = np.logical_or(mnist.target == class_0, mnist.target == class_1)

    X, y = shuffle(mnist.data[mask], mnist.target[mask], random_state=42)
    if n_samples is not None:
        X, y = X[:n_samples], y[:n_samples]
    return X, y

X, y = load_mnist(n_samples=10000)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
```
