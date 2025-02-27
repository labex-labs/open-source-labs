# Импортируем необходимые библиотеки и загружаем данные

Начнем с импорта необходимых библиотек и загрузки набора данных. В этом примере мы будем использовать набор данных Iris.

```python
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.datasets import load_iris
from sklearn.linear_model import Ridge

np.random.seed(0)
X, y = load_iris(return_X_y=True)
```
