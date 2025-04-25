# ランダムな線を生成する

`numpy`ライブラリを使って 12 本のランダムな線を生成し、`plot`メソッドを使って描画します。線が矩形と交差する場合、その色は赤色になり、それ以外の場合は青色になります。線を作成するために`Path`クラスを使い、矩形と交差するかどうかを確認するために`intersects_bbox`メソッドを使います。

```python
bbox = Bbox.from_bounds(left, bottom, width, height)

for i in range(12):
    vertices = (np.random.random((2, 2)) - 0.5) * 6.0
    path = Path(vertices)
    if path.intersects_bbox(bbox):
        color = 'r'
    else:
        color = 'b'
    ax.plot(vertices[:, 0], vertices[:, 1], color=color)
```
