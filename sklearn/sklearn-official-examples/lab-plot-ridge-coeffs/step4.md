# Train the model with different regularization strengths

We will train the model with different regularization strengths using a loop. We will set the regularization strength by changing the value of alpha in the `set_params` function. We will save the coefficients and errors for each value of alpha.

```python
coefs = []
errors = []

alphas = np.logspace(-6, 6, 200)

for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X, y)
    coefs.append(clf.coef_)
    errors.append(mean_squared_error(clf.coef_, w))
```
