# サブプロット1を作成する

最初のサブプロットでは、`axisartist.Axes` を使ってy = 0を通る新しい軸を作成します。また、他のスパインを非表示にします。

```python
ax0 = fig.add_subplot(gs[0, 0], axes_class=axisartist.Axes)
ax0.axis["y=0"] = ax0.new_floating_axis(nth_coord=0, value=0, axis_direction="bottom")
ax0.axis["y=0"].toggle(all=True)
ax0.axis["y=0"].label.set_text("y = 0")
ax0.axis["bottom", "top", "right"].set_visible(False)
```
