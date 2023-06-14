# Fit a Linear Regression Model

Next, we fit a linear regression model to the training set.

```python
from sklearn import linear_model

ols = linear_model.LinearRegression()
_ = ols.fit(X_train, y_train)
```


