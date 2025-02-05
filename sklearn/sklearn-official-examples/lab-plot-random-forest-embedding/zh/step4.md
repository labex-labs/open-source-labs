# 使用截断奇异值分解（Truncated SVD）可视化降维后的结果

在这一步中，我们将使用截断奇异值分解来可视化降维后的结果。

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
