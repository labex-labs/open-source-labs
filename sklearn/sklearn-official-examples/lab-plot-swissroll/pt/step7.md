# Calcular Embeddings LLE e t-SNE do Conjunto de Dados Swiss-Hole

Calculamos os embeddings LLE e t-SNE do conjunto de dados Swiss-Hole usando as funções `manifold.locally_linear_embedding()` e `manifold.TSNE()` da biblioteca `sklearn`, respectivamente.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
