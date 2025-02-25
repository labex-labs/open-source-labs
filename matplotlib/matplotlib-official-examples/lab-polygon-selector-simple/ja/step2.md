# プログラムで多角形を作成する

プログラムで多角形を作成するには、`Figure` オブジェクトと `Axes` オブジェクトを作成する必要があります。その後、`PolygonSelector` オブジェクトを作成してそれに頂点を追加できます。最後に、`Axes` 上に多角形を描画できます。

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

# 3つの頂点を追加する
selector.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# 多角形を描画する
ax.add_patch(plt.Polygon(selector.verts, alpha=0.3))
plt.show()
```
