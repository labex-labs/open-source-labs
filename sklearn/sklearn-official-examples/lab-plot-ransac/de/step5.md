# Vergleiche geschätzte Koeffizienten

Wir werden die geschätzten Koeffizienten des wahren Modells, des linearen Modells und des RANSAC-Regressors vergleichen.

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
