# Гауссовая регрессия (Gaussian Process Regression, GPR)

Класс GaussianProcessRegressor реализует Гауссовы процессы для задач регрессии. Для этого требуется указать априорное распределение для GP, например, функции среднего и ковариации. Гиперпараметры ядра оптимизируются в процессе подгонки модели. Рассмотрим пример использования GPR для регрессии.

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

# Создаем модель GPR с ядром RBF
kernel = RBF()
model = GaussianProcessRegressor(kernel=kernel)

# Подгоняем модель под обучающие данные
model.fit(X_train, y_train)

# Предсказываем с использованием обученной модели
y_pred = model.predict(X_test)
```
