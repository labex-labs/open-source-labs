# 片側に外向きの目盛りラベル

このステップでは、片側に目盛りラベルが外向きになるサブプロットを作成します。

```python
ax = setup_axes(fig, 133)
ax.axis["left"].set_axis_direction("right")
ax.axis[:].major_ticks.set_tick_out(True)

ax.axis["left"].label.set_text("Long Label Left")
ax.axis["bottom"].label.set_text("Label Bottom")
ax.axis["right"].label.set_text("Long Label Right")
ax.axis["right"].label.set_visible(True)
ax.axis["left"].label.set_pad(0)
ax.axis["bottom"].label.set_pad(10)

plt.show()
```
