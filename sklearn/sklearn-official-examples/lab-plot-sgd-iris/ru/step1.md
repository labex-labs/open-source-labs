# Загрузка и подготовка данных

Начнем с импорта необходимых библиотек и загрузки набора данных iris. Затем перемешаем данные и стандартизируем их для использования в обучении.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# load iris dataset
iris = datasets.load_iris()

# take the first two features
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# shuffle the data
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# standardize the data
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
