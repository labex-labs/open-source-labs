# Fit the Regressors

We try a degree 10 polynomial to potentially overfit, though the bayesian linear models regularize the size of the polynomial coefficients. As `fit_intercept=True` by default for ARDRegression and BayesianRidge, then PolynomialFeatures should not introduce an additional bias feature. By setting `return_std=True`, the bayesian regressors return the standard deviation of the posterior distribution for the model parameters.

```python
ard_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    ARDRegression(),
).fit(X, y)
brr_poly = make_pipeline(
    PolynomialFeatures(degree=10, include_bias=False),
    StandardScaler(),
    BayesianRidge(),
).fit(X, y)

y_ard, y_ard_std = ard_poly.predict(X_plot, return_std=True)
y_brr, y_brr_std = brr_poly.predict(X_plot, return_std=True)
```
