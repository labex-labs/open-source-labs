# 対話的に多角形を作成する

対話的に多角形を作成するには、`Figure` オブジェクトと `Axes` オブジェクトを作成する必要があります。その後、`PolygonSelector` オブジェクトを作成し、プロット上をクリックすることでそれに頂点を追加できます。また、`shift` キーと `ctrl` キーを使って頂点を移動させることもできます。

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Click on the figure to create a polygon.")
print("Press the 'esc' key to start a new polygon.")
print("Try holding the 'shift' key to move all of the vertices.")
print("Try holding the 'ctrl' key to move a single vertex.")

plt.show()
```
