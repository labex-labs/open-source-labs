# 绘制不同角度的椭圆

在这个示例中，我们将绘制许多具有不同角度的椭圆。我们将使用一个循环为每个想要绘制的角度创建一个`Ellipse`实例。

```python
# 定义角度步长和要绘制的角度范围
angle_step = 45  # 度
angles = np.arange(0, 180, angle_step)

# 创建绘图并将纵横比设置为'equal'
fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

# 遍历角度并为每个角度绘制一个椭圆
for angle in angles:
    ellipse = Ellipse((0, 0), 4, 2, angle=angle, alpha=0.1)
    ax.add_artist(ellipse)

# 设置绘图的x和y轴范围
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

# 显示绘图
plt.show()
```
