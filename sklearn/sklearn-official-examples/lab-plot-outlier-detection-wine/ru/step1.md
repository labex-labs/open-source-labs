# Импортируем библиотеки и загружаем датасет

Начнем с импорта необходимых библиотек и загрузки датасета Wine из scikit-learn. Датасет Wine содержит информацию о различных видах вина, включая их химические свойства.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# Load dataset
X1 = load_wine()["data"][:, [1, 2]]  # two clusters
X2 = load_wine()["data"][:, [6, 9]]  # "banana"-shaped
```
