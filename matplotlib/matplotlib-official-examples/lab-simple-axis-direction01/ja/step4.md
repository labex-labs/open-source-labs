# 軸のラベルの設定

`ax1.axis[]` 関数を使って、グラフの左右の軸のラベルを設定します。また、`set_axis_direction()` 関数を使って目盛りのラベルの方向を設定します。

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```
