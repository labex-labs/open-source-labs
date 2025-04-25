# 计算瑞士洞数据集的局部线性嵌入（LLE）和 t-SNE 嵌入

我们分别使用 `sklearn` 中的 `manifold.locally_linear_embedding()` 和 `manifold.TSNE()` 函数来计算瑞士洞数据集的局部线性嵌入（LLE）和 t-SNE 嵌入。

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
