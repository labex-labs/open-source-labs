# Генерация кросс-валидированных предсказаний

Мы будем использовать функцию `cross_val_predict` из библиотеки scikit-learn для генерации кросс-валидированных предсказаний.

```python
from sklearn.model_selection import cross_val_predict

y_pred = cross_val_predict(lr, X, y, cv=10)
```
