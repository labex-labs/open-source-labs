# Fit Non-Negative Least Squares Regression

We will now fit our data using non-negative least squares regression. This is done using scikit-learn's `LinearRegression` class with the `positive=True` parameter. We will then predict the values for our test set and calculate the R2 score.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
