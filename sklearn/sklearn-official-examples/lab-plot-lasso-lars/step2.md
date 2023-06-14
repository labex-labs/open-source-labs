# Compute Lasso Path

Next, we compute the Lasso Path using the LARS algorithm. The `lars_path` function from Scikit-Learn's `linear_model` module is used to compute the Lasso Path. The function takes the input features, target variable, and method as parameters. In this case, we use the "lasso" method for L1 regularization.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```


