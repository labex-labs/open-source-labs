# 评估指标

我们可以使用评估指标来量化所得聚类的质量。我们将使用同质性、完整性、V 度量、调整兰德指数、调整互信息和轮廓系数等指标。我们将从 `sklearn.metrics` 模块中获取这些指标。如果真实标签未知，则只能使用模型结果本身进行评估。在这种情况下，轮廓系数就会派上用场。

```python
print(f"同质性：{metrics.homogeneity_score(labels_true, labels):.3f}")
print(f"完整性：{metrics.completeness_score(labels_true, labels):.3f}")
print(f"V 度量：{metrics.v_measure_score(labels_true, labels):.3f}")
print(f"调整兰德指数：{metrics.adjusted_rand_score(labels_true, labels):.3f}")
print(f"调整互信息：{metrics.adjusted_mutual_info_score(labels_true, labels):.3f}")
print(f"轮廓系数：{metrics.silhouette_score(X, labels):.3f}")
```
