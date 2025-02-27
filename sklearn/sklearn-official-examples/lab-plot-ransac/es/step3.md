# Ajustar un regresor RANSAC

Ajustaremos un regresor RANSAC a los datos utilizando la clase RANSACRegressor de scikit-learn.

```python
# Ajustar robustamente el modelo lineal con el algoritmo RANSAC
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
