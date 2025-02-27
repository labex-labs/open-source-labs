# Импортируем необходимые библиотеки и генерируем данные

Первым шагом является импорт необходимых библиотек и генерация данных. Мы будем использовать numpy и matplotlib для генерации и визуализации данных, а scikit-learn для построения модели одноклассовой SVM.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Генерируем обучающие данные
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Генерируем некоторые обычные новаторские наблюдения
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]

# Генерируем некоторые аномальные новаторские наблюдения
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
