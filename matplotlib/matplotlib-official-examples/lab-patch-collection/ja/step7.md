# 多角形を作成する

`Polygon()` を使って多角形を作成し、パッチのリストに追加します。

```python
for i in range(N):
    polygon = Polygon(np.random.rand(N, 2), closed=True)
    patches.append(polygon)
```
