# 多维缩放

多维缩放（Multidimensional scaling，MDS）旨在寻找数据的低维表示，其中的距离能很好地反映原始高维空间中的距离。

```python
md_scaling = manifold.MDS(
    n_components=n_components,
    max_iter=50,
    n_init=4,
    random_state=0,
    normalized_stress=False,
)
S_scaling = md_scaling.fit_transform(S_points)
```
