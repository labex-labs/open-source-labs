# Compute LLE and t-SNE Embeddings of Swiss-Hole Dataset

We compute the LLE and t-SNE embeddings of the Swiss-Hole dataset using the `manifold.locally_linear_embedding()` and `manifold.TSNE()` functions from `sklearn`, respectively.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
