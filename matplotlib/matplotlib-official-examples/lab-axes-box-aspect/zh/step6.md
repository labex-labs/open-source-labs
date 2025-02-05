# 多个子图的框体纵横比

可以在初始化时为坐标轴（Axes）指定框体纵横比。以下代码创建了一个 2 行 3 列的子图网格，其中所有坐标轴都是正方形的。

```python
fig7, axs = plt.subplots(2, 3, subplot_kw=dict(box_aspect=1),
                         sharex=True, sharey=True, layout="constrained")

for i, ax in enumerate(axs.flat):
    ax.scatter(i % 3, -((i // 3) - 0.5)*200, c=[plt.cm.hsv(i / 6)], s=300)
plt.show()
```
