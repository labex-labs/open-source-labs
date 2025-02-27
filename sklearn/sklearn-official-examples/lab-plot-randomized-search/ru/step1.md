# Импортируем необходимые библиотеки и загружаем данные

Начнем с импорта необходимых библиотек и загрузки набора данных digits из scikit-learn.

```python
import numpy as np
from time import time
import scipy.stats as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.datasets import load_digits
from sklearn.linear_model import SGDClassifier

# load digits dataset
X, y = load_digits(return_X_y=True, n_class=3)
```
