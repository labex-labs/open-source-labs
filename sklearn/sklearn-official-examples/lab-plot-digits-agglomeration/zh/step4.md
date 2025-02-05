# 执行特征凝聚

在这一步中，我们将使用scikit-learn中的`FeatureAgglomeration`类执行特征凝聚。我们将把聚类数量设置为32。

```python
agglo = cluster.FeatureAgglomeration(connectivity=connectivity, n_clusters=32)
agglo.fit(X)
X_reduced = agglo.transform(X)
```
