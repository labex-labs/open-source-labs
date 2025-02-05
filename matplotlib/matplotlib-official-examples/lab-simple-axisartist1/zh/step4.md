# 创建子图 2

在第二个子图中，我们将使用 `axisartist.axislines.AxesZero` 自动创建 x 轴零点和 y 轴零点。我们将使其他脊线不可见，并将 x 轴零点设置为可见。

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
