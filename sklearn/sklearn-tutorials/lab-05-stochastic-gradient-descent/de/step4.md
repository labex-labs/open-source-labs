# Trainieren eines Regressors mit SGD

Als nächstes werden wir einen Regressor mit der SGDRegressor-Klasse trainieren. Wir werden die squared_error-Verlustfunktion und die l2-Strafe verwenden.

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
