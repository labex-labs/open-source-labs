# Обучение регрессора Ridge на исходных данных

В этом разделе мы обучим регрессор Ridge на наборе данных с и без кодирования и исследуем влияние целевого кодировщика (target encoder) с и без интервального кросс-валидации. Сначала мы обучим модель Ridge на исходных признаках. Выполните следующий код для обучения модели Ridge:

```python
ridge = Ridge(alpha=1e-6, solver="lsqr", fit_intercept=False)

raw_model = ridge.fit(X_train, y_train)
print("Raw Model score on training set: ", raw_model.score(X_train, y_train))
print("Raw Model score on test set: ", raw_model.score(X_test, y_test))
```
