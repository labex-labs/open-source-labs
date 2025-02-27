# Загрузка данных

Начнем с загрузки датасета Iris и выбора только первых двух признаков для целей визуализации.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 0, :2]
y = y[y!= 0]
```
