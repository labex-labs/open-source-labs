# スイスホールデータセットの LLE と t-SNE 埋め込みの計算

`sklearn` の `manifold.locally_linear_embedding()` と `manifold.TSNE()` 関数をそれぞれ使って、スイスホールデータセットの LLE と t-SNE 埋め込みを計算します。

```python
sh_lle, sh_err = manifold.locally_linear_embedding(sh_points, n_neighbors=12, n_components=2)

sh_tsne = manifold.TSNE(n_components=2, perplexity=40, init="random", random_state=0).fit_transform(sh_points)
```
