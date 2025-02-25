# 方向矢印を逆にする

方向矢印を逆にしたい場合は、マーカーの種類を `>` から `<` に切り替えることができます。

```python
# To reverse the orientation arrow, switch the marker type from > to <.
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```
