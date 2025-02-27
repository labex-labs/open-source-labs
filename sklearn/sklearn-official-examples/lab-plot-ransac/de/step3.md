# Einen RANSAC-Regressor anpassen

Wir werden einen RANSAC-Regressor an die Daten mit der RANSACRegressor-Klasse von scikit-learn anpassen.

```python
# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
