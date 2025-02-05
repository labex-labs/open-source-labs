# 执行非度量多维缩放（Non-Metric MDS）

我们还将对同一数据集执行非度量多维缩放，以便进行比较。我们将使用与多维缩放相同的选项，只是将度量选项设置为False。

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
