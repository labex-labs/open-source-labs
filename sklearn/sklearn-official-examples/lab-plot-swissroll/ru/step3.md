# Вычисление эмбеддингов LLE и t-SNE для набора данных Swiss Roll

Мы вычисляем эмбеддинги LLE и t-SNE для набора данных Swiss Roll с использованием функций `manifold.locally_linear_embedding()` и `manifold.TSNE()` из `sklearn` соответственно.

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
