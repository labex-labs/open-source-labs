# RANSAC 回帰器の適合

scikit-learn の RANSACRegressor クラスを使って、データに RANSAC 回帰器を適合させます。

```python
# Robustly fit linear model with RANSAC algorithm
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
inlier_mask = ransac.inlier_mask_
outlier_mask = np.logical_not(inlier_mask)
```
