# Импорт необходимых библиотек и набора данных

Сначала мы импортируем необходимые библиотеки и загружаем набор данных Iris из scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF

iris = datasets.load_iris()
X = iris.data[:, :2]  # мы берем только первые два признака.
y = np.array(iris.target, dtype=int)
```
