# t-SNE auf die Daten anwenden

Als nächstes werden wir t-SNE auf den Datensatz mit den konzentrischen Kreisen anwenden.

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
