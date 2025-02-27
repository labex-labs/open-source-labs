# Настройка регрессионной модели

Теперь мы инициализируем регрессоры градиентного бустинга и настраиваем их на наших тренировочных данных. Также давайте посмотрим на среднеквадратичную ошибку на тестовых данных.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```
