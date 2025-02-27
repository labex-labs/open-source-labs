# Berechnung von LLE- und t-SNE-Embeddings für den Swiss Roll-Datensatz

Wir berechnen die LLE- und t-SNE-Embeddings des Swiss Roll-Datensatzes mithilfe der Funktionen `manifold.locally_linear_embedding()` und `manifold.TSNE()` aus `sklearn` respective.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
