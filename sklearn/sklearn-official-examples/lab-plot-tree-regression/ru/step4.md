# Предсказание

Мы будем использовать модели для предсказания значений в диапазоне от 0 до 5.

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```
