# Fit a RANSAC regressor

We will fit a RANSAC regressor to the data using scikit-learn's RANSACRegressor class.

```python
# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```


