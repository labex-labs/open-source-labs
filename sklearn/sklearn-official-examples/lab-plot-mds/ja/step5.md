# 非計量 MDS を実行する

比較のため、同じデータセットに対して非計量 MDS も実行します。MDS と同じオプションを使用しますが、metric オプションを False に設定することを除きます。

```python
nmds = manifold.MDS(
    n_components=2,
    metric=False,
    max_iter=3000,
    eps=1e-12,
    dissimilarity="precomputed",
    random_state=seed,
    n_jobs=1,
    n_init=1,
    normalized_stress="auto",
)
npos = nmds.fit_transform(similarities, init=pos)
```
