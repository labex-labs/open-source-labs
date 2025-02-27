# Предскажем данные оцененных моделей

Мы предскажем данные линейной модели и регрессора RANSAC и сравним их результаты.

```python
# Predict data of estimated models
line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = lr.predict(line_X)
line_y_ransac = ransac.predict(line_X)
```
