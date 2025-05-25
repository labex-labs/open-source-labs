# Ajustar um regressor RANSAC

Ajustaremos um regressor RANSAC aos dados utilizando a classe `RANSACRegressor` do scikit-learn.

```python
# Ajustar robustamente o modelo linear com o algoritmo RANSAC
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
