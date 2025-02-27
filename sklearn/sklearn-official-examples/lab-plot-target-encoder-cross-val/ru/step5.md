# Обучение регрессора Ridge с кросс-валидацией

Далее мы создадим конвейер (pipeline) с `TargetEncoder` и моделью Ridge. Конвейер использует `TargetEncoder.fit_transform`, который применяет кросс-валидацию. Выполните следующий код для обучения модели Ridge с кросс-валидацией:

```python
model_with_cv = make_pipeline(TargetEncoder(random_state=0), ridge)
model_with_cv.fit(X_train, y_train)
print("Model with CV on training set: ", model_with_cv.score(X_train, y_train))
print("Model with CV on test set: ", model_with_cv.score(X_test, y_test))
```
