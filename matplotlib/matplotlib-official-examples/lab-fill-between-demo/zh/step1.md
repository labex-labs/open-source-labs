# 基本用法

`fill_between` 函数可用于填充两条线之间的区域。参数 `y1` 和 `y2` 可以是标量，表示在给定 y 值处的水平边界。如果只给出 `y1`，则 `y2` 默认值为 0。

```python
x = np.arange(0.0, 2, 0.01)
y1 = np.sin(2 * np.pi * x)
y2 = 0.8 * np.sin(4 * np.pi * x)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(6, 6))

ax1.fill_between(x, y1)
ax1.set_title('fill between y1 and 0')

ax2.fill_between(x, y1, 1)
ax2.set_title('fill between y1 and 1')

ax3.fill_between(x, y1, y2)
ax3.set_title('fill between y1 and y2')
ax3.set_xlabel('x')
fig.tight_layout()
```

`fill_between` 函数的第一个示例填充了曲线 `y1` 与 x 轴（即 `y = 0`）之间的区域。第二个示例填充了曲线 `y1` 与水平直线 `y = 1` 之间的区域。第三个示例填充了曲线 `y1` 与曲线 `y2` 之间的区域。

每个子图都有一个标题，第三个子图还设置了 x 轴标签。`fig.tight_layout()` 用于自动调整子图布局，以避免标签重叠。
