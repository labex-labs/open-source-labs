# Вычисление эмбеддингов LLE и t-SNE для набора данных Swiss-Hole

Мы вычисляем эмбеддинги LLE и t-SNE для набора данных Swiss-Hole с использованием функций `manifold.locally_linear_embedding()` и `manifold.TSNE()` из `sklearn` соответственно.

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
