# Path オブジェクトを生成してそれからパッチを作成する

次に、Path オブジェクトを生成してそれからパッチを作成します。長方形を使ってヒストグラムを描画するために Path オブジェクトを使用します。次のコードを追加します。

```python
XY = np.array([[left, left, right, right], [bottom, top, top, bottom]]).T
barpath = path.Path.make_compound_path_from_polys(XY)
patch = patches.PathPatch(barpath)
patch.sticky_edges.y[:] = [0]
axs[0].add_patch(patch)
axs[0].autoscale_view()
```
