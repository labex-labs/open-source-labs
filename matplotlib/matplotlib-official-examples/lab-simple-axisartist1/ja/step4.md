# サブプロット2を作成する

2番目のサブプロットでは、`axisartist.axislines.AxesZero` を使ってxzero軸とyzero軸を自動的に作成します。他のスパインを非表示にし、xzero軸を表示に設定します。

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
