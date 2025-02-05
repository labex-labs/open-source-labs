# 拟合 RANSAC 回归器

我们将使用 scikit-learn 的 RANSACRegressor 类对数据拟合一个 RANSAC 回归器。

```python
# 使用 RANSAC 算法稳健地拟合线性模型
ransac = linear_model.RANSACRegressor()
ransac.fit(X, y)
内点掩码 = ransac.inlier_mask_
外点掩码 = np.logical_not(内点掩码)
```
