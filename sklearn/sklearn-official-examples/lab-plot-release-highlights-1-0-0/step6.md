# Fit a Quantile Regression Model

Next, we will fit a quantile regression model to the training data using scikit-learn's `QuantileRegressor` class. We will set the quantile parameter to 0.5, which corresponds to the median.

```python
quantile_model = QuantileRegressor(alpha=0.5)
quantile_model.fit(X_train, y_train)
```
