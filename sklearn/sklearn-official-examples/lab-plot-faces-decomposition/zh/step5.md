# 稀疏分量 - 小批量稀疏主成分分析（MiniBatchSparsePCA）

稀疏主成分分析（Sparse PCA）是主成分分析（PCA）的一种变体，它促使载荷向量具有稀疏性，从而得到更易于解释的分解结果。我们使用小批量稀疏主成分分析（MiniBatchSparsePCA），它是稀疏主成分分析（SparsePCA）的一个更快版本，更适合处理大型数据集。

```python
# 稀疏分量 - 小批量稀疏主成分分析（MiniBatchSparsePCA）
batch_pca_estimator = decomposition.MiniBatchSparsePCA(
    n_components=n_components, alpha=0.1, max_iter=100, batch_size=3, random_state=rng
)
batch_pca_estimator.fit(faces_centered)
plot_gallery(
    "稀疏分量 - 小批量稀疏主成分分析（MiniBatchSparsePCA）",
    batch_pca_estimator.components_[:n_components],
)
```
