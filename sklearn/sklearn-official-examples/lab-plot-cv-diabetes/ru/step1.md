# Загрузка и подготовка датасета

Сначала мы загрузим и подготовим датасет о диабете. Для этого упражнения мы будем использовать только первые 150 образцов.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
