# 创建一个包含两个坐标轴的图形

在这一步中，我们创建一个包含两个坐标轴的图形。我们使用 `add_axes` 方法向图形中添加两个坐标轴。我们还为第一个坐标轴设置 y 轴刻度标签，并为第二个坐标轴设置标题。

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["非常长的标签"])
ax1.set_ylabel("Y 标签")

ax2.set_title("标题")
```
