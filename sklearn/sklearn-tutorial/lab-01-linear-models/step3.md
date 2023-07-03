# Lasso

#### Introduction:

Lasso is a linear regression method that adds a penalty term to the ordinary least squares objective function. The penalty term has the effect of setting some coefficients to exactly zero, thus performing feature selection. Lasso can be used for sparse model estimation.

#### Code:

Let's fit a lasso model.

```python
reg = linear_model.Lasso(alpha=0.1)
reg.fit([[0, 0], [1, 1]], [0, 1])

print(reg.coef_)
```

#### Explanation:

- We create an instance of `Lasso` with the regularization parameter `alpha` set to 0.1.
- We use the `fit` method to fit the model to the training data.
- We print the coefficients of the lasso model.
