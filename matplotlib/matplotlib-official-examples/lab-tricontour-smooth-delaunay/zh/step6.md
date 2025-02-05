# 改进三角剖分

我们使用 `TriAnalyzer` 通过移除三角剖分边界处形状不佳（扁平）的三角形来改进三角剖分。然后我们使用 `set_mask` 将掩码应用于三角剖分。

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
