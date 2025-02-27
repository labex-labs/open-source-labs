# データにt-SNEを適用する

次に、同心円のデータセットにt-SNEを適用します。

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
