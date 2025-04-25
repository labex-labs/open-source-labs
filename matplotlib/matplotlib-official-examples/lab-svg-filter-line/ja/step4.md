# 影を描画する

わずかなオフセットと灰色の同じ線を使って、線に影を描画します。影の線の色と z 順序を調整して、元の線の下に描画されるようにします。また、影の線用のオフセット変換を作成するために `offset_copy()` メソッドを使います。

```python
for l in [l1, l2]:
    xx = l.get_xdata()
    yy = l.get_ydata()
    shadow, = ax.plot(xx, yy)
    shadow.update_from(l)

    shadow.set_color("0.2")
    shadow.set_zorder(l.get_zorder() - 0.5)

    transform = mtransforms.offset_copy(l.get_transform(), fig1, x=4.0, y=-6.0, units='points')
    shadow.set_transform(transform)

    shadow.set_gid(l.get_label() + "_shadow")
```
