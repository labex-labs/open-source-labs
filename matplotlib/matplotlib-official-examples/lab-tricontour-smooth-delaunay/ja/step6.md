# 三角分割を改善する

三角分割の境界から形状が悪い（扁平な）三角形を取り除くことで三角分割を改善するために、`TriAnalyzer`を使用します。その後、`set_mask`を使ってマスクを三角分割に適用します。

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
