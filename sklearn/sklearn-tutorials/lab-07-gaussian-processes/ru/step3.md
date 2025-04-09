# Гауссовая классификация (Gaussian Process Classification, GPC)

Класс GaussianProcessClassifier реализует GPC для вероятностной классификации. Он назначает априорное распределение GP для скрытой функции, которая затем сжимается с помощью связующей функции, чтобы получить вероятности классов. GPC поддерживает многоклассовую классификацию путем выполнения обучения и предсказания методом "один против остальных" (one-versus-rest) или "один против одного" (one-versus-one).

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.gaussian_process import GaussianProcessClassifier
# Создаем модель GPC с ядром RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Подгоняем модель под обучающие данные
model.fit(X_train, y_train)

# Предсказываем с использованием обученной модели
y_pred = model.predict(X_test)
```
