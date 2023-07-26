# Compare estimated coefficients

We will compare the estimated coefficients of the true model, the linear model, and the RANSAC regressor.

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
