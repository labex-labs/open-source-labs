# 执行主成分分析（PCA）

既然我们已经对数据集进行了可视化，现在就让我们对其执行主成分分析。我们将为此使用 scikit-learn 的 `PCA()` 函数。我们将组件数量设置为 3，因为我们希望将数据集从 4 维（4 个特征）减少到 3 维。

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
