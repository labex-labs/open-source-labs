# 计算瑞士卷数据集的局部线性嵌入（LLE）和t-SNE嵌入

我们分别使用 `sklearn` 中的 `manifold.locally_linear_embedding()` 和 `manifold.TSNE()` 函数来计算瑞士卷数据集的局部线性嵌入（LLE）和t-SNE嵌入。

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
