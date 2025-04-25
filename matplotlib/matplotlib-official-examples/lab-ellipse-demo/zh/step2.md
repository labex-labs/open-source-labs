# 绘制单个椭圆

在这个示例中，我们将绘制许多具有随机大小、位置和颜色的椭圆。每个椭圆都将是`Ellipse`类的一个实例。

```python
# 固定随机状态以确保可重复性
np.random.seed(19680801)

# 要绘制的椭圆数量
NUM = 250

# 生成椭圆
ells = [Ellipse(xy=np.random.rand(2) * 10,
                width=np.random.rand(), height=np.random.rand(),
                angle=np.random.rand() * 360)
        for i in range(NUM)]

# 创建绘图并将纵横比设置为'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# 将每个椭圆添加到绘图中
for e in ells:
    ax.add_artist(e)
    e.set_clip_box(ax.bbox)
    e.set_alpha(np.random.rand())
    e.set_facecolor(np.random.rand(3))

# 设置绘图的 x 和 y 轴范围
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# 显示绘图
plt.show()
```
