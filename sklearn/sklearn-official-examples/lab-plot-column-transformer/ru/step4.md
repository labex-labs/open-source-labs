# Обучение и тестирование

Мы обучим нашу линейку на тренировочных данных и используем ее для предсказания тем для `X_test`. Затем выводятся метрики качества нашей линейки.

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```
