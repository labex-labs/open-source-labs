# Calcular las proyecciones LLE y t-SNE del conjunto de datos Swiss-Hole

Calculamos las proyecciones LLE y t-SNE del conjunto de datos Swiss-Hole utilizando las funciones `manifold.locally_linear_embedding()` y `manifold.TSNE()` de `sklearn`, respectivamente.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
