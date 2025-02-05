# 创建并拟合分类器

我们创建一个收缩阈值为 0.2 的最近质心分类器实例，并对数据进行拟合。

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```
