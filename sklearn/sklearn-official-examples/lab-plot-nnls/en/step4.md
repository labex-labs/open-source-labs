# Fit Classic Linear Regression

We will now fit our data using classic linear regression. This is done using scikit-learn's `LinearRegression` class. We will then predict the values for our test set and calculate the R2 score.

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
