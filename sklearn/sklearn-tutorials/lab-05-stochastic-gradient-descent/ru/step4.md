# Обучаем регрессор с использованием SGD

Далее мы обучим регрессор с использованием класса SGDRegressor. Мы будем использовать функцию потерь squared_error и штраф l2.

```python
# Train a regressor using SGD
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = reg.predict(X_test)

# Measure the mean squared error of the regressor
mse = mean_squared_error(y_test, y_pred)

# Print the mean squared error
print("Regressor Mean Squared Error:", mse)
```
