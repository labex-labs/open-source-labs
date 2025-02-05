# 设置轴方向

现在我们将创建一个图形对象，并为我们的绘图设置轴方向。我们将创建五个不同的子图来展示不同的轴方向。

```python
plt.rcParams.update({
    "axes.titlesize": "medium",
    "axes.titley": 1.1,
})

fig = plt.figure(figsize=(10, 4))
fig.subplots_adjust(bottom=0.1, top=0.9, left=0.05, right=0.95)

ax1 = setup_axes(fig, 251)
ax1.axis["x"].set_axis_direction("left")

ax2 = setup_axes(fig, 252)
ax2.axis["x"].label.set_text("Label")
ax2.axis["x"].toggle(ticklabels=False)
ax2.axis["x"].set_axislabel_direction("+")
ax2.set_title("标签方向 = $+$")

ax3 = setup_axes(fig, 253)
ax3.axis["x"].label.set_text("Label")
ax3.axis["x"].toggle(ticklabels=False)
ax3.axis["x"].set_axislabel_direction("$-$")
ax3.set_title("标签方向 = $-$")

ax4 = setup_axes(fig, 254)
ax4.axis["x"].set_ticklabel_direction("$+$")
ax4.set_title("刻度标签方向 = $+$")

ax5 = setup_axes(fig, 255)
ax5.axis["x"].set_ticklabel_direction("$-$")
ax5.set_title("刻度标签方向 = $-$")

ax7 = setup_axes(fig, 257)
ax7.axis["x"].label.set_text("旋转 = 10")
ax7.axis["x"].label.set_rotation(10)
ax7.axis["x"].toggle(ticklabels=False)

ax8 = setup_axes(fig, 258)
ax8.axis["x"].set_axislabel_direction("$-$")
ax8.axis["x"].label.set_text("旋转 = 10")
ax8.axis["x"].label.set_rotation(10)
ax8.axis["x"].toggle(ticklabels=False)

plt.show()
```
