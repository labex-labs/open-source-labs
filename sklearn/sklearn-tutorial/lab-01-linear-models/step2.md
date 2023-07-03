# Ridge Regression

#### Introduction:

Ridge regression is a linear regression method that adds a penalty term to the ordinary least squares objective function. This penalty term helps to reduce overfitting by shrinking the coefficients towards zero. The complexity of the model can be controlled by the regularization parameter.

#### Code:

Let's fit a ridge regression model.

```python
reg = linear_model.Ridge(alpha=0.5)
reg.fit([[0, 0], [0, 0], [1, 1]], [0, 0.1, 1])

print(reg.coef_)
```

#### Explanation:

- We create an instance of `Ridge` with the regularization parameter `alpha` set to 0.5.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the ridge regression model.
