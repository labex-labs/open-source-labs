# Berechnung von LLE- und t-SNE-Embeddings für den Swiss-Hole-Datensatz

Wir berechnen die LLE- und t-SNE-Embeddings des Swiss-Hole-Datensatzes mithilfe der Funktionen `manifold.locally_linear_embedding()` und `manifold.TSNE()` aus `sklearn` respective.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
