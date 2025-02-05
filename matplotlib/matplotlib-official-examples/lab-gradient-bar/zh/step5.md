# 创建图表

现在，我们可以创建图表了。我们将首先创建一个图形和一个坐标轴对象。然后，我们将设置坐标轴的 x 和 y 范围。我们将使用 `gradient_image()` 函数创建一个渐变背景。最后，我们将创建一个随机数据集，并使用 `gradient_bar()` 函数创建条形图。

```python
fig, ax = plt.subplots()
ax.set(xlim=(0, 10), ylim=(0, 1))

# 背景图像
gradient_image(ax, direction=1, extent=(0, 1, 0, 1), transform=ax.transAxes,
               cmap=plt.cm.RdYlGn, cmap_range=(0.2, 0.8), alpha=0.5)

N = 10
x = np.arange(N) + 0.15
y = np.random.rand(N)
gradient_bar(ax, x, y, width=0.7)
plt.show()
```
