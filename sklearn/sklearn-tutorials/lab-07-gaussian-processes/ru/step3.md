# Гауссовая классификация (Gaussian Process Classification, GPC)

Класс GaussianProcessClassifier реализует GPC для вероятностной классификации. Он назначает априорное распределение GP для скрытой функции, которая затем сжимается с помощью связующей функции, чтобы получить вероятности классов. GPC поддерживает многоклассовую классификацию путем выполнения обучения и предсказания методом "один против остальных" (one-versus-rest) или "один против одного" (one-versus-one).

```python
from sklearn.gaussian_process import GaussianProcessClassifier

# Создаем модель GPC с ядром RBF
kernel = RBF()
model = GaussianProcessClassifier(kernel=kernel)

# Подгоняем модель под обучающие данные
model.fit(X_train, y_train)

# Предсказываем с использованием обученной модели
y_pred = model.predict(X_test)
```
