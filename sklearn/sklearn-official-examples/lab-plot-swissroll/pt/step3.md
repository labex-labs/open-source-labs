# Calcular as Embeddings LLE e t-SNE do Conjunto de Dados Swiss Roll

Calculamos as embeddings LLE e t-SNE do conjunto de dados Swiss Roll usando as funções `manifold.locally_linear_embedding()` e `manifold.TSNE()`, respectivamente, de `sklearn`.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
