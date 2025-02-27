# Обучаем модель Kernel Ridge Regression

Теперь обучим модель Kernel Ridge Regression на этих данных. Будем использовать ядро RBF (Radial Basis Function), которое часто используется для нелинейной регрессии.

```python
# Fit Kernel Ridge Regression model
alpha = 1.0  # Параметр регуляризации
gamma = 0.1  # Коэффициент ядра для ядра RBF
krr = KernelRidge(alpha=alpha, kernel='rbf', gamma=gamma)
krr.fit(X, y)
```
