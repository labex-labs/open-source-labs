# 选择性标记整个坐标轴上的水平区域

相同的选择机制可用于填充坐标轴的整个垂直高度。为了不受 y 轴范围的影响，我们添加一个变换，该变换将数据坐标中的 x 值和坐标轴坐标中的 y 值进行解释。以下示例标记了 y 数据高于给定阈值的区域。

```python
fig, ax = plt.subplots()
x = np.arange(0, 4 * np.pi, 0.01)
y = np.sin(x)
ax.plot(x, y, color='black')

threshold = 0.75
ax.axhline(threshold, color='green', lw=2, alpha=0.7)
ax.fill_between(x, 0, 1, where=y > threshold,
                color='green', alpha=0.5, transform=ax.get_xaxis_transform())
```

在这个示例中：

1. 创建了一个图形和坐标轴对象。
2. 生成了从 0 到 4π 的 x 值数组，并计算了对应的 y = sin(x) 值。
3. 绘制了黑色的曲线 y = sin(x)。
4. 设置了阈值为 0.75，并绘制了一条绿色的水平参考线。
5. 使用 `fill_between` 函数，通过 `where=y > threshold` 条件，在 x 轴数据范围内，从 y = 0 到 y = 1 的区域填充绿色，并且使用 `ax.get_xaxis_transform()` 进行坐标变换，使得填充区域不受 y 轴范围的影响。
