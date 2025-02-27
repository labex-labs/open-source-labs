# Comparer les coefficients estimés

Nous allons comparer les coefficients estimés du modèle réel, du modèle linéaire et du régresseur RANSAC.

```python
# Compare estimated coefficients
print("Estimated coefficients (true, linear regression, RANSAC):")
print(coef, lr.coef_, ransac.estimator_.coef_)
```
