# 浮動軸を作成する

このステップでは、矩形ボックス内に極座標曲線を表示するために使用される 2 つの浮動軸を作成します。浮動軸を作成するには、`new_floating_axis()` を使用します。

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
