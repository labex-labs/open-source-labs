# Compute LLE and t-SNE Embeddings of Swiss Roll Dataset

We compute the LLE and t-SNE embeddings of the Swiss Roll dataset using the `manifold.locally_linear_embedding()` and `manifold.TSNE()` functions from `sklearn`, respectively.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```


