# 非計量MDSを実行する

比較のため、同じデータセットに対して非計量MDSも実行します。MDSと同じオプションを使用しますが、metricオプションをFalseに設定することを除きます。

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
