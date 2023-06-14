# Fit Regression Model

Now we will initiate the gradient boosting regressors and fit it with our training data. Let's also look and the mean squared error on the test data.

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```


