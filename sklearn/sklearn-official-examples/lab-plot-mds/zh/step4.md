# 执行多维缩放（MDS）

然后，我们将使用scikit-learn的MDS类对噪声数据集执行MDS。由于我们已经计算了数据点之间的成对距离，所以我们将使用预先计算的相异度选项。为了进行二维可视化，我们还将组件数量设置为2。

```python
mds = manifold.MDS(
    n_components=2,
    max_iter=3000,
    eps=1e-9,
    random_state=seed,
    dissimilarity="precomputed",
    n_jobs=1,
    normalized_stress="auto",
)
pos = mds.fit(similarities).embedding_
```
