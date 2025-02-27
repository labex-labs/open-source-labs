# 多次元尺度法

多次元尺度法（Multidimensional scaling：MDS）は、元の高次元空間における距離を十分に反映する低次元表現を求めます。

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
