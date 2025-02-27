# Calcular las proyecciones LLE y t-SNE del conjunto de datos Swiss Roll

Calculamos las proyecciones LLE y t-SNE del conjunto de datos Swiss Roll utilizando las funciones `manifold.locally_linear_embedding()` y `manifold.TSNE()` de `sklearn`, respectivamente.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
