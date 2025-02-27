# Ajuster un régresseur RANSAC

Nous allons ajuster un régresseur RANSAC aux données à l'aide de la classe RANSACRegressor de scikit-learn.

```python
# Ajuster robustement un modèle linéaire avec l'algorithme RANSAC
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
