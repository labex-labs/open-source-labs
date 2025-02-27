# Appliquer t-SNE aux données

Ensuite, nous allons appliquer t-SNE à l'ensemble de données de cercles concentriques.

```python
t0 = time()
tsne = manifold.TSNE(
    n_components=n_components,
    init="random",
    random_state=0,
    perplexity=perplexity,
    n_iter=300,
)
Y = tsne.fit_transform(X)
t1 = time()
```
