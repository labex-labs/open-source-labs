# Ordinary Least Squares

Ordinary Least Squares (OLS) is a linear regression method that minimizes the sum of squared differences between the observed targets and the predicted targets. Mathematically, it solves a problem of the form:
$$\min_{w} || X w - y||_2^2$$

Let's start by fitting a linear regression model using OLS.

```python
from sklearn import linear_model

reg = linear_model.LinearRegression()
X = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit(X, y)

print(reg.coef_)
```

- We import the `linear_model` module from scikit-learn.
- We create an instance of `LinearRegression`.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the linear model.
