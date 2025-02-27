# スイスロールデータセットのLLEとt-SNE埋め込みの計算

`sklearn` の `manifold.locally_linear_embedding()` と `manifold.TSNE()` 関数をそれぞれ使って、スイスロールデータセットのLLEとt-SNE埋め込みを計算します。

```python
sr_lle, sr_err = manifold.locally_linear_embedding(sr_points, n_neighbors=12, n_components=2)

sr_tsne = manifold.TSNE(n_components=2, perplexity=40, random_state=0).fit_transform(sr_points)
```
