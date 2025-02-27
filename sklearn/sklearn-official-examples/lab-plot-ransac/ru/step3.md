# Подберем регрессор RANSAC

Мы подберём регрессор RANSAC для данных с использованием класса RANSACRegressor из scikit-learn.

```python
# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
