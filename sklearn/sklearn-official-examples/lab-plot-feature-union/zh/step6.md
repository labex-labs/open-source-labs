# 组合特征

我们将使用 `FeatureUnion` 变换器来组合从主成分分析（PCA）和单变量选择中获得的特征。

```python
combined_features = FeatureUnion([("pca", pca), ("univ_select", selection)])
```
