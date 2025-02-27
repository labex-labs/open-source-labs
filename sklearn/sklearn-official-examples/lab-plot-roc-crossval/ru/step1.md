# Загрузка и подготовка данных

Сначала мы загрузим датасет iris с использованием библиотеки Scikit-learn. Датасет iris содержит 3 класса ирисных растений, и мы бинаризируем датасет, удалив один класс, чтобы создать задачу бинарной классификации. Также мы добавим шумовые признаки, чтобы сделать задачу более сложной.

```python
import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
target_names = iris.target_names
X, y = iris.data, iris.target
X, y = X[y!= 2], y[y!= 2]
n_samples, n_features = X.shape

# add noisy features
random_state = np.random.RandomState(0)
X = np.concatenate([X, random_state.randn(n_samples, 200 * n_features)], axis=1)
```
