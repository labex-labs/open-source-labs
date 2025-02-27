# Aplicar t-SNE a los datos

A continuación, aplicaremos t-SNE al conjunto de datos de círculos concéntricos.

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
