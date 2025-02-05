# 创建图形和子图

第二步是创建用于动画的图形和子图。在本示例中，我们创建两个并排的子图，它们具有不同的宽高比。左边的子图是一个单位圆，右边的子图是一个空图，将用于为一条正弦曲线制作动画。

```python
fig, (axl, axr) = plt.subplots(
    ncols=2,
    sharey=True,
    figsize=(6, 2),
    gridspec_kw=dict(width_ratios=[1, 3], wspace=0),
)
axl.set_aspect(1)
axr.set_box_aspect(1 / 3)
axr.yaxis.set_visible(False)
axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ["0", r"$\pi$", r"$2\pi$"])
```
